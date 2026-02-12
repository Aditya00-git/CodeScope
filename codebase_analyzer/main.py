from codebase_analyzer.cli.args import get_cli_args
from codebase_analyzer.cli.commands import run_analysis

def main():
    args = get_cli_args()
    run_analysis(args.path, args.report,args.html,args.graph,args.verbose)


if __name__ == "__main__":
    main()