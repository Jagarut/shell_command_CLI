import google.generativeai as genai
import pyperclip
import sys
from dotenv import load_dotenv
import os
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama for colored output

def check_dependencies():
    """
    Checks if required dependencies are installed.

    This function checks if the required packages (`google.generativeai` and `pyperclip`) are installed.
    If any are missing, it prints an error message and exits the program.
    """
    required_packages = ["google.generativeai", "pyperclip", "colorama"]
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"{Fore.RED}Error: Missing dependencies. Please install the following packages:")
        for package in missing_packages:
            print(f"  {package}")
        sys.exit(1)

from enum import Enum

class Shell(Enum):
    """Represents different shell types."""
    CMD = "Windows Command Prompt"
    POWERSHELL = "PowerShell"
    BASH = "bash"

def get_shell_selection() -> Shell:
    """
    Gets the user's selection for the shell type.

    This function presents a menu of shell types to the user and prompts them to choose one.
    It validates the user's input and returns the selected shell type.
    """
    shells = {
        str(i): shell 
        for i, shell in enumerate(Shell, 1)
    }
    
    print(f"\n{Fore.CYAN}Select shell type:")
    for num, shell in shells.items():
        print(f"{num}. {shell.value}")
        
    while True:
        selection = input(f"{Fore.YELLOW}Enter number (1-3): ").strip()
        if selection in shells:
            return shells[selection]
        print(f"{Fore.RED}Invalid selection. Please choose 1, 2, or 3.")

def get_command_description() -> str:
    """
    Gets a description of the command from the user.

    This function prompts the user to describe the command they want to generate.
    It returns the user's input as a string.
    """
    print(f"\n{Fore.CYAN}Describe the command you want to generate:")
    return input(f"{Fore.YELLOW}> ").strip()

def get_user_input():
    """
    Gets the user's input for the command description and shell type.

    This function calls `get_command_description` and `get_shell_selection` to get the user's input.
    It then prints the user's inputs for confirmation and returns them as a tuple.
    """
    query = get_command_description()
    shell_type = get_shell_selection()
    
    print(f"\n{Fore.CYAN}Your inputs:")
    print(f"Command description: {query}")
    print(f"Selected shell: {shell_type.value}\n")
    
    return query, shell_type

def main():
    """
    Main function of the program.

    This function checks dependencies, loads the API key, gets user input, generates a command using the Gemini API,
    copies the command to the clipboard, and prints a confirmation message.
    It also allows the user to generate another command or exit the program.
    """
    # Check dependencies first
    check_dependencies()
    
    # Load and configure API key
    # The load_dotenv() function reads key-value pairs from a .env file 
    # and adds them to the environment variables that can be accessed using os.getenv()
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=api_key)

    # Check for API key
    if not api_key:
        print(f"{Fore.RED}Error: API key not found. Please set the 'GOOGLE_API_KEY' environment variable in your .env file.")
        sys.exit(1)

    print(f"{Fore.GREEN}Dependencies installed and API key found. Project setup complete.")
    
    # Get user input
    query, shell_type = get_user_input()
    
    # Generate command using Gemini API
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        # f"Generate a {shell_type.value} command to {query}",
        f"Generate a valid {shell_type.value} command for the following query: {query}. Return ONLY the command, without any explanation.",
        generation_config=genai.types.GenerationConfig(
            temperature=0.2,
            top_k=50,
            top_p=0.95,
            max_output_tokens=100
        )
    )    
    # Extract and print the generated command
    command = response.text.strip()
    
    # Copy command to clipboard
    pyperclip.copy(command)
    
    # Print confirmation message
    print(f"\n{Fore.GREEN}Command '{command}' copied to clipboard.\n")

    # Ask user if they want to generate another command
    while True:
        generate_again = input(f"{Fore.YELLOW}Generate another command? (y/n): ").strip().lower()
        if generate_again in ('y', 'n'):
            break
        print(f"{Fore.RED}Invalid input. Please enter 'y' or 'n'.")

    if generate_again == 'y':
        main()
    else:
        print(f"{Fore.YELLOW}Exiting.")

if __name__ == "__main__":
    main()
