from pathlib import Path
import sys
import argparse
from formatter import format_text
from config import load_config

def main():
    parser = argparse.ArgumentParser(
        prog="note-formatter",
        description="Format markdown notes, intended for Obsidian"
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="(Markdown) file to process"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Separate output file path"
    )
    parser.add_argument(
        "-s",
        "--symbols",
        help="Custom symbol configuration"
    )
    parser.add_argument(
        "--no-toc",
        action="store_true",
        help="Disable automatic table of contents generation"
    )
    args = parser.parse_args()

    if args.input is None:
        inpt_path_str = input("Enter input file path: ").strip('"').replace("\\","/")
        if inpt_path_str == "":
            inpt_path = load_prev_path()
        else:
            inpt_path = Path(inpt_path_str)
        #... and for output path
    else:
        inpt_path = Path(args.input.replace("\\","/"))

    if args.output is None:
        out_path = inpt_path
    else:
        out_path = Path(args.output.replace("\\","/"))

    print(inpt_path + " --> " + out_path)

    inpt_file_content = read_file(inpt_path)
    formatted_text = format_text(inpt_file_content)

    with open(out_path, 'w', encoding="utf-8") as f:
        f.write(formatted_text)

def load_prev_path():
    return load_config()["previous_path"]

def read_file(path: Path) -> str:
    with open(path, 'r', encoding="utf-8") as f:
        return f.read()

main()