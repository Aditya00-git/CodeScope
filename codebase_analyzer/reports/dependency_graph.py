import os
import ast
import subprocess
def extract_imports(file_path):
    """Extract imported modules from a Python file using AST."""
    imports = set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split(".")[0])
    except Exception:
        pass  
    return imports
def write_dependency_graph(output_path, files):
    dot_path = output_path.replace(".png", ".dot")
    py_files = [f for f in files if f.endswith(".py")]
    edges = []
    for file in py_files:
        module_name = os.path.splitext(os.path.basename(file))[0]
        imports = extract_imports(file)
        for imp in imports:
            edges.append((module_name, imp))
    with open(dot_path, "w", encoding="utf-8") as f:
        f.write("digraph CodebaseDependencies {\n")
        f.write("rankdir=LR;\n")
        f.write('node [shape=box, style="filled,rounded", fontname="Arial"];\n\n')

        project_modules = {
            os.path.splitext(os.path.basename(f))[0]
            for f in py_files
        }

        external_modules = set(dst for _, dst in edges if dst not in project_modules)

        # ✅ FIRST: define project nodes (blue)
        for module in project_modules:
            f.write(f'"{module}" [fillcolor="#4F81BD", fontcolor="white"];\n')

        # ✅ SECOND: define external nodes (gray)
        for module in external_modules:
            f.write(f'"{module}" [fillcolor="#D3D3D3", fontcolor="black"];\n')

        f.write("\n")

        # ✅ LAST: draw edges
        for src, dst in edges:
            f.write(f'"{src}" -> "{dst}";\n')

        f.write("}\n")

    subprocess.run(["dot", "-Tpng", dot_path, "-o", output_path], check=False)