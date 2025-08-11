import argparse
import sys
import os
from agent import load_agent

try:
    from colorama import init, Fore, Style, Back
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    class Fore:
        CYAN = YELLOW = GREEN = RED = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""
    class Back:
        BLACK = ""

def colored_print(text, color="", style=""):
    if COLORS_AVAILABLE:
        print(f"{style}{color}{text}{Style.RESET_ALL}")
    else:
        print(text)

def show_welcome():
    if COLORS_AVAILABLE:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    welcome_text = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ✦ Welcome to Coder Agent                                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}{Style.BRIGHT}
 ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                         
 █████╗  ██████╗ ███████╗███╗   ██╗████████╗
██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝
███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║   
██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   
██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   
{Style.RESET_ALL}

{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}
"""
    print(welcome_text)
    input()
    os.system('cls' if os.name == 'nt' else 'clear')

def interactive_mode():
    show_welcome()
    agent = load_agent()
    
    colored_print("🤖 Coder Agent CLI", Fore.CYAN, Style.BRIGHT)
    colored_print("Type 'quit', 'exit', or 'q' to end session\n", Fore.WHITE)
    
    while True:
        try:
            if COLORS_AVAILABLE:
                question = input(f"{Fore.GREEN}❯ {Style.RESET_ALL}")
            else:
                question = input("❯ ")
                
            if question.lower() in ["quit", "exit", "q"]:
                colored_print("\n👋 Goodbye!", Fore.YELLOW, Style.BRIGHT)
                break
            if question.strip() == "":
                continue
                
            res = agent.invoke({"messages": [{"role": "user", "content": question}]})
            print(f"\n{res['messages'][-1].content}\n")
            
        except KeyboardInterrupt:
            colored_print("\n\n👋 Goodbye!", Fore.YELLOW, Style.BRIGHT)
            break
        except EOFError:
            colored_print("\n👋 Goodbye!", Fore.YELLOW, Style.BRIGHT)
            break

def single_query_mode(query):
    agent = load_agent()
    res = agent.invoke({"messages": [{"role": "user", "content": query}]})
    print(res["messages"][-1].content)

def file_mode(file_path):
    if not os.path.exists(file_path):
        colored_print(f"❌ Error: File '{file_path}' not found", Fore.RED, Style.BRIGHT)
        sys.exit(1)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    if content:
        single_query_mode(content)

def main():
    parser = argparse.ArgumentParser(
        description='AI-Powered Coder Agent CLI',
        prog='coder-agent'
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        'query', 
        nargs='?', 
        help='Single query to process'
    )
    group.add_argument(
        '-f', '--file',
        help='Read query from file'
    )
    group.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Start interactive mode'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Coder Agent v1.0.0'
    )

    args = parser.parse_args()

    if args.file:
        file_mode(args.file)
    elif args.query:
        single_query_mode(args.query)
    elif args.interactive or len(sys.argv) == 1:
        interactive_mode()

if __name__ == "__main__":
    main()