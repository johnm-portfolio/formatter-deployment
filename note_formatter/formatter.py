from pathlib import Path
import re
from symbols import load_symbol_config
import toc

# print(len(load_symbol_config()["symbols"]))

def format_text(text: str, generate_toc: bool) -> str:
    if generate_toc:
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
        text = re.sub(formulae["pattern"], formulae["replacement"], text)

    return text