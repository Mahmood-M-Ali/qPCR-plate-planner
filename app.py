import os
import sys
import json
import time
import socket
import multiprocessing
import threading
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List
import atexit
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

# Global Lock to prevent concurrent inference collisions
inference_lock = threading.Lock()

AI_SYSTEM_PROMPT = """You are the "Sample Architect," a specialized PhD-level experimental designer. Your ONLY goal is to help researchers organize their samples into a perfect Cartesian Matrix for biological experiments.

### I. THE 3-DIMENSIONAL KNOWLEDGE MATRIX
You must act as a consultant to identify the 3 Dimensions of the user's experiment:
1. **Groups (Dimension 1):** The biological source (e.g., Cell Lines, Patient IDs, Mouse Models).
2. **Targets (Dimension 2):** The biological entity being measured (e.g., Genes of interest, Reference/Housekeeping genes). *Note: Reference genes are Targets, not Conditions.*
3. **Treatments (Dimension 3):** The experimental variable applied (e.g., Antibodies like IgG/H3K27me3, Drugs, siRNA, Time points, Untreated).

### II. CALIBRATION RANGES (Gamme de l'étalonnage)
If the user mentions "Standards," "Calibration Curve," or "Serial Dilution":
1. **The Range Interview:** You MUST ask for:
    - The **Starting Concentration** (e.g., 100 ng/uL).
    - The **Dilution Factor** (e.g., 1:10) OR specific **Custom Points**.
    - The **Number of Points** (e.g., 5-point curve).
2. **Role:** Set role to "Standard" for all samples in the calibration range.
3. **Naming:** Use the numeric concentration as the Treatment part (e.g., `HeLa_GAPDH_100`).
4. **Pfaffl Symmetry:** Remind the user that for high-accuracy Pfaffl efficiency correction, BOTH the Target gene AND the Reference gene should have matching calibration ranges.

### III. UNIVERSAL CARTESIAN EXPANSION
You must generate samples representing EVERY combination of the 3 Dimensions.
**Total Samples = (Number of Groups) × (Number of Targets) × (Number of Treatments).**
- *Standard Curve Exception:* If a Target has a Calibration Range, it generates N samples (where N = Number of Points) for that Target.
- **Rule of Symmetry:** If Target 'GAPDH' exists for the 'Untreated' condition, it MUST also exist for the 'Treated' condition.

### IV. STRICT NAMING CONVENTION
You MUST name EVERY sample using this exact format: `[Group]_[Target]_[Treatment]`.
- *Correct:* `HT_HOXD1_IgG`, `Ly18_CCNA1_100` (for a standard).
- *Incorrect:* `HT_IgG_HOXD1`.

**Role Assignment:** 
- Set role to "Standard" for calibration points.
- Set role to "Control" for Reference Targets (e.g., Housekeeping genes, Input) OR Control Treatments (e.g., IgG, Untreated).
- Set role to "Condition" for Targets of Interest undergoing active Treatment.

### V. INTERACTION PROTOCOL
1. **The Interview:** Acknowledge the user's intent. If any of the 3 Dimensions (Groups, Targets, Treatments) OR Calibration details (Start, Factor, Points) are missing, ask for them politely but briefly.
2. **The Draft:** Once all details are known, provide a bulleted "Experiment Plan" (e.g., "5-point standard curve + 3 groups x 2 treatments") and ask for confirmation.
3. **The Blueprint:** DO NOT output JSON until the user confirms.
4. **JSON Specs:** Output exactly ONE JSON block. Set `update_mode` to "replace".

=== EXAMPLE BLUEPRINT ===
{
  "experiment_name": "Factorial Study",
  "experimentType": "qpcr",
  "update_mode": "replace",
  "samples": [
    { "name": "CellA_RefGene_Untreated", "target": "RefGene", "role": "Control", "group": "CellA" },
    { "name": "CellA_RefGene_DrugX", "target": "RefGene", "role": "Control", "group": "CellA" },
    { "name": "CellA_TargetGene_Untreated", "target": "TargetGene", "role": "Control", "group": "CellA" },
    { "name": "CellA_TargetGene_DrugX", "target": "TargetGene", "role": "Condition", "group": "CellA" }
  ]
}
========================="""


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

app = FastAPI()

# ---------------------------------------------------------
# AI ENGINE (llama-cpp-python with HF Hub Download)
# ---------------------------------------------------------
print("--- DOWNLOADING NEURAL ENGINE (GEMMA-4-E2B) FROM HUB ---")
try:
    model_path = hf_hub_download(
        repo_id="unsloth/gemma-4-E2B-it-GGUF",
        filename="gemma-4-E2B-it-Q4_K_M.gguf"
    )
    print(f"--- GEMMA-4 DOWNLOADED TO: {model_path} ---")
except Exception as e:
    print(f"--- DOWNLOAD ERROR: {e} ---")
    model_path = None

print(f"--- INITIALIZING NEURAL ENGINE ---")

warmup_successful = False

try:
    if model_path:
        llm = Llama(
            model_path=model_path,
            n_ctx=8192,      
            n_threads=2,     
            n_batch=512,     
            verbose=True     
        )
        print("--- NEURAL ENGINE READY ---")
        
        # DEEP NEURAL WARMUP (Pre-calculates System Prompt KV Cache)
        print("--- PRIMING NEURAL CACHE (DEEP WARMUP) ---")
        try:
            # We process the actual system prompt so it's ready in memory for User 1
            llm.create_chat_completion(
                messages=[{"role": "system", "content": AI_SYSTEM_PROMPT}, {"role": "user", "content": "ping"}],
                max_tokens=1,
                stream=False
            )
            warmup_successful = True
            print("--- WARMUP COMPLETE: BRAIN IS HOT AND READY ---")
        except Exception as warmup_err:
            print(f"--- WARMUP SKIPPED: {warmup_err} ---")
            
    else:
        llm = None
except Exception as e:
    print(f"--- ENGINE INITIALIZATION ERROR: {e} ---")
    llm = None

# ---------------------------------------------------------
# API
# ---------------------------------------------------------

class ChatRequest(BaseModel):
    messages: List[dict]

@app.get("/api/status")
async def get_status():
    return {
        "engine": "online" if llm else "offline",
        "model": "ready" if llm else "error",
        "device": "Cloud CPU" if os.environ.get("SPACE_ID") else "Local CPU",
        "locked": inference_lock.locked(),
        "warmed_up": warmup_successful
    }

@app.post("/api/chat")
async def chat(request: ChatRequest):
    if not llm:
        return {"error": "AI Engine is offline."}

    try:
        def stream_response():
            with inference_lock:
                # SERVER-SIDE PROMPT INJECTION (Security + Cache Guarantee)
                # We force the backend prompt as the first message to guarantee KV cache hits
                input_messages = [{"role": "system", "content": AI_SYSTEM_PROMPT}]
                
                # Filter out any incoming system prompts from the client to prevent duplication
                client_messages = [m for m in request.messages if m.get("role") != "system" or "CURRENT DASHBOARD DATA" in m.get("content")]
                
                final_payload = input_messages + client_messages

                print(f"--- STARTING INFERENCE STREAM (Total: {len(final_payload)} messages) ---")
                try:
                    stream = llm.create_chat_completion(
                        messages=final_payload,
                        stream=True,
                        temperature=0.3,
                        max_tokens=2048,
                        repeat_penalty=1.1
                    )

                    chunk_count = 0
                    for chunk in stream:
                        if "choices" in chunk and len(chunk["choices"]) > 0:
                            delta = chunk["choices"][0].get("delta", {})
                            if "content" in delta:
                                yield delta["content"]
                                chunk_count += 1
                                if chunk_count == 1:
                                    print("--- FIRST CHUNK GENERATED ---")

                    print(f"--- INFERENCE COMPLETE: {chunk_count} chunks sent ---")
                except Exception as e:
                    print(f"INFERENCE ERROR: {str(e)}")
                    yield f"Inference Error: {str(e)}"

        return StreamingResponse(stream_response(), media_type="text/plain")
    except Exception as e:
        return {"error": f"Inference Error: {str(e)}"}


public_path = get_resource_path("public")
if os.path.exists(public_path):
    app.mount("/", StaticFiles(directory=public_path, html=True), name="public")
else:
    print(f"WARNING: Static files not found at {public_path}")
