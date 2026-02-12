import argparse


def get_cli_args():
    parser = argparse.ArgumentParser(
        description="Codebase Analyzer Tool"
    )

    parser.add_argument(
        "path",
        help="Path of the project to analyze"
    )

    parser.add_argument(
        "--report",
        help="Generate analysis report to a text file",
        default=None
    )
    parser.add_argument(
    "--html",
    type=str,
    help="Generate HTML report at specified path"
    )
    parser.add_argument(
    "--graph",
    type=str,
    help="Generate dependency graph (.dot file)"
    )   
    parser.add_argument(
    "--verbose",
    action="store_true",
    help="Show detailed output"
    )




    return parser.parse_args()
