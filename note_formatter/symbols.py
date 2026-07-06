from pathlib import Path
from importlib.resources import files
import json

ROOT = Path(__file__).parent
SRC = ROOT / "data/symbols.json"

def load_symbol_config() -> dict:
    return json.loads(SRC.read_text(encoding="utf-8"))