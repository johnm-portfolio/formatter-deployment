# Symbol Formatter
## Contents
- [Symbol Formatter](#symbol-formatter)
  - [Contents](#contents)
  - [Installation](#installation)
    - [Initial Setup](#initial-setup)
    - [Shortcut Setup](#shortcut-setup)
  - [Usage](#usage)
  - [Description](#description)
  - [Purpose](#purpose)
  - [Symbol Table](#symbol-table)
  - [Example](#example)

## Installation
### Initial Setup
Build the project, includes copying symbol JSON data
```shell
# From root directory
python build.py
```

### Shortcut Setup
The program works by running a Python file, which will either take command line arguments or prompt for an input. There is a powershell shortcut "/runMdToOb.ps1" that will run the python file from any directory.
To make a shortcut that runs it, create a new shortcut with the location set to `powershell.exe -ExecutionPolicy Bypass -File "<yourPath>/runMdToOb.ps1"` where `<yourPath>` is replaced with the absolute path to the parent folder.
- e.g. `powershell.exe -ExecutionPolicy Bypass -File "C:Users/john/Documents/symbol_formatter/runMdToOb.ps1"`
- 
Alternatively, set the location as `powershell.exe -ExecutionPolicy Bypass -File runMdToOb.ps1` and then edit the Properties of it by right clicking on the created shortcut and setting the "Start In" to the absolute path (e.g. "C:/Users/john/Documents/symbol_formatter")

## Usage
==TODO update for package call==
In the format `python inputFrom.md -o <outTo.md> -s <symbolJSON> [--no-toc]`.
The extension `--help` can also be used

Install package (from local folder i.e. git pull/clone)
```shell
python -m pip install .
```

```shell
python .cli.py inputFrom.md -o outputTo.md -s mySymbols.json --no-toc
#Namespace(input='inputFrom.md', output='outputTo.md', symbols='mySymbols.json', no_toc=True)
```


## Description
This program uses python to convert a custom format for representing commonly used symbols in Computer Science and Mathematics into the relevant text symbols or processed format.
- It sterilises the provided text, such as replacing symbols that represent quotation marks into actual quotation marks
- It also structures notes to include a customised table of contents at the top
[The website](https://symbol-formatter.netlify.app/) contains a filterable list of all the symbols and is up-to-date with the [symbol table](https://symbol-formatter.netlify.app/website/symbol-table).

## Purpose
This program was designed to allow me to take notes in univeristy lectures much more efficiently, not having to worry about finding specific symbols, then copying and pasting them whenever needed. Creating this allowed my notes to be much more streamlined and I could quickly write out a representation for a symbol during a lecture - allowing me to pay better attention -, and afterwards, run a simple shortcut to execute the python script on a desired file path to format it as intended.
With regular use, common representations are easily remembered and I designed them to be as intuitive as possible, some 'symbols' having multiple different representations for ease of use. However, if any are forgotten having a table (like the one below) proves useful, I had one in my Obsidian vault (where I took notes) for quick reference.

## Symbol Table
[Symbol Table](https://symbol-formatter.netlify.app/website/symbol-table)

## Example
**Before**
> ![Before](./website/images/example_before.png)

**After**
> ![After](./website/images/example_after.png)
