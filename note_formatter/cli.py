from pathlib import Path
import sys
# from .formatter import process_content
import argparse

def main():
    print("GENIUS")
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
        input_path = input("Enter input file path: ").strip('"')
    else:
        input_path = args.input

    if args.output is None:
        output_path = load_prev_path()
    else:
        output_path = args.output

    print(args)

def load_prev_path():
    return

main()