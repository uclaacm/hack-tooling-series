# Regular Expression Solutions

These are the solutions to the exercises found in `Exercises.md`.

## Street Addresses

`ROAD$` matches "ROAD" at the end of the line. Check out the [cheatsheet](https://www.rexegg.com/regex-quickstart.html) to match more complex addresses with word boundaries `\b` or any whitespace `\s`.

## Phone Numbers

`^\d{3}-\d{3}-\d{4}$` matches the dash format.

`^\d{3}-?\d{3}-?\d{4}$` makes the dash optional.

`^(\(\d{3}\) ?|\d{3})-?\d{3}-?\d{4}$` supports the parentheses format for the first three numbers as well by using the `|` operator to allow for parentheses and an optional space.

## Roman Numerals

`^M{0,3}$` will match 0-3 occurrences of M.

`^CM|CD|D?C{0,3}$` will match the hundreds place. `C{0,3}` takes care of the cases with only C. There is optionally a `D` in front giving `D?C{0,3}`. The last two cases are covered with the `|` operator, meaning "OR".

`^XC|XL|L?X{0,3}$` will match the tens place for the same reason.

`^IX|IV|V?I{0,3}$` will match the ones place for the same reason.

`^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$` puts it all together.

These exercises are based off https://diveintopython3.net/regular-expressions.html. Read the full article for more complex and detailed information on Python regular expressions.