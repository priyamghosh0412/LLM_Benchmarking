import gradio as gr
import shutil
import os
import subprocess
import pandas as pd
from utils.update_config import update_model_config

UPLOAD_DIR = "models"

def process_upload(gguf_file, model_name, prompt):
    if not gguf_file.name.endswith(".gguf"):
        return "❌ Please upload a valid .gguf file."

    # Save uploaded file to models directory
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    dest_path = os.path.join(UPLOAD_DIR, os.path.basename(gguf_file.name))
    shutil.move(gguf_file.name, dest_path)

    # Update YAML config
    update_model_config(model_name, dest_path, prompt)

    return f"✅ Model '{model_name}' registered and config updated."

def run_benchmark():
    try:
        subprocess.run(["python", "main.py"], check=True)

        # Load benchmark results
        df = pd.read_csv("benchmark_results.csv")
        return "✅ Benchmark complete!", df

    except subprocess.CalledProcessError as e:
        return f"❌ Benchmark failed: {e}", None
    except FileNotFoundError:
        return "❌ benchmark_results.csv not found.", None

# --- Gradio UI ---
with gr.Blocks() as demo:
    gr.Markdown("## 🧪 Local GGUF Model Benchmarking")

    with gr.Row():
        gguf_file = gr.File(label="Upload GGUF File", type="filepath")
        model_name = gr.Textbox(label="Model Name", placeholder="e.g. Gemma 2B (Q4)")
        prompt = gr.Textbox(label="Prompt Template", placeholder="Leave blank to use default: {prompt}")

    upload_btn = gr.Button("Register Model")
    output_msg = gr.Textbox(label="Upload Status")

    run_btn = gr.Button("Run Benchmark")
    benchmark_status = gr.Textbox(label="Benchmark Status")
    benchmark_table = gr.Dataframe(label="Benchmark Results")

    upload_btn.click(fn=process_upload,
                     inputs=[gguf_file, model_name, prompt],
                     outputs=output_msg)

    run_btn.click(fn=run_benchmark,
                  outputs=[benchmark_status, benchmark_table])

if __name__ == "__main__":
    demo.launch()


