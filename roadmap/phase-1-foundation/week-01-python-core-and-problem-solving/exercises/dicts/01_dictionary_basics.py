"""
Week 01 - Dictionaries: Key-Value Data

What this file teaches:
- how dictionaries store named pieces of information
- how to read and update values
- how to loop through keys and values
- how dictionaries help with counting and merging data
"""


def show_basic_dictionary_usage():
    """Create a dictionary and perform common read/update operations."""
    student = {
        "name": "Asha",
        "age": 24,
        "city": "Ahmedabad",
        "is_active": True,
    }

    print("Student:", student)
    print("Student name:", student["name"])

    # get(...) is safer than direct indexing when a key may not exist.
    print("Phone number:", student.get("phone"))

    student["age"] = 25
    student["email"] = "asha@example.com"
    print("Updated student:", student)

    removed_value = student.pop("city")
    print("Removed city:", removed_value)
    print("Student after pop:", student)

    return student


def show_dictionary_loop(student):
    """Print each key-value pair in a readable format."""
    for key, value in student.items():
        print(f"{key} -> {value}")


def word_frequency(sentence):
    """Return a dictionary showing how many times each word appears."""
    frequencies = {}

    for word in sentence.lower().split():
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def merge_scores(first_scores, second_scores):
    """Merge two score dictionaries and add values for repeated names."""
    merged = first_scores.copy()

    for name, score in second_scores.items():
        # If the name already exists, add to the old score.
        if name in merged:
            merged[name] += score
        else:
            merged[name] = score

    return merged


def show_problem_solving_examples():
    """Use dictionaries for counting and combining records."""
    sample_sentence = "python code code practice python"
    print("Word frequency:", word_frequency(sample_sentence))

    quiz_scores = {"Asha": 8, "Ravi": 6}
    assignment_scores = {"Asha": 7, "Neha": 9}
    print("Merged scores:", merge_scores(quiz_scores, assignment_scores))


def main():
    """Run all dictionary examples."""
    student = show_basic_dictionary_usage()
    print("-" * 40)
    show_dictionary_loop(student)
    print("-" * 40)
    show_problem_solving_examples()


if __name__ == "__main__":
    main()
