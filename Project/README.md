# Expert System - Skin Care

This project is a rule-based expert system for skin care using the `experta` library in Python. The project is divided into multiple files to maintain modularity and clarity.

## Project Structure

/Project
    ├── facts.py
    ├── rules.py
    ├── engine.py
    ├── main.py
    ├── utils.py
    ├── gui.py
    ├── README.md


### File Descriptions

- `facts.py`: Defines the facts used in the expert system.
- `rules.py`: Defines the rules for the expert system.
- `engine.py`: Sets up the knowledge engine and integrates the rules.
- `main.py`: The main script to run the expert system.
- `utils.py`: Contains utility functions and type hinting.
- `gui.py`: Implements the graphical user interface using Tkinter.

## Prerequisites

- Python 2.7
- `experta` library
- `typing` module

## Installation

1. **Install Python 2.7:**

   Ensure you have Python 2.7 installed. You can download it from [python.org](https://www.python.org/downloads/release/python-2718/).

2. **Install `pip`:**

   Download the `get-pip.py` script:

   ```sh
   curl -O https://bootstrap.pypa.io/pip/2.7/get-pip.py
