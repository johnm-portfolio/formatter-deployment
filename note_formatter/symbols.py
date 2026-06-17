from pathlib import Path
from importlib.resources import files
import json

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "shared/symbols.json"

def load_symbol_config() -> dict:
    return json.loads(SRC.read_text(encoding="utf-8"))