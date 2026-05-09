"""
Week 01 - Dictionaries: Key-Value Data
"""

student = {
    "name": "Asha",
    "age": 24,
    "city": "Ahmedabad",
    "is_active": True,
}

print("Student:", student)
print("Student name:", student["name"])
print("Phone number:", student.get("phone"))

student["age"] = 25
student["email"] = "asha@example.com"
print("Updated student:", student)

removed_value = student.pop("city")
print("Removed city:", removed_value)
print("Student after pop:", student)

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


sample_sentence = "python code code practice python"
print("Word frequency:", word_frequency(sample_sentence))


def merge_scores(first_scores, second_scores):
    """Merge two score dictionaries and add scores when a name appears in both."""
    merged = first_scores.copy()

    for name, score in second_scores.items():
        if name in merged:
            merged[name] += score
        else:
            merged[name] = score

    return merged


quiz_scores = {"Asha": 8, "Ravi": 6}
assignment_scores = {"Asha": 7, "Neha": 9}
print("Merged scores:", merge_scores(quiz_scores, assignment_scores))
