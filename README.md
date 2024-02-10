# About Flask File Renderer

## Introduction

The Flask File Renderer is a web application designed to dynamically serve text files over the web. This utility allows users to view the content of text files directly in their web browser with the option to specify a particular range of lines to be displayed. The application supports text files encoded in UTF-8 and UTF-16, ensuring compatibility with a variety of languages and character sets, including files containing Chinese characters.

## Features

- **Dynamic File Serving**: Users can request to view any text file available on the server by specifying its name in the URL.
- **Line Range Specification**: Through URL parameters, users can request a specific range of lines from the file, allowing for partial content display.
- **Multiple Encoding Support**: The application can handle files encoded in both UTF-8 and UTF-16, catering to a diverse set of text files.
- **Error Handling**: The application provides graceful error handling for scenarios such as missing files or incorrect URL parameters, enhancing user experience.

## Use Cases

- Viewing logs or documents hosted on a server without the need to download them.
- Displaying excerpts from large text files for quick reference.
- Serving content in multiple languages from text files through a web interface.

## Technical Stack

- **Framework**: Flask (Python)
- **Languages**: Supports text files in various languages, including those with special characters.
- **Encoding**: Handles UTF-8 and UTF-16 encoded text files.

For more information on how to set up and run the project, please refer to the `RUNNING.md` file.


# Running Flask File Renderer
## Setup and Installation

Ensure you have Python 3.6 or newer installed on your system as the application is built with Flask, which requires Python.

1. Clone the Repository To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Mandil-18/flask-file-renderer.git
cd flask-file-renderer

2. Create and Activate a Virtual Environment
Set up a virtual environment to manage the application's dependencies separately from your system's global Python packages:

python3 -m venv venv
source venv/bin/activate  # Use 'venv\Scripts\activate' on Windows

3. Install Dependencies
Install the necessary Python packages as specified in the REQUIREMENTS.txt:

pip install -r REQUIREMENTS.txt

Running the Application
With the setup complete, you can now run the Flask application:

flask run

Usage Instructions
To view a file, append the /read_file/<file_name> route to the base URL, and specify the name of the file you wish to view. Optionally, you can also specify the range of lines by adding ?start=<line_start>&end=<line_end> parameters to the URL.

Example
To view lines 10 to 20 of file2.txt:
http://127.0.0.1:5000/read_file/file2.txt?start=10&end=20



