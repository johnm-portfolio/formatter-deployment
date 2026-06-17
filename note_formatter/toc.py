# from typing import Array

def has_toc(text: str) -> bool:
    HEADING_DEMARKATION = '<hr style="border-color:#52308c">'
    return HEADING_DEMARKATION in text

def extract_headings(text: str) -> list:
    # Form [[headingLink, indLevel],...]
    headings = []
    headings.append(["One", 1])
    return headings

def add_toc(text: str) -> str:
    # Get headings
    headings = extract_headings(text)
    heading_text = "" + '\n\n<hr style="border-color:#52308c">\n'
    # Remove previous TOC
    text = remove_toc(text)
    # Insert new TOC before main file contents
    text = heading_text + "\n" + text

    return text

def remove_toc(text: str) -> str:
    return text

# print(extract_headings(""))