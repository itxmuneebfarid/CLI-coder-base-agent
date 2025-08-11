import os
import shutil
from langchain.tools import tool

@tool
def delete_file(keyword: str, search_path: str = ".") -> str:
    """
    Deletes the first file or folder found that contains the given keyword in its name.
    :param keyword: Keyword to search in file/folder name.
    :param search_path: Directory path to search in (default: current folder).
    """
    keyword_lower = keyword.lower()


    for root, dirs, files in os.walk(search_path):
    
        for filename in files:
            if keyword_lower in filename.lower():
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                return f"Success: File '{filename}' has been deleted."

        for foldername in dirs:
            if keyword_lower in foldername.lower():
                folder_path = os.path.join(root, foldername)
                shutil.rmtree(folder_path)
                return f"Success: Folder '{foldername}' and all its contents have been deleted."

    return f"No file or folder containing '{keyword}' was found."
