from pathlib import Path
import sys
import argparse
from note_formatter.formatter import format_text
from note_formatter.config import load_config, update_prev_path

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
    parser.add_argument(
        "--inline",
        action="store_true",
        help="Format the file inline (use the same input and output path)"
    )
    args = parser.parse_args()

    inpt_path: Path | None = None
    out_path: Path | None = None

    if args.input is None:
        # Get user to enter the input path
        inpt_path_str = input("Enter input file path (press Enter to use previous path): ").strip('"').replace("\\","/")
        if inpt_path_str == "":
            inpt_path = load_prev_path()
        else:
            inpt_path = Path(inpt_path_str)
        # Get the user to enter the output path
        if args.inline:
            out_path = inpt_path
        else:
            out_path_str = input("Enter output file path (press Enter to use the input path): ").strip('"').replace("\\","/")
            if out_path_str == "":
                out_path = inpt_path
            else:
                out_path = Path(out_path_str)
                print(out_path)
        #TODO Get the user to enter the symbols path
    else:
        inpt_path = Path(args.input.replace("\\","/"))

    if args.inline:
        out_path = inpt_path
    elif args.input is not None:
        if args.output is None:
            out_path = inpt_path
        else:
            out_path = Path(args.output.replace("\\","/"))
    
    inpt_file_content = read_file(inpt_path)
    formatted_text = format_text(inpt_file_content, not args.no_toc)

    with open(out_path, 'w', encoding="utf-8") as f:
        f.write(formatted_text)

    update_prev_path(inpt_path)

def load_prev_path() -> Path:
    prev_path_str = load_config()["previous_path"]
    return Path(prev_path_str.replace("\\","/"))

def read_file(path: Path) -> str:
    with open(path, 'r', encoding="utf-8") as f:
        return f.read()

main()