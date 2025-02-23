# NOTES
# - only works if there is at least one heading

import re

def writeTo(data,path):
    with open(path,"w",encoding="utf-8") as file:
        file.writelines(data)
        file.close()
def readFrom(path):
    with open(path,"r", encoding="utf-8", errors="replace") as file:
        data=file.readlines()
        file.close()
    return data

def format_LaTeX(inpt):
    # Format sums
    pattern = r"!sum\((.*?)\)\((.*?)\)!"
    replacement = r"$\\sum_{\1}^{\2}$"
    inpt = re.sub(pattern, replacement, inpt)
    # Format square roots
    pattern = r"!sqrt\((.*?)\)!"
    replacement = r"$\\sqrt{\1}$"
    inpt = re.sub(pattern, replacement, inpt)
    # Format fractions
    pattern = r"!\((.*?)\)/\((.*?)\)!"
    replacement = r"$\\frac{\1}{\2}$"
    inpt = re.sub(pattern, replacement, inpt)
    return inpt


def main():
    path=input("Enter a file name (or leave empty for previous file): ").replace('"','')
    if len(path)==0:
        path = readFrom("prevPath.txt")[0].replace("\n","")
    else:
        writeTo([path], "prevPath.txt")
    data=readFrom(path)
    for i in range(len(data)):
        if len(data[i].strip().replace("\n",""))==0:
            data.pop(i)
        else:
            break
    headings=[]
    count=0
    prevFormat=False
    for item in data:
        if '<hr style="border-color:#52308c">' in item:
            if data[count+1]=="\n":
                data=data[count+2:]
            else:
                data=data[count+1:]
            count=0
            headings=[]
            prevFormat=True
        elif prevFormat==True and item=="# Beginning\n":
            data=data[count:]
            break
        count+=1
    count=0
    inCode = False
    toReplace=[["‘","'"],["’","'"],["“",'"'],["”",'"'],["!^!","∧"],["!->!","→"],["!|->!","↦"],["!<->!","↔"],["!<=!","≤"],["!>=!","≥"],["!!=!","≠"],["!=!","≡"],
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
               ["!!","!!"],
               ["!!","!!"],
               ["!!","!!"],
               ["!N!","ℕ"],["!n!","∩"],["!NOT!","¬"],
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
                        
    for item in data:
        if "```" in item:
            if inCode==True:
                inCode=False
            else:
                inCode=True
        if item[0]=="#" and item.replace("#","")[0]==" " and not inCode:
            headings.append(count)
        for rep in toReplace:
            data[count]=data[count].replace(rep[0],rep[1])
            data[count] = format_LaTeX(data[count]) ##MAY CAUSE ISSUES?
        count+=1
    nextHeading=0
    table=[]
    offset=0
    for i in range(len(data)):
        numHashtags=0
        #print(i==headings[nextHeading])
        if i==headings[nextHeading]:
            x=0
            # Suggestion
            #numHashtags = data[i].count('#')
            #headingName = data[i].strip().replace("#", "").strip()

            for char in data[i+offset]:
                if char=="#":
                    numHashtags+=1
                if char==" ":
                    headingName=data[i+offset][x:].strip().replace("\n","")
                    #print(f"--{headingName}--")
                    break
                x+=1
            # print("\t"*(numHashtags-1)+"- "+headingName)
            #print(i,numHashtags)
            if i==0 and numHashtags>1:
                table.append("- \n")
            table.append(f"{'    '*(numHashtags-1)}- [[#{headingName}]]\n")
            if nextHeading==len(headings)-1:
                break
            else:
                nextHeading+=1
        else:
            if i==0 and headings[nextHeading]>i and prevFormat==False:
                data.insert(0,"# Beginning\n")
                offset=1
                table.insert(0,"- [[#Beginning]]\n")
    data.insert(0,'# <span class="highHeader">Table of Contents</span>\n')
    for i in range(len(table)):
        data.insert(1,table[len(table)-i-1])
    data.insert(len(table)+1,'<hr style="border-color:#52308c">\n')
    data.insert(len(table)+1,"\n")
    data.insert(len(table)+3,"\n")
    writeTo(data,path)

main()