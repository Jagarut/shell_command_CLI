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
if __name__ == "__main__":
    main()
