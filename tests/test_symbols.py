import json
from pathlib import Path
import re

SYMBOLS_PATH = Path(__file__).resolve().parents[1] / "note_formatter/data/symbols.json"

# Assume JSON format should have two non-empty lists, "symbols" and "formulae"
def test_symbols_json_loads():
    data = json.loads(SYMBOLS_PATH.read_text(encoding="utf-8"))
    assert "symbols" in data
    assert isinstance(data["symbols"], list)
    assert len(data["symbols"]) > 0

    assert "formulae" in data
    assert isinstance(data["formulae"], list)
    assert len(data["formulae"]) > 0

# Assume JSON formulae store actual Python regex
def test_formula_regex_compile():
    data = json.loads(SYMBOLS_PATH.read_text(encoding="utf-8"))

    for rule in data.get("formulae", []):
        re.compile(rule["pattern"])