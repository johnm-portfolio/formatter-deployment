from pathlib import Path
import json

CONFIG_DIR = (
        Path.home()
        / "AppData"
        / "Local"
        / "note_formatter"
    )

CONFIG_FILE = CONFIG_DIR / "config.json"

DEFAULT_CONFIG = {
        "previous_path": "",
        "custom_symbols": "",
        "default_generate_toc": True
    }

def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

def load_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)

    with open(CONFIG_FILE, encoding="utf-8") as f:
        return json.load(f)
    
def update_prev_path(new_prev_path):
    config = load_config()

    config["previous_path"] = str(
        Path(new_prev_path.replace("\"","")).resolve()
    )

    save_config(config)