from pathlib import Path
from note_formatter.formatter import format_text
# from ../formatter import format_text

DATA_DIR = Path(__file__).parent / "data"

def load_file(name: str) -> str:
    return (DATA_DIR / name).read_text(encoding="utf-8")

def test_format_text_matches_expected():
    input_text = load_file("input.md")
    expected = load_file("expected.md")

    result = format_text(input_text, True)

    assert result == expected