"""
Week 01 - Strings: Common Operations

What this file teaches:
- cleaning text with strip()
- changing text case
- splitting and joining strings
- searching and replacing inside text
- indexing and slicing
- writing a small string-processing function
"""


def show_cleanup_and_case_changes():
    """Trim whitespace and show common case-conversion methods."""
    full_name = "  asha patel  "
    clean_name = full_name.strip()

    print("Clean name:", clean_name)
    print("Upper:", clean_name.upper())
    print("Lower:", clean_name.lower())
    print("Title:", clean_name.title())


def show_split_and_join():
    """Turn one string into a list of words, then combine them again."""
    clean_name = "asha patel"
    words = clean_name.split()
    print("Words:", words)

    joined_name = "-".join(words)
    print("Joined with hyphen:", joined_name)


def show_search_and_replace():
    """Look for text patterns and replace part of a sentence."""
    sentence = "Python is readable and powerful."

    print("Contains 'readable':", "readable" in sentence)
    print("Starts with 'Python':", sentence.startswith("Python"))
    print("Ends with '.':", sentence.endswith("."))

    updated_sentence = sentence.replace("powerful", "friendly")
    print("Updated sentence:", updated_sentence)


def show_indexing_and_slicing():
    """Read specific characters or sections from a string."""
    word = "developer"

    print("First character:", word[0])
    print("Last character:", word[-1])
    print("First four characters:", word[:4])
    print("Last four characters:", word[-4:])


def show_f_string_example():
    """Format values inside a readable sentence."""
    language = "Python"
    version = 3.14
    print(f"I am learning {language} {version}.")


def count_vowels(text):
    """Return how many vowels exist in a piece of text."""
    vowels = "aeiou"
    total = 0

    # Convert to lowercase so one check works for both uppercase and lowercase.
    for character in text.lower():
        if character in vowels:
            total += 1

    return total


def show_small_function_example():
    """Demonstrate a simple text-processing function."""
    sample_text = "Programming with Python"
    print("Vowel count:", count_vowels(sample_text))


def main():
    """Run all string examples in a logical order."""
    show_cleanup_and_case_changes()
    print("-" * 40)
    show_split_and_join()
    print("-" * 40)
    show_search_and_replace()
    print("-" * 40)
    show_indexing_and_slicing()
    print("-" * 40)
    show_f_string_example()
    show_small_function_example()


if __name__ == "__main__":
    main()
