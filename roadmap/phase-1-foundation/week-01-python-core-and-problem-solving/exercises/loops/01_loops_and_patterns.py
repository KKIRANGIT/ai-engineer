"""
Week 01 - Loops: Repeating Work Cleanly
"""

for number in range(1, 6):
    print("Number:", number)

even_total = 0
for number in range(1, 11):
    if number % 2 == 0:
        even_total += number
print("Sum of even numbers from 1 to 10:", even_total)

count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Blast off!")

numbers = [4, 7, 9, 12, 15]
for number in numbers:
    if number % 2 == 0:
        print("First even number found:", number)
        break

for number in range(1, 6):
    if number == 3:
        continue
    print("Number except 3:", number)


def build_stars(rows):
    """Return a list of star-pattern lines."""
    pattern_lines = []

    for row in range(1, rows + 1):
        pattern_lines.append("*" * row)

    return pattern_lines


for line in build_stars(5):
    print(line)


def find_maximum(values):
    """Find the largest value manually without using max()."""
    largest = values[0]

    for value in values:
        if value > largest:
            largest = value

    return largest


sample_values = [14, 7, 22, 19, 5]
print("Largest value:", find_maximum(sample_values))
