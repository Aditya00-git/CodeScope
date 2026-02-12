def print_summary(data, verbose=False):
    total_lang = sum(data["languages"].values())

    top_langs = sorted(
        data["languages"].items(),
        key=lambda x: -x[1]
    )[:3]

    lang_str = " ".join(
        f"{k}({int(v/total_lang*100)}%)"
        for k, v in top_langs if total_lang
    )

    print("\n════════ Codebase Analyzer ════════\n")

    print(
        f"Files: {data['total_files']} | "
        f"Folders: {data['total_folders']} | "
        f"Lines: {data['total_lines']}"
    )

    print(f"Languages: {lang_str}")

    complexity = data.get("complexity", {})
    if complexity:
        print(
            f"Complexity: Avg {complexity['avg_lines_per_file']} lines/file | "
            f"Depth {complexity['max_depth']}"
        )

    duplicates = data.get("duplicates", [])
    print(f"Duplicates: {len(duplicates)} group(s)")

    dead = data.get("dead_files", [])
    print(f"Dead files: {len(dead)}")

    # 🔥 detailed only if verbose
    if verbose:
        print("\n--- Duplicate Details ---")
        for group in duplicates:
            for f in group:
                print(" ", f)
            print()

        print("\n--- Dead Files ---")
        for f in dead:
            print(" ", f)
