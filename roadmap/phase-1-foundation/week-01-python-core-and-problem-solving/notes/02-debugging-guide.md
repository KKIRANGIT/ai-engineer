# Beginner Debugging Guide

## Read Errors In This Order

1. Read the last line of the traceback first.
2. Identify the error type.
3. Find the file and line number.
4. Inspect the values used on that line.
5. Check whether your assumption was wrong.

## Common Week 01 Errors

### `SyntaxError`

Usually caused by:

- missing colon
- missing closing bracket
- broken indentation
- unmatched quotes

### `NameError`

Usually caused by:

- misspelled variable name
- using a variable before creating it

### `TypeError`

Usually caused by:

- mixing incompatible types
- calling a function with the wrong arguments

### `ValueError`

Usually caused by:

- converting invalid text to `int` or `float`
- manually raising an error for invalid user input

### `IndexError`

Usually caused by:

- reading a list item that does not exist

### `KeyError`

Usually caused by:

- reading a dictionary key that does not exist

## Good Debugging Habits

- print important values temporarily
- test one small part at a time
- do not change five things at once
- make one fix, then run again
