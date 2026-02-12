from codebase_analyzer.analyzer.scanner import scan_project
from codebase_analyzer.analyzer.file_stats import get_file_and_folder_count, get_largest_files
from codebase_analyzer.analyzer.line_counter import count_lines
from codebase_analyzer.analyzer.language_detector import detect_languages
from codebase_analyzer.analyzer.empty_finder import find_empty_and_small_files
from codebase_analyzer.reports.reports import write_report
from codebase_analyzer.analyzer.pretty_output import print_summary
from codebase_analyzer.analyzer.complexity import compute_complexity
from codebase_analyzer.analyzer.duplicates import find_duplicates
def run_analysis(project_path, report_path=None, html_path=None,graph_path=None,verbose=False):
    files, folders = scan_project(project_path)
    total_files, total_folders = get_file_and_folder_count(files, folders)
    total_lines, empty_lines, code_lines = count_lines(files)
    languages = detect_languages(files)
    empty_files, small_files = find_empty_and_small_files(files)
    largest_files = get_largest_files(files)
    complexity = compute_complexity(files, folders)
    duplicates = find_duplicates(files)
    data = {
        "total_files": total_files,
        "total_folders": total_folders,
        "total_lines": total_lines,
        "empty_lines": empty_lines,
        "code_lines": code_lines,
        "languages": languages,
        "largest_files": largest_files,
        "empty_files": empty_files,
        "small_files": small_files,
        "duplicates": duplicates,
        "complexity": complexity,
        "duplicates": duplicates
    }
    print_summary(data,verbose)
    data["complexity"] = compute_complexity(files, folders)



    if report_path:
        write_report(report_path, data)
        print("\nText report generated at:", report_path)

    from codebase_analyzer.reports.html_report import write_html_report

    html_path = html_path or "analysis_report.html"
    write_html_report(html_path, data)
    print("\nHTML report generated at:", html_path)

    from codebase_analyzer.reports.dependency_graph import write_dependency_graph

    graph_path = graph_path or "dependency_graph.png"
    write_dependency_graph(graph_path, files)
    print("\nDependency graph generated at:", graph_path)

