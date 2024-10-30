# Shell Command Generator

A CLI tool that generates shell commands using Google's Gemini AI model. Simply describe what you want to do in plain English, select your preferred shell, and get the command copied to your clipboard.

## Features

- Supports multiple shells:
- Windows Command Prompt (CMD)
- PowerShell
- Bash
- Uses Google's Gemini AI for accurate command generation
- Automatic clipboard copy of generated commands
- Environment-based configuration

## Technologies

- Python 3.x
- Google Generative AI API
- pyperclip
- python-dotenv

## Setup

1. Clone the repository
2. Install dependencies:

pip install -r requirements.txt

3. Create a .env file in the project root with your Google API key:

GOOGLE_API_KEY=your_api_key_here

## Usage

1. Run the application:

python main.py

2. Follow the prompts to describe your task, select your shell, and get the generated command.

### Example:

> python main.py
> Dependencies installed and API key found. Project setup complete.

Describe the command you want to generate:

> list all files in current directory including hidden ones

Select shell type:

1. Windows Command Prompt
2. PowerShell
3. bash
   Enter number (1-3): 3

Command 'ls -la' copied to clipboard.

### Testing

Run the test suite:

python -m unittest test_main.py
