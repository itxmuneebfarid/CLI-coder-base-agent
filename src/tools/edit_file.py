import os
from langchain.tools import tool

@tool
def edit_file_content(file_path: str, new_content: str, mode: str = "replace") -> str:
    """
    Edits the content of a file.
    """
    if not os.path.exists(file_path):
        return f"Error: File not found at {file_path}"
    
    try:
        if mode == "replace":
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
        elif mode == "append":
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(new_content)
        else:
            return "Error: Mode must be either 'replace' or 'append'"
        return f"Success: File at '{file_path}' has been updated with mode '{mode}'."
    except Exception as e:
        return f"Error editing file: {str(e)}"