from pathlib import Path
import json

ROOT = Path(__file__).parent
SRC = ROOT / "shared/symbols.json"
WEB_DST = ROOT / "website/data/symbols.json"
PROJ_DST = ROOT / "note_formatter/data/symbols.json"

def build():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    WEB_DST.parent.mkdir(parents=True, exist_ok=True)
    WEB_DST.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    PROJ_DST.parent.mkdir(parents=True, exist_ok=True)
    PROJ_DST.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    build()