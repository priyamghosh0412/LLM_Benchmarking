import yaml
import os
config_path = os.path.join(os.path.dirname(__file__), "../config/model_config.yaml")
config_path = os.path.abspath(config_path)

def update_model_config(model_name, model_path, prompt):
    
    # Load existing config
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    config["models"] = {
        model_name.lower().replace(" ", "_"): {
            "name": model_name,
            "model_path": model_path,
            "loader": "gguf_loader",
            "max_tokens": 50,
            "prompt_template": "{prompt}" if not prompt else prompt
        }
    }

    # Save updated config
    with open(config_path, "w") as f:
        yaml.dump(config, f)
