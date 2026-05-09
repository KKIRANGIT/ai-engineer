import argparse

from src.evaluation import evaluate_mode
from src.retrieval import SemanticSearchPlayground


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 11 Semantic Search Playground")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("inspect-chunks")

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("--mode", choices=["keyword", "semantic", "hybrid"], required=True)
    search_parser.add_argument("--query", required=True)
    search_parser.add_argument("--category")
    search_parser.add_argument("--audience")

    compare_parser = subparsers.add_parser("compare")
    compare_parser.add_argument("--query", required=True)

    evaluate_parser = subparsers.add_parser("evaluate")
    evaluate_parser.add_argument("--mode", choices=["keyword", "semantic", "hybrid"], required=True)

    return parser


def print_result(result) -> None:
    print(
        {
            "chunk_id": result.chunk.chunk_id,
            "document_id": result.chunk.document_id,
            "title": result.chunk.title,
            "category": result.chunk.category,
            "audience": result.chunk.audience,
            "score": round(result.score, 4),
            "keyword_score": round(result.keyword_score, 4),
            "semantic_score": round(result.semantic_score, 4),
            "text": result.chunk.text,
        }
    )


def main() -> None:
    parser = build_parser()
    arguments = parser.parse_args()
    playground = SemanticSearchPlayground()

    if arguments.command == "inspect-chunks":
        for chunk in playground.chunks:
            print(
                {
                    "chunk_id": chunk.chunk_id,
                    "document_id": chunk.document_id,
                    "title": chunk.title,
                    "text": chunk.text,
                }
            )
        return

    if arguments.command == "search":
        results = playground.search(
            query=arguments.query,
            mode=arguments.mode,
            category=arguments.category,
            audience=arguments.audience,
        )
        for result in results:
            print_result(result)
        return

    if arguments.command == "compare":
        for mode in ["keyword", "semantic", "hybrid"]:
            print(f"\n--- {mode.upper()} ---")
            results = playground.search(query=arguments.query, mode=mode)
            for result in results:
                print_result(result)
        return

    if arguments.command == "evaluate":
        outcomes = evaluate_mode(arguments.mode)
        passed = 0
        for outcome in outcomes:
            status = "PASS" if outcome["passed"] else "FAIL"
            print(f"{status} - {outcome['query']}")
            print(
                {
                    "expected_document_id": outcome["expected_document_id"],
                    "retrieved_document_id": outcome["retrieved_document_id"],
                }
            )
            if outcome["passed"]:
                passed += 1
        print(f"\nEvaluation summary: {passed}/{len(outcomes)} queries passed.")


if __name__ == "__main__":
    main()
