import argparse
from lib.search_command import search


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            results = search(args.query)
            if not results:
                print("No movies found.")
            else:
                for i, r in enumerate(results, start=1):
                    print(f"{i}. {r['title']}")
        case _:
            parser.exit(2, parser.format_help())

if __name__ == "__main__":
    main()
