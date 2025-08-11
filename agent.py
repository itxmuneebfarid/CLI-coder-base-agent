from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from src.tools.create_file import create_file
from src.tools.create_folder import create_folder
from src.tools.create_structure import create_folder_structure
from src.tools.delete import delete_file
from src.tools.edit_file import edit_file_content
from utils.prompt import prompt

load_dotenv()
def load_agent():
    """
    Initialize and return the configured file/folder management agent.

    Steps:
    1. Load environment variables.
    2. Prepare the toolset for file operations.
    3. Initialize the LLM model.
    4. Create and return the ReAct agent.
    """



    tools = [
        create_folder_structure,
        create_folder,
        create_file,
        edit_file_content,
        delete_file
    ]

    llm = ChatOpenAI(
        model="gpt-4o-mini",
    )

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=prompt
    )

    return agent


if __name__ == "__main__":
    agent = load_agent()
    question = input("Enter your question: ")

    res = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )

    print(res["messages"][-1].content)
