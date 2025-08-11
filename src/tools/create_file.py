import os
from langchain.tools import tool
@tool
def create_file(path: str) -> str:
    """
    Creates a new file .
    Returns a  message File created successfully .
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'x') as f:
      pass
    return f"File created at: {os.path.abspath(path)}"