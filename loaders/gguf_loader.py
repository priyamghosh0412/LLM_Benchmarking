from llama_cpp import Llama

def load_model(config):
    model = Llama(
        model_path=config["model_path"],
        n_ctx=2048,
        n_threads=4,          # Adjust to CPU cores
        n_gpu_layers=0,       # For CPU-only
        verbose=False
    )
    return model
