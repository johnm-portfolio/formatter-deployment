from pathlib import Path
import re
from symbols import load_symbol_config
import toc

# print(len(load_symbol_config()["symbols"]))

def format_text(text: str) -> str:
    # Remove previous TOC
    text = toc.remove_toc(text)
    # Add new TOC
    text = toc.add_toc(text)

    # Replace symbols
    symbols = load_symbol_config()
    for symbol in symbols["symbols"]:
        for alias in symbol["inputs"]:
            text = text.replace(alias, symbol["output"])

    # Replace formulae
    for formulae in symbols["formulae"]:
        print(repr(formulae["replacement"]))
        text = re.sub(formulae["pattern"], formulae["replacement"], text)

    return text

TEST_PATH = Path(r"C:\Users\johnk\Documents\D&D\Obsidian\PIRATE CAMPAIGN\TEST.md")
with open(TEST_PATH, 'r', encoding="utf-8") as f:
    contents = f.read()
print(format_text(contents))
with open(TEST_PATH, 'w', encoding="utf-8") as f: f.write(format_text(contents))