from pathlib import Path
import argparse

from note_formatter.formatter import format_text
from note_formatter.config import load_config, update_prev_path


def main():
    parser = argparse.ArgumentParser(
        prog="note-formatter",
        description="Format markdown notes, intended for Obsidian",
    )

    parser.add_argument(
        "input",
        nargs="?",
        help="(Markdown) file to process",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Separate output file path",
    )
    parser.add_argument(
        "-s",
        "--symbols",
        help="Custom symbol configuration",
    )
    parser.add_argument(
        "--no-toc",
        action="store_true",
        help="Disable automatic table of contents generation",
    )
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="Format the file in place",
    )

    args = parser.parse_args()

    if args.input is None:
        in_path, out_path = run_interactive(args)
    else:
        in_path, out_path = run_cli(args)

    text = read_file(in_path)
    formatted = format_text(text, not args.no_toc)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(formatted)

    update_prev_path(in_path)


def run_interactive(args) -> tuple[Path, Path]:
    in_path_str = (
        input("Enter input file path (press Enter to use previous path): ")
        .strip('"')
        .replace("\\", "/")
    )

    if in_path_str:
        in_path = Path(in_path_str)
    else:
        in_path = load_prev_path()

    if args.inplace:
        return in_path, in_path

    out_path_str = (
        input("Enter output file path (press Enter to use the input path): ")
        .strip('"')
        .replace("\\", "/")
    )

    if out_path_str:
        out_path = Path(out_path_str)
    else:
        out_path = in_path

    return in_path, out_path


def run_cli(args) -> tuple[Path, Path]:
    in_path = Path(args.input.replace("\\", "/"))

    if args.inplace:
        out_path = in_path
    elif args.output:
        out_path = Path(args.output.replace("\\", "/"))
    else:
        out_path = in_path

    return in_path, out_path


def load_prev_path() -> Path:
    prev_path = load_config()["previous_path"]
    return Path(prev_path.replace("\\", "/"))


def read_file(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    main()