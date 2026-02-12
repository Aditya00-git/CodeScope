# 🚀 CodeScope

> A fast, professional CLI tool to **analyze, inspect, and visualize any codebase**.

CodeScope gives you **code metrics, project insights, dependency graphs, and an interactive HTML dashboard** — all with a single command.

Built with **pure Python (standard library only)**.
No heavy dependencies. No setup pain.

---

#  Features

##  Core Analysis

* Recursive directory scanning
* File & folder counts
* Line of code stats (total / empty / code)
* Language detection
* Largest files
* Empty & small file detection

##  Smart Insights

* Complexity metrics

  * Avg lines per file
  * Largest file
  * Deepest nesting
  * Largest directory
* Duplicate file detection (hash-based)
* Dead/unused Python file detection

##  Visual Reports

* Clean terminal summary
* Interactive HTML dashboard
* Language pie chart
* Dark theme UI
* Auto-opens browser
* Dependency graph visualization
* Colored architecture diagram

##  CLI Experience

* Installable via pip
* Single command usage
* Minimal, readable output
* `--verbose` detailed mode
* Zero external Python dependencies

---

#  Installation

## Option 1 — Local install (current)

```bash
git clone https://github.com/<your-username>/codescope.git
cd codescope
pip install -e .
```

---

## Option 2 — PyPI (future)

After publishing:

```bash
pip install codescope
```

---

#  Usage

## Run analysis

```bash
codescope .
```

## What happens automatically

* Terminal summary
* HTML dashboard opens in browser
* Dependency graph generated

## Verbose mode

```bash
codescope . --verbose
```

Shows:

* duplicate file groups
* dead files
* detailed breakdown

---

#  Generated Outputs

After running:

```
codescope .
```

You get:

```
analysis_report.html     → interactive dashboard
dependency_graph.png    → dependency graph
```

---

#  Example Terminal Output

```
════════ CodeScope ════════

Files: 142 | Folders: 21 | Lines: 12430
Languages: Python(70%) JS(20%)
Complexity: Avg 132 lines/file | Depth 6
Duplicates: 2 group(s)
Dead files: 3
```

Clean. Short. Actionable.

---

#  HTML Dashboard Includes

* Summary cards
* Language pie chart
* Complexity metrics
* Largest files table
* Duplicate file groups
* Dead files list
* Dark theme UI

---

# 🔗 Dependency Graph

Visualizes Python import relationships.

Requires **Graphviz**.

---

# 🧱 Project Structure

```
codebase_analyzer/
│
├── analyzer/
├── cli/
├── reports/
├── main.py
├── pyproject.toml
```

---

# 🧠 Tech Stack

* Python 3
* Standard library only
* argparse
* ast
* hashlib
* webbrowser
* graphviz (optional)

---

# 👤 Author

Aditya Seswani

