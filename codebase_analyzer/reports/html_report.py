import json
import webbrowser
import os
def write_html_report(path, data):
    languages = data["languages"]
    labels = list(languages.keys())
    values = list(languages.values())
    complexity = data.get("complexity", {})
    duplicates = data.get("duplicates", [])
    dead_files = data.get("dead_files", [])
    largest_files = data.get("largest_files", [])
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Codebase Analysis Report</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
    body {{
        font-family: Arial, sans-serif;
        margin: 30px;
        background: #0f172a;
        color: #e2e8f0;
    }}
    h1 {{
        text-align: center;
        color: #38bdf8;
    }}
    h2 {{
        margin-bottom: 10px;
        color: #60a5fa;
    }}
    .grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
        margin-bottom: 25px;
    }}
    .card {{
        background: #1e293b;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        transition: transform 0.2s ease;
    }}
    .card:hover {{
        transform: translateY(-4px);
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }}
    th {{
        text-align: left;
        padding: 10px;
        font-size: 14px;
        color: #93c5fd;
        border-bottom: 1px solid #334155;
    }}
    td {{
        padding: 8px;
        border-bottom: 1px solid #334155;
        font-size: 13px;
        color: #cbd5e1;
    }}
    tr:hover {{
        background: #273449;
    }}
    ul {{
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 6px;
    }}
    .chart-container {{
        width: 420px;
        height: 420px;
        margin: auto;
    }}
</style>
</head>
<body>
<h1>Codebase Analysis Dashboard</h1>
<!-- SUMMARY CARDS -->
<div class="grid">
    <div class="card"><b>Files</b><br>{data['total_files']}</div>
    <div class="card"><b>Folders</b><br>{data['total_folders']}</div>
    <div class="card"><b>Total Lines</b><br>{data['total_lines']}</div>
    <div class="card"><b>Code Lines</b><br>{data['code_lines']}</div>
</div>
<!-- LANGUAGE CHART -->
<div class="card">
    <h2>Language Distribution</h2>
    <div class="chart-container">
        <canvas id="langChart"></canvas>
    </div>
</div>
<!-- COMPLEXITY -->
<div class="card">
<h2>Complexity Metrics</h2>
<ul>
<li>Average lines per file: {complexity.get('avg_lines_per_file',0)}</li>
<li>Largest file: {complexity.get('max_file_lines',0)} lines</li>
<li>Max depth: {complexity.get('max_depth',0)}</li>
<li>Largest directory files: {complexity.get('largest_directory_files',0)}</li>
</ul>
</div>
<!-- LARGEST FILES -->
<div class="card">
<h2>Largest Files</h2>
<table>
<tr><th>File</th><th>Size</th></tr>
{''.join(f"<tr><td>{f}</td><td>{s}</td></tr>" for f,s in largest_files)}
</table>
</div>
<!-- DUPLICATES -->
<div class="card">
<h2>Duplicate Files ({len(duplicates)} groups)</h2>
<table>
<tr><th>Group</th><th>Files</th></tr>
{''.join(f"<tr><td>{i+1}</td><td>{'<br>'.join(g)}</td></tr>" for i,g in enumerate(duplicates))}
</table>
</div>
<!-- DEAD FILES -->
<div class="card">
<h2>Dead Files ({len(dead_files)})</h2>
<table>
{''.join(f"<tr><td>{f}</td></tr>" for f in dead_files)}
</table>
</div>
<script>
const ctx = document.getElementById('langChart');
new Chart(ctx, {{
    type: 'pie',
    data: {{
        labels: {json.dumps(labels)},
        datasets: [{{
            data: {json.dumps(values)},
            backgroundColor: [
                "#38bdf8",
                "#6366f1",
                "#f59e0b",
                "#ef4444",
                "#10b981",
                "#a855f7",
                "#f472b6"
            ],
            borderColor: "#0f172a"
        }}]
    }},
    options: {{
        maintainAspectRatio: false,
        plugins: {{
            legend: {{
                labels: {{
                    color: "#e2e8f0"
                }}
            }}
        }}
    }}
}});
</script>
</body>
</html>
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_content)
    webbrowser.open("file://" + os.path.abspath(path))