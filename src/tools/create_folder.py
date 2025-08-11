from langchain.tools import tool
import os
@tool
def create_folder(path: str) -> str:
    """
    Creates a new folder .
    Returns a  message Folder created successfully .
    """
    os.makedirs(path, exist_ok=False)
    return f" Folder created at: {os.path.abspath(path)}"