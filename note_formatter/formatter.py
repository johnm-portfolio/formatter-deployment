from pathlib import Path
from symbols import load_symbol_config
import toc

# print(len(load_symbol_config()["symbols"]))

def format_text(text: str) -> str:
    # Remove previous TOC
    text = toc.remove_toc(text)
    # Add new TOC
    text = toc.add_toc(text)
    return text

def make_link(link: str, display: str) -> str:
    return f"[[{link}|{display}]]"

TEST_PATH = Path(r"C:\Users\johnk\Documents\D&D\Obsidian\PIRATE CAMPAIGN\TEST.md")
with open(TEST_PATH, 'r', encoding="utf-8") as f:
    contents = f.read()
print(format_text(contents))
with open(TEST_PATH, 'w', encoding="utf-8") as f: f.write(format_text(contents))