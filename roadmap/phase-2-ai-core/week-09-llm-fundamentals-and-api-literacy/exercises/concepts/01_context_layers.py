"""
Week 09 Exercise
----------------
This script makes the context-construction problem visible by separating
instructions, user content, retrieved context, and tool results.
"""


def build_context_layers():
    return {
        "instructions": "You are a careful study assistant. Prefer concise, actionable answers.",
        "user_task": "Summarize the main idea of retrieval-augmented generation in plain English.",
        "retrieved_context": [
            "RAG combines retrieval of external knowledge with generation.",
            "Good grounding reduces hallucination risk.",
        ],
        "tool_results": [],
    }


def main():
    context = build_context_layers()

    print("Context layers in a model-backed system:")
    for layer_name, value in context.items():
        print(f"\n{layer_name.upper()}:")
        print(value)


if __name__ == "__main__":
    main()
