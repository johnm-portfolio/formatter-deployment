# Symbol Formatter
## Contents
- [Symbol Formatter](#symbol-formatter)
  - [Contents](#contents)
  - [Installation](#installation)
  - [Description](#description)
  - [Purpose](#purpose)
  - [Symbol Table](#symbol-table)

## Installation
The program works by running a Python file, which will either take command line arguments or prompt for an input. There is a powershell shortcut "/runMdToOb.ps1" that will run the python file from any directory.
To make a shortcut that runs it, create a new shortcut with the location set to `powershell.exe -ExecutionPolicy Bypass -File "<yourPath>/runMdToOb.ps1"` where `<yourPath>` is replaced with the absolute path to the parent folder.
- e.g. `powershell.exe -ExecutionPolicy Bypass -File "C:Users/john/Documents/symbol_formatter/runMdToOb.ps1"`
- 
Alternatively, set the location as `powershell.exe -ExecutionPolicy Bypass -File runMdToOb.ps1` and then edit the Properties of it by right clicking on the created shortcut and setting the "Start In" to the absolute path (e.g. "C:/Users/john/Documents/symbol_formatter")

## Description
This program uses python to convert a custom format for representing commonly used symbols in Computer Science and Mathematics into the relevant text symbols or processed format.
- It sterilises the provided text, such as replacing symbols that represent quotation marks into actual quotation marks
- It also structures notes to include a customised table of contents at the top
[The website](https://symbol-formatter.netlify.app/) contains a filterable list of all the symbols and is up-to-date with the [Symbol table below](#symbol-table).

## Purpose
This program was designed to allow me to take notes in univeristy lectures much more efficiently, not having to worry about finding specific symbols, then copying and pasting them whenever needed. Creating this allowed my notes to be much more streamlined and I could quickly write out a representation for a symbol during a lecture - allowing me to pay better attention -, and afterwards, run a simple shortcut to execute the python script on a desired file path to format it as intended.
With regular use, common representations are easily remembered and I designed them to be as intuitive as possible, some 'symbols' having multiple different representations for ease of use. However, if any are forgotten having a table (like the one below) proves useful, I had one in my Obsidian vault (where I took notes) for quick reference.

## Symbol Table
Note that raw markdown text for symbols may contain backslashes to escape symbols such as $ that would cause LaTeX formatting to display as its symbol (if viewed in a markdown engine), this is so that the literal replacement can be visually seen.

_As of 23/02/2025_
|Symbol|Representation|Description|
|------|--------------|-----------|
|'|‘|Left single quote|
|'|’|Right single quote|
|"|“|Left double quote|
|"|”|Right double quote|
|∧|!^! or !AND!|Logical conjunction|
|→|!->!|Set/function mapping|
|↦|!\|->!|Element mapping|
|↔|!<->!|Double-sided arrow|
|≤|!<=!|Less than or equal to|
|≥|!>=!|Greater than or equal to|
|≡|!=!|Mathematical equivalence|
|≠|!!=!|Not equal to|
|∤|!!\|!|Not a factor of|
|±|!+-!|Plus-minus sign|
|\$\frac{a}{b}$|!(a)/(b)!|LaTeX fraction notation|
|||
|𝑎|!a!|Algebraic "a"|
|∀|!all!|Universal quantification|
|α|!alpha!|Greek lowercase alpha|
|≈|!approx! or !~!|Approximately equal to|
|||
|𝔹|!B!|Set of binary numbers|
|𝑏|!b!|Algebraic "b"|
|β|!beta!|Greek lowercase beta|
|||
|𝑐|!c!|Algebraic "c"|
|ᶜ|!complem!|Set complement|
|ᵒ|!compos!|Function composition|
|⊗|!conv!|Convolution|
|||
|⊢|!deriv!|Derivable|
|||
|∈|!E!|Set membership|
|∉|!!E!|Does not belong to|
|∅|!empty!|Empty set|
|ε|!eword!|Empty word|
|⊨|!entail!|Entailment|
|⊭|!!entail!|Does not entail|
|ε|!eps!|Greek lowercase epsilon|
|⇔|!equiv!|Logical equivalence|
|||
|𝑓|!func! or !f!|Function symbol|
|||
|𝑖|!i!|Algebraic "i"|
|∞|!infinity!|Infinity|
|⇒|!imply!|Logical implication|
|||
|𝑘|!k!|Algebraic "k"|
|||
|𝑙|!l!|Algebraic "l"|
|\$㏒$|!log!|Logarithm symbol|
|\$\㏒(a)$|!log(a)!|Logarithm symbol|
|||
|𝑚|!m!|Algebraic "m"|
|||
|ℕ|!N!|Set of natural numbers|
|𝑛|!"n"!|Algebraic "n"|
|∩|!n!|Set intersection|
|¬|!NOT!|Logical negation|
|||
|Ω|!OMEGA!|Greek uppercase omega|
|ω|!omega!|Greek lowercase omega|
|||
|𝑝|!p!|Algebraic "p"|
|ϕ|!phi!|Greek lowercase phi|
|π|!pi!|Pi|
|𝒫|!power!|Powerset|
|⊂|!psub!|Proper subset|
|⊃|!psup!|Proper Superset|
|||
|ℚ|!Q!|Set of rational numbers|
|𝑞|!q!|Algebraic "q"|
|||
|ℝ|!R!|Set of real numbers|
|𝑟|!r!|Algebraic "r"|
|||
|∴|!so!|Therefore|
|∃|!some!|Existential quantification|
|√|!sqrt!|Square root|
|\$\sqrt{a}$|!sqrt(a)!|LaTeX square root notation|
|⊆|!sub!|Improper subset|
|Σ|!sum! or !sigma!|Greek uppercase sigma (mathematical sum)|
|\$\sum_{a}^{b}$|!sum(a)(b)!|LaTeX sum notation|
|⊇|!sup!|Improper superset|
|||
|θ|!theta! or !0!|Greek lowercase theta|
|||
|∪|!u!|Set union|
|||
|∨|!V! or !v! or !OR!|Logical disjunction|
|||
|𝑥|!x!|Algebraic "x"|
|||
|𝑦|!y!|Algebraic "y"|
|||
|ℤ|!Z!|Set of integers|
|𝑧|!z!|Algebraic "z"|
