
# Password Guessing Game

A simple Python password guessing where you try to guess the correct password. It is built with FastAPI

## Description

This project is a basic password guessing game implemented in Python. 
It generates a random password and challenges the user to guess it correctly. 

## Features

- Randomly generated passwords.
- User-friendly command-line interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/password-guess.git
   ```

2. Navigate to the project directory:

   ```bash
   cd password-guess
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the game:

   ```bash
    uvicorn main:app --reload --port 8080
   ```
