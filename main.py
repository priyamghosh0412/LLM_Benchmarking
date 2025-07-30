import yaml
import importlib
from benchmarks.latency_benchmark import generate_and_time
from utils.csv_writer import write_csv

PROMPT = "Explain what large language models are in simple terms."

def load_config(path="config/model_config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)["models"]

def run_benchmark():
    models_config = load_config()
    results = []

    for model_id, config in models_config.items():
        loader = importlib.import_module(f"loaders.{config['loader']}")
        model = loader.load_model(config)

        timing = generate_and_time(
            model=model,
            prompt=PROMPT,
            max_tokens=config["max_tokens"],
            prompt_template=config.get("prompt_template")
        )

        verdict = "Too slow (low TPM)" if timing["tokens_per_min"] < 30 else "Acceptable performance"
        runnable = "❌ Not Runnable" if timing["tokens_per_min"] < 30 else "✅ Runnable"

        results.append({
            "model": config["name"],
            "load_time": "-",  # llama-cpp-python does not provide separate load time
            "first_token": round(timing["avg_token"], 3),
            "avg_token": round(timing["avg_token"], 3),
            "tokens_per_min": round(timing["tokens_per_min"], 2),
            "verdict": verdict,
            "runnable": runnable
        })

    write_csv(results)

if __name__ == "__main__":
    run_benchmark()
