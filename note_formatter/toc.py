# (A new line, then a horizontal rule on a new line, and a new line after it)
HEADING_SEPARATOR = '\n<hr style="border-color:#52308c">\n\n' #extra \n before?

def has_toc(text: str) -> bool:
    return HEADING_SEPARATOR in text

def extract_headings(text: str) -> list:
    # A heading is in the format "# Some heading\n"
    # Resulting list in the form [[headingLnk, headingLvl],...]
    headings = []

    inCode = False # hashtags in code are not headings
    for line in text.split("\n"):
        if "```" in line: inCode = not inCode

        if not inCode:
            valid_heading = (len(line) > 2 # guard empty lines - at least "# ")
                        and line[0] == "#" # very start is a hashtag
                        and line.replace("#","")[0] == " ") # a space after any hashtags
            if valid_heading:
                heading_split = line.split(" ", 1)
                heading_lvl = len(heading_split[0])
                display_txt = heading_split[1]
                headings.append([display_txt, heading_lvl])
    return headings

def add_toc(text: str) -> str:
    # Get headings
    headings = extract_headings(text)
    heading_text = ""
    # Add each heading, including indentation level
    for heading in headings:
        heading_lvl = heading[1]
        heading_text += ("   " * (heading_lvl - 1)) + f"- [[#{heading[0]}]]\n"
    # Insert new TOC before main file contents
    heading_text += HEADING_SEPARATOR
    text = heading_text + text

    return text

# Remove EVERYTHING before the TOC delineation (should just be generated headings)
def remove_toc(text: str) -> str:
    if not has_toc(text):
        return text
    
    return text.split(HEADING_SEPARATOR)[1]