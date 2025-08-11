import os
from langchain.tools import tool
def generate_tree_format(root_dir=".") -> str:
    """
    Generate a tree-style folder structure starting from root_dir.
    """
    root_path = os.path.abspath(root_dir)
    tree_output = f"{root_path}/\n"

    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, "").count(os.sep)
        indent = "│   " * level
        folder = os.path.basename(root)
        if root != root_dir:
            tree_output += f"{indent}├── {folder}/\n"

        sub_indent = "│   " * (level + 1)
        for file in files:
            tree_output += f"{sub_indent}└── {file}\n"

    return tree_output

@tool
def create_folder_structure() -> str:
    """
   Creates and returns the current folder structure in tree-style format.
    """
    return f" FOLDER STRUCTURE in Tree Format /n:{generate_tree_format()}"

