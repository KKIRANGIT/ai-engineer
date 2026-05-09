"""
Week 01 - Strings: Common Operations
"""

full_name = "  asha patel  "
clean_name = full_name.strip()
print("Clean name:", clean_name)

print("Upper:", clean_name.upper())
print("Lower:", clean_name.lower())
print("Title:", clean_name.title())

words = clean_name.split()
print("Words:", words)

joined_name = "-".join(words)
print("Joined with hyphen:", joined_name)

sentence = "Python is readable and powerful."
print("Contains 'readable':", "readable" in sentence)
print("Starts with 'Python':", sentence.startswith("Python"))
print("Ends with '.':", sentence.endswith("."))

updated_sentence = sentence.replace("powerful", "friendly")
print(updated_sentence)

word = "developer"
print("First character:", word[0])
print("Last character:", word[-1])
print("First four characters:", word[:4])
print("Last four characters:", word[-4:])

language = "Python"
version = 3.14
print(f"I am learning {language} {version}.")


def count_vowels(text):
    """Return how many vowels exist in a piece of text."""
    vowels = "aeiou"
    total = 0

    for character in text.lower():
        if character in vowels:
            total += 1

    return total


sample_text = "Programming with Python"
print("Vowel count:", count_vowels(sample_text))
