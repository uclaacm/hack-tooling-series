# Regular Expression Exercises

Type the text boxes into https://regexr.com/ and make sure the multi-line flag is enabled.

[Regular Expression Cheat Sheet](https://www.rexegg.com/regex-quickstart.html)

## Street Addresses

Match
any instance of "ROAD" that can be replaced with "RD":

```
100 NORTH MAIN ROAD
100 NORTH BROAD ROAD
```

## Roman Numerals

Match the thousands place of
a Roman numeral:

```
M
MM
MMM
```

Match the hundreds place of a Roman numeral:

```
C
CC
CCC
CD
D
DC
DCC
DCCC
CM
```

Match the tens place of a Roman numeral:

```
X
XX
XXX
XL
L
LX
LXX
LXXX
XC
```

Match the ones place of a Roman numeral:

```
I
II
III
IV
V
VI
VII
VIII
IX
```

Match any valid Roman numeral:

```
Valid:
MCM
MD
MMMCCC
MCMC
MCMXL
MCMLX
MCMLXXX
MDLV
MMDCLXVI
MMMDCCCLXXXVIII
I

Invalid:
MMMM
MCMLXXXX
```

## Phone Numbers

Match any phone numbers in this format:

```
800-555-1212
123-456-6789
310-825-4321
```

Match the previous phone numbers and phone numbers without dash separators:

```
800-555-1212
123-456-6789
310-825-4321
8005551212
1234566789
3108254321
```

Match the previous numbers and phone numbers with the area code in parentheses:

```
800-555-1212
123-456-6789
310-825-4321
8005551212
1234566789
3108254321
(800)555-1212
(123)456-6789
(310)825-4321
```

If you want to match any special character, you will need to escape it with a backslash.

- `\(` matches `(`
- `\.` matches `.`
- `\\` matches `\`

These exercises are based off https://diveintopython3.net/regular-expressions.html. Read the full article for more complex and detailed information on Python regular expressions.