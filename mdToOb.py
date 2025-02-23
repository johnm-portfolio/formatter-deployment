# NOTES
# - only works if there is at least one heading

import re

def writeTo(data,path):
    with open(path,"w",encoding="utf-8") as file:
        file.writelines(data)
def readFrom(path):
    with open(path,"r", encoding="utf-8", errors="replace") as file:
        data = file.readlines()
    return data

def format_LaTeX(text):
    replacements = [
        (r"!sum\((.*?)\)\((.*?)\)!", r"$\\sum_{\1}^{\2}$"), # Format sums
        (r"!sqrt\((.*?)\)!", r"$\\sqrt{\1}$"), # Format square roots
        (r"!\((.*?)\)/\((.*?)\)!", r"$\\frac{\1}{\2}$"), # Format fractions
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)
    return text

# Check for previous formatting and adjust
def checkPrevFormat(data):
    lineNum = 0
    for item in data:
        if '<hr style="border-color:#52308c">' in item:
            if data[lineNum + 1]=="\n":
                data = data[lineNum + 2:]
            else:
                data = data[lineNum + 1:]
            lineNum = 0
        lineNum += 1
    return data


def replaceSymbols(data, lineNumber):
    toReplace = [
        ["‘","'"],["’","'"],["“",'"'],["”",'"'],["!^!","∧"],["!->!","→"],["!|->!","↦"],["!<->!","↔"],["!<=!","≤"],["!>=!","≥"],["!!=!","≠"],["!=!","≡"],
            ["!!|!", "∤"],["!+-!","±"],["!~!","≈"],
        ["!0!","θ"],
        ["!a!","𝑎"],["!all!","∀"],["!alpha!","α"],["!AND!","∧"],["!approx!","≈"],
        ["!b!","𝑏"],["!B!","𝔹"],["!beta!","β"],
        ["!c!","𝑐"],["!complem!","<sup>c</sup>"],["!compos!","<sup>o</sup>"],["!conv!","⊗"],
        ["!deriv!","⊢"],
        ["!E!","∈"],["!!E!","∉"],["!empty!","∅"],["!eword!","ε"],["!entail!","⊨"],["!!entail!","⊭"],["!eps!","ε"],["!equiv!","⇔"],
        ["!f!","𝑓"],["!func!","𝑓"],
        ["!!","!!"],
        ["!!","!!"],
        ["!infinity!","∞"],["!imply!","⇒"],
        ["!!","!!"],
        ["!k!","𝑘"],
        ["!l!","𝑙"],["!log!","$㏒$"],
        ["!m!","𝑚"],
        ["!N!","ℕ"],["!n!","∩"],['!"n"!',"𝑛"],["!NOT!","¬"],
        ["!OMEGA!","Ω"],["!omega!","ω"],["!OR!","∨"],
        ["!p!","𝑝"],["!phi!","ϕ"],["!pi!","π"],["!power!","𝒫"],["!psub!","⊂"],["!psup!","⊃"],
        ["!q!","𝑞"],["!Q!","ℚ"],
        ["!r!","𝑟"],["!R!","ℝ"],
        ["!sigma!","Σ"],["!so!","∴"],["!some!","∃"],["!sqrt!","√"],
            ["!sub!","⊆"],["!sum!","Σ"],["!sup!","⊇"],
        ["!theta!","θ"],
        ["!u!","∪"],
        ["!v!","∨"],["!V!","∨"],
        ["!!","!!"],
        ["!x!","𝑥"],
        ["!y!","𝑦"],
        ["!z!","𝑧"],["!Z!","ℤ"],
    ]
    for replace in toReplace:
            data[lineNumber] = data[lineNumber].replace(replace[0], replace[1])
            data[lineNumber] = format_LaTeX(data[lineNumber])
    return data

def makeToC(data):
    # Find indexes of headingIndexes
    inCode = False
    headingIndexes = []
    for lineNum in range(len(data)):
        data = replaceSymbols(data, lineNum)
        if "```" in data[lineNum]:
            inCode = not inCode
        # If hasthag is part of a heading ("# someHeading" & not in code block)
        if data[lineNum][0] == "#" and data[lineNum].replace("#","")[0] == " " and not inCode:
            headingIndexes.append(lineNum)

    # Add links for each heading to ToC
    nextHeading = 0
    tableOfContents = []
    offset = 0
    for i in range(len(data)):
        numHashtags = 0
        if i == headingIndexes[nextHeading]:
            x = 0
            for char in data[i + offset]:
                if char == "#":
                    numHashtags += 1
                elif char == " ":
                    headingName = data[i + offset][x:].strip().replace("\n","")
                    break
                x += 1
            if i == 0 and numHashtags > 1:
                tableOfContents.append("- \n")
            # Make an Obsidian link ("[[#someHeading]]") with indentation based on heading level
            tableOfContents.append(f"{'    '*(numHashtags - 1)}- [[#{headingName}]]\n")
            if nextHeading == len(headingIndexes)-1:
                break
            else:
                nextHeading += 1

    # Add extra (HTML) formatting
    data.insert(0,'# <span class="highHeader">Table of Contents</span>\n')
    for i in range(len(tableOfContents)):
        data.insert(1, tableOfContents[len(tableOfContents) - i - 1])
    data.insert(len(tableOfContents) + 1, '<hr style="border-color:#52308c">\n')
    data.insert(len(tableOfContents) + 1, "\n")
    data.insert(len(tableOfContents) + 3, "\n")
    return data

def main():
    path=input("Enter a file name (or leave empty for previous file): ").replace('"','')
    if len(path) == 0:
        path = readFrom("prevPath.txt")[0].replace("\n","")
    else:
        writeTo([path], "prevPath.txt")
    data = readFrom(path)
    # Remove unneeded lines
    for i in range(len(data)):
        if len(data[i].strip().replace("\n","")) == 0:
            data.pop(i)
        else:
            break

    data = checkPrevFormat(data)

    data = makeToC(data)
    writeTo(data, path)

main()
