# Symbol Formatter
## Contents
- [Symbol Formatter](#symbol-formatter)
  - [Contents](#contents)
  - [Installation](#installation)
    - [Shortcut Setup](#shortcut-setup)
  - [Usage](#usage)
  - [Description](#description)
  - [Purpose](#purpose)
  - [Symbol Table](#symbol-table)
  - [Example](#example)

## Installation
Install package directly from github
```shell
pip install pip@githttps://github.com/johnm-portfolio/formatter-deployment
```

OR

Clone repo then install package locally (from local folder i.e. git pull/clone)
```shell
# Clone the repo
git clone https://github.com/johnm-portfolio/formatter-deployment.git note_formatter
# Install the project
cd .\note_formatter\
pip install .
```

### Shortcut Setup
You can create a Windows shortcut with the location set as
```lnk
powershell.exe -Command "note-formatter --inplace" 
 ```
- Or replace `note-formatter --inplace` with a different package command

This means you can quickly and easily run the CLI with a single click.

## Usage
With the package installed, simply run
```shell
note-formatter
```
If the package is not installed but the project repo is cloned
```shell
# From project root (not package root)
python -m note_formatter.cli
```

Arguments are detailed in `note-formatter --help`, but the quickest format is:
```shell
# Format the given file and output to it as well
note-formatter "inputFrom.md" --inplace
```
- It is good practice to wrap path arguments in quotation marks (`"`) because, for example, the `&` character causes issues if the path is not in quotes

The shell script `/start_cli.ps1` runs `note_formatter.cli` with no args, you can create a shortcut to run this script and add it to your hotbar

To uninstall
```shell
pip uninstall note-formatter
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
> ![Before](website/images/example_before.png)

**After**
> ![After](website/images/example_after.png)
