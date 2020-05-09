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

> `ROAD$` with the multi-line flag enabled matches "ROAD" at the end of the line. Check out the [cheatsheet](https://www.rexegg.com/regex-quickstart.html) to match more complex addresses with word boundaries `\b` or any whitespace `\s`.

## Roman Numerals

Match the thousands place of
a Roman numeral:

```
M
MM
MMM
```
>`M{0,3}` will match 0-3 occurrences of M.

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

> `CM|CD|D?C{0,3}` will match the above. `C{0,3}` takes care of the cases with only C. There is optionally a `D` in front giving `D?C{0,3}`. The last two cases are covered with the `|` operator, meaning "OR".

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
> `XC|XL|L?X{0,3}` will match the above.

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
> `IX|IV|V?I{0,3}` will match the above.

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

> `^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$` puts it all together.

## Phone Numbers

Match any phone numbers in this format:

```
800-555-1212
123-456-6789
310-825-4321
```
> `\d{3}-\d{3}-\d{4}` matches this format.

Match the previous phone numbers and phone numbers without dash separators:

```
800-555-1212
123-456-6789
310-825-4321
8005551212
1234566789
3108254321
```
> `\d{3}-?\d{3}-?\d{4}` makes the dash optional.

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

> `(\(\d{3}\)|\d{3})-?\d{3}-?\d{4}` supports the parentheses format for the first three numbers as well.

These exercises are based off https://diveintopython3.net/regular-expressions.html. Read the full article for more complex and detailed information on Python regular expressions.