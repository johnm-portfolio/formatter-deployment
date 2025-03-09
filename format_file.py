#!/usr/bin/env python3
print("Content-Type: text/html")
print()  # End of the headers

# TODO: headings in the form "# [[someLink]]" or "# [[someLink|displayed]]"

import re
import sys

def writeTo(data,path):
    with open(path,"w",encoding="utf-8") as file:
        file.writelines(data)
def readFrom(inputPath):
    with open(inputPath,"r", encoding="utf-8", errors="replace") as file:
        data = file.readlines()
    return data

def format_LaTeX(text):
    replacements = [
        (r"!sum\((.*?)\)\((.*?)\)!", r"$\\sum_{\1}^{\2}$"), # Format sums
        (r"!sqrt\((.*?)\)!", r"$\\sqrt{\1}$"), # Format square roots
        (r"!\((.*?)\)/\((.*?)\)!", r"$\\frac{\1}{\2}$"), # Format fractions
        (r"!log\((.*?)\)!", r"$\\log{\1}$"), # Format logarithms
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
            ["!!|!", "∤"],["!+-!","±"],["!~!","<span style='font-size:21px'>~</span>"],["!~=!","≈"],
        ["!0!","θ"],
        ["!a!","𝑎"],["!all!","∀"],["!alpha!","α"],["!AND!","∧"],["!approx!","≈"],
        ["!b!","𝑏"],["!B!","𝔹"],["!beta!","β"],
        ["!c!","𝑐"],["!complem!","<sup>c</sup>"],["!compos!","<sup>o</sup>"],["!conv!","⊗"],
        ["!delta!","δ"],["!deriv!","⊢"],
        ["!!E!","∉"],["!E!","∈"],["!empty!","∅"],["!eword!","ε"],["!entail!","⊨"],["!!entail!","⊭"],["!eps!","ε"],["!equiv!","⇔"],
        ["!f!","𝑓"],["!func!","𝑓"],
        ["!gamma!","γ"],
        ["!!","!!"],
        ["!i!","𝑖"],["!infinity!","∞"],["!imply!","⇒"],
        ["!!","!!"],
        ["!k!","𝑘"],
        ["!l!","𝑙"],["!log!","$㏒$"],
        ["!m!","𝑚"],
        ["!N!","ℕ"],['!"N"!',"𝒩"],["!n!","∩"],['!"n"!',"𝑛"],["!NOT!","¬"],
        ["!OMEGA!","Ω"],["!omega!","ω"],["!OR!","∨"],
        ["!p!","𝑝"],["!phi!","ϕ"],["!pi!","π"],["!power!","𝒫"],["!psub!","⊂"],["!psup!","⊃"],
        ["!q!","𝑞"],["!Q!","ℚ"],
        ["!r!","𝑟"],["!R!","ℝ"],
        ["!sigma!","Σ"],["!so!","∴"],["!some!","∃"],["!sqrt!","√"],
            ["!sub!","⊆"],["!sum!","Σ"],["!sup!","⊇"],
        ["!theta!","θ"],["!tick!", "✓"],
        ["!u!","∪"],
        ["!v!","∨"],["!V!","∨"],
        ["!!","!!"],
        ["!x!","𝑥"],["!X!","✕"],
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
            if data[lineNum - 1][0:2] == "- ":
                data[lineNum - 1] = data [lineNum - 1] + "\n"

    # Add links for each heading to ToC
    if len(headingIndexes) > 0:
        nextHeading = 0
        tableOfContents = []
        offset = 0
        for i in range(len(data)):
            currLine = data[i + offset]
            numHashtags = 0
            if i == headingIndexes[nextHeading]:
                x = 0
                for j in range(len(currLine)):
                    if currLine[j] == "#":
                        numHashtags += 1
                    elif currLine[j] == "<":
                        headingName = currLine[x:].strip().replace("\n","") + "|" + currLine[currLine.index(">") + 1 : currLine.index("</")]
                        break
                    elif currLine[j] == " ":
                        headingName = currLine[x:].strip().replace("\n","")
                        if "<" not in currLine:
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
    # If not called from XAMPP
    if len(sys.argv) != 3:
        inputPath = input("Enter a file name (or leave empty for previous file): ").replace('"','')
        if len(inputPath) == 0:
            inputPath = readFrom("prevPath.txt")[0].replace("\n","")
        else:
            writeTo([inputPath], "prevPath.txt")
    else:
        inputPath = sys.argv[1]
        outputFile = sys.argv[2]
    data = readFrom(inputPath)
    # Remove unneeded lines
    for i in range(len(data)):
        if len(data[i].strip().replace("\n","")) == 0:
            data.pop(i)
        else:
            break

    data = checkPrevFormat(data)
    data = makeToC(data)

    if len(sys.argv) == 3:
        try:
            writeTo(data, outputFile)
        except Exception as e:
            print("Error processing file:", e)
            sys.exit(1)
    else:
        writeTo(data, inputPath)

main()

#########
# def process_content(content):
#     # Example: convert text to uppercase
#     return content.upper()

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python3 process_file.py input_file output_file")
#         sys.exit(1)
    
#     input_file = sys.argv[1]
#     output_file = sys.argv[2]
    
#     try:
#         with open(input_file, "r", encoding="utf-8") as infile:
#             content = infile.read()
#         new_content = process_content(content)
#         with open(output_file, "w", encoding="utf-8") as outfile:
#             outfile.write(new_content)
#     except Exception as e:
#         print("Error processing file:", e)
#         sys.exit(1)
