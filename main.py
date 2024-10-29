import google.generativeai as genai
import pyperclip
import sys
from dotenv import load_dotenv
import os

def check_dependencies():
    required_packages = ["google.generativeai", "pyperclip"]
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("Error: Missing dependencies. Please install the following packages:")
        for package in missing_packages:
            print(f"  {package}")
        sys.exit(1)

from enum import Enum

class Shell(Enum):
    CMD = "Windows Command Prompt"
    POWERSHELL = "PowerShell"
    BASH = "bash"

def get_shell_selection() -> Shell:
    shells = {
        str(i): shell 
        for i, shell in enumerate(Shell, 1)
    }
    
    print("\nSelect shell type:")
    for num, shell in shells.items():
        print(f"{num}. {shell.value}")
        
    while True:
        selection = input("Enter number (1-3): ").strip()
        if selection in shells:
            return shells[selection]
        print("Invalid selection. Please choose 1, 2, or 3.")

def get_command_description() -> str:
    print("\nDescribe the command you want to generate:")
    return input("> ").strip()

def get_user_input():
    query = get_command_description()
    shell_type = get_shell_selection()
    
    print("\nYour inputs:")
    print(f"Command description: {query}")
    print(f"Selected shell: {shell_type.value}")
    
    return query, shell_type
def main():
    # Check dependencies first
    check_dependencies()
    
    # Load and configure API key
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=api_key)

    # Check for API key
    if not api_key:
        print("Error: API key not found. Please set the 'GOOGLE_API_KEY' environment variable in your .env file.")
        sys.exit(1)

    print("Dependencies installed and API key found. Project setup complete.")
    
    # Get user input
    query, shell_type = get_user_input()
    
    # Generate command using Gemini API
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        f"Generate a {shell_type.value} command to {query}",
        generation_config=genai.types.GenerationConfig(
            temperature=0.2,
            top_k=50,
            top_p=0.95,
            max_output_tokens=100
        )
    )    

    # Extract and print the generated command
    command = response.text
    
    # Copy command to clipboard
    pyperclip.copy(command)
    
    # Print confirmation message
    print(f"Command '{command}' copied to clipboard.")

    # Ask user if they want to generate another command
    while True:
        generate_again = input("Generate another command? (y/n): ").strip().lower()
        if generate_again in ('y', 'n'):
            break
        print("Invalid input. Please enter 'y' or 'n'.")

    if generate_again == 'y':
        main()
    else:
        print("Exiting.")

if __name__ == "__main__":
    main()
