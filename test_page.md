This is a page designed to test that the symbol formatter correctly creates and renames links. The page 'Haskell' is a pre-existing page.

The expected (valid) table of contents should be:

```

- [[#A heading]]
	- [[#A subheading]]
	- [[# A subheading and more]]
	- [[# A subheading smth and more| smth and more]]
	- [[#Haskell and more]]
	- [[#Haskell hskl and more and more|hskl and more and more]]
	- [[#Haskell Running and more]]
	- [[#Haskell Running rning and more|rning and more]]

```

# A heading

## A subheading

<hr>

## [[#A subheading]] and more
Link to a subheading

## [[#A subheading|smth]] and more
Renamed link to a subheading

<hr>

## [[Haskell]] and more
Link to a different note

## [[Haskell|hskl and more]] and more
Link to a different note renamed

## [[Haskell#Running]] and more
Link to a different subheading

## [[Haskell#Running|rning]] and more
Link to a different subheading renamed

<hr>

Here are the various tables of contents produced by the code

<u>Base code</u>
```
- [[#A heading]]
    - [[#A subheading]]
    - [[# A subheading and more]]
    - [[# A subheading smth and more| smth and more]]
    - [[#[[Haskell]] and more]]
    - [[#Haskell hskl and more]] and mor|hskl and more]] and mo]]
    - [[#[[Haskell#Running]] and more]]
    - [[#Haskell Running rning]] and mor|rning]] and mo]]
```
The first four links work, though the third has an erroneous space before the display name " smth and more". There are also spaces before the "A" in the third and fourth links.

The fifth link would work if the internal square brackets were removed (`[[#Haskell and more]]`).

The sixth link would work if the internal square brackets were removed, and the letters were not cut off (i.e. "mor", and "mo").

The seventh link would work if the internal square brackets were removed, along with the internal hashtag (`Haskell#Running`) being replaced by a space.

The eight link would work if the internal square brackets were removed, and the letters were not cut off (as was with the sixth link)

Problems:
- Square brackets present in headings need to be removed. It should be very easy to fix
- The erroneous spaces are abnormal but may arise from code not accounting for headings including links to internal headings. It seems to *not* be an issue with the first two links, but is with the third and fourth (which have extra text accompanying the link in the heading). This could be a simple fix or may take longer to debug
- The letters being cut off in the sixth and eigth link may be caused from using indexing on strings to cut out substrings, and the link format makes the code cut out letters instead of, for example, square brackets. This may take some time to diagnose the specific issue
- The erroneous hashtag in the seventh link could easily be fixed