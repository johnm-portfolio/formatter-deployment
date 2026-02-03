#!/usr/bin/env python3
print("Content-Type: text/html")
print()  # End of the headers

# TODO:
# - headings in the form "# [[someLink]]" or "# [[someLink|displayed]]"
#   - [[#Software Engineering/Course/Introduction to Algorithms and Data Structures/Week 3 Building a Data Structure Data Structures|Data Structures]]
# - add reverse process?

import re
import sys

def writeTo(data,path):
    with open(path,"w",encoding="utf-8") as file:
        file.writelines(data)
def readFrom(inputPath):
    with open(inputPath,"r", encoding="utf-8", errors="replace") as file:
        data = file.readlines()
    return data

def format_formulae(text):
    replacements = [
        (r"!sum\((.*?)\)\((.*?)\)!", r"$\\sum_{\1}^{\2}$"), # Format sums
        (r"!sqrt\((.*?)\)!", r"$\\sqrt{\1}$"), # Format square roots
        (r"!\((.*?)\)/\((.*?)\)!", r"$\\frac{\1}{\2}$"), # Format fractions
        (r"!log\((.*?)\)!", r"$\\log{\1}$"), # Format logarithms
        (r"!floor\((.*?)\)!", r"⌊\1⌋"), (r"!rdown\((.*?)\)!", r"⌊\1⌋"), # Format rounding up
        (r"!ceil\((.*?)\)!", r"⌈\1⌉"), (r"!rup\((.*?)\)!", r"⌈\1⌉") # Format rounding down
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
        ["!0!","θ"],
        ["!A!","𝐴"],["!a!","𝑎"],["!all!","∀"],["!alpha!","α"],["!AND!","∧"],["!approx!","≈"],
        ["!B!","𝔹"],["!b!","𝑏"],['!"B"!',"𝐵"],["!beta!","β"],
        ["!c!","𝑐"],["!chi!","χ"],["!complem!","<sup>c</sup>"],["!comp!","<sup>o</sup>"],["!conv!","⊗"],["!cross!","✕"],
        ["!d!","𝑑"],["!deg!","°"],["!DELTA!","∆"],["!delta!","δ"],["!deriv!","⊢"],["!dot!",r"$\cdot$"],
        ["!e!","𝑒"],["!empty!","∅"],["!eword!","ε"],["!entail!","⊨"],["!!entail!","⊭"],["!epsilon!","ε"],["!equiv!","⇔"],
        ["!F!","𝐹"],["!f!","𝑓"],["!func!","𝑓"],
        ["!G!","𝐺"],["!g!","𝑔"],["!gamma!","γ"],["!gtick!", '<span style="color:lightgreen">✓</span>'],
        ["!H!","𝐻"],["!h!","ℎ"],
        ["!I!","𝐼"],["!i!","𝑖"],["!inf!","∞"],["!infinity!","∞"],["!imply!","⇒"],
        ["!j!","𝑗"],
        ["!K!","𝐾"],["!k!","𝑘"],["!kron!","⊗"],
        ["!L!","𝐿"],["!l!","𝑙"],["!lambda!","λ"],["!log!",r"$\log$"],
        ["!M!","𝑀"],["!m!","𝑚"],["!mu!","μ"],
        ["!N!","ℕ"],['!"N"!',"𝑁"],['!~N!',"𝒩"],["!n!","∩"],['!"n"!',"𝑛"],["!NOT!","¬"],
        ["!o!","𝑜"],["!OMEGA!","Ω"],["!omega!","ω"],["!OR!","∨"],
        ["!P!","𝑃"],["!p!","𝑝"],["!part!","∂"],["!pdiff!","∂"],["!phi!","ϕ"],["!PI!",r"$\Pi$"],["!pi!","π"],["!power!","𝒫"],["!psub!","⊂"],["!psup!","⊃"],
        ["!Q!","ℚ"],['!"Q"!',"𝑄"],["!q!","𝑞"],
        ["!R!","ℝ"],['!"R"!',"𝑅"],["!~R!","ℛ"],["!r!","𝑟"],
            ["!rcross!",'<span style="color:red">✕</span>'],
        ["!S!","𝑆"],["!s!","𝑠"],["!SIGMA!","Σ"],["!sigma!","σ"],["!so!","∴"],["!some!","∃"],["!sqrt!","√"],
            ["!sub!","⊆"],["!sum!","Σ"],["!sup!","⊇"],
        ["!T!","𝑇 "],["!t!","𝑡"],["!theta!","θ"],["!tick!", "✓"],["!tri!","∆"],
        ["!U!","∪"],['!"U"!',"𝑈"],["!u!","𝑢"],
        ["!V!","∨"],["!v!","𝑣"],['!"V"!',"𝑉"],
        ["!w!","𝑤"],
        ["!X!","×"],['!"X"!',"𝑋"],["!x!","𝑥"],["!XO!","⊗"],
        ["!Y!","𝑌"],["!y!","𝑦"],
        ["!Z!","ℤ"],["!z!","𝑧"],
        ["‘","'"],["’","'"],["“",'"'],["”",'"'],["!^!","∧"],["!->!","→"],["!|->!","↦"],["!<->!","↔"],["!<-!","←"],
            ["!<=!","≤"],["!>=!","≥"],["!!=!","≠"],["!=!","≡"],
            ["!!|!", "∤"],["!+-!","±"],["!~!","<span style='font-size:21px'>~</span>"],["!~=!","≈"],["!.!","•"],
            # ["•", "-"],
            ["!!E!","∉"],["!E!","∈"]
    ]
    for replace in toReplace:
            data[lineNumber] = data[lineNumber].replace(replace[0], replace[1])
            data[lineNumber] = format_formulae(data[lineNumber])
    return data

def headingWithLink(heading):
    # Find the links within the heading name
    linkStart = -1
    links = []
    for i in range(len(heading)):
        if heading[i:i+3] == "[[#":
            linkStart = i
        if heading[i:i+2] == "]]" and linkStart != -1:
            links.append(heading[linkStart:i + 2])
            linkStart = -1
    
    # Parse and produce a link
    withoutLinks = heading
    toEnd = ""
    for link in links:
        if "|" in link:
            rename = link.split("|")[1].replace("]]","")
            withoutLinks = withoutLinks.replace(link, rename)
            toEnd = "|" + withoutLinks
        heading = heading.replace(link, (link.replace("[[","").replace("]]","").replace("#","").replace("|"," ")))
    
    return heading + toEnd

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
                # startHashFound = False
                for j in range(len(currLine)):
                    if currLine[j] == "#":
                        numHashtags += 1
                    elif currLine[j] == "<":
                        headingName = currLine[j:].strip().replace("\n","") + "|" + currLine[currLine.index(">") + 1 : currLine.index("</")]
                        break
                    elif currLine[j] == " ": # reached the space after hashtags (## myTitle)
                        if "[[#" in currLine:
                            headingName = headingWithLink(currLine[j:].replace("\n",""))
                            # headingName = currLine[2:].replace("\n","")
                            break
                        elif "|" in currLine:
                            headingName = currLine[j + 3:-2].replace("#", " ").replace("|", " ") + "|" + currLine[currLine.index("|") + 1:-3]
                            break
                        else:
                            headingName = currLine[j:].strip().replace("\n","")
                            if "<" not in currLine:
                                break
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
