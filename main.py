import google.generativeai as genai
import pyperclip
import sys

def main():
    # Set up API key
    genai.configure(api_key="YOUR_API_KEY")

    # Check for API key
    if not genai.get_api_key():
        print("Error: API key not found. Please set the 'GOOGLE_APPLICATION_CREDENTIALS' environment variable to the path of your API key file.")
        sys.exit(1)

    # Check for dependencies
    try:
        import google.generativeai
        import pyperclip
    except ImportError:
        print("Error: Missing dependencies. Please install the following packages:")
        print("  google-generativeai")
        print("  pyperclip")
        sys.exit(1)

    print("Dependencies installed and API key found. Project setup complete.")

if __name__ == "__main__":
    main()
