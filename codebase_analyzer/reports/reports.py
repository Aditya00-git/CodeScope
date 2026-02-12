def write_report(report_path, data):
    with open(report_path, "w", encoding="utf-8") as file:
        file.write("CODEBASE ANALYSIS REPORT\n")
        file.write("=" * 30 + "\n\n")

        file.write(f"Total files: {data['total_files']}\n")
        file.write(f"Total folders: {data['total_folders']}\n\n")

        file.write("Line Statistics:\n")
        file.write(f"  Total lines: {data['total_lines']}\n")
        file.write(f"  Empty lines: {data['empty_lines']}\n")
        file.write(f"  Code lines: {data['code_lines']}\n\n")

        file.write("Languages Used:\n")
        for lang, count in data["languages"].items():
            file.write(f"  {lang}: {count}\n")

        file.write("\nLargest Files:\n")
        for path, size in data["largest_files"]:
            file.write(f"  {path} - {size} bytes\n")

        file.write("\nEmpty Files:\n")
        for path in data["empty_files"]:
            file.write(f"  {path}\n")

        file.write("\nSmall Files:\n")
        for path, lines in data["small_files"]:
            file.write(f"  {path} ({lines} lines)\n")