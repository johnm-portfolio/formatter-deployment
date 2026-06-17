from pathlib import Path
from symbols import load_symbol_config
import toc

# print(len(load_symbol_config()["symbols"]))

def format_text(text: str) -> str:
    return text
    # Add TOC (includes replacing previous one)
    formatted_text = toc.add_toc(text)
    return formatted_text

def make_link(link: str, display: str) -> str:
    return f"[[{link}|{display}]]"

TEST_PATH = Path(r"C:\Users\johnk\Documents\D&D\Obsidian\PIRATE CAMPAIGN\TEST.md")
with open(TEST_PATH, 'r', encoding="utf-8") as f:
    contents = f.read()
print(format_text(contents))