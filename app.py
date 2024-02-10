from flask import Flask, request, render_template_string, abort
import os

app = Flask(__name__)

def read_file_with_fallback_encodings(file_path, encodings=('utf-8', 'utf-16')):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.readlines(), None
        except UnicodeDecodeError as e:
            last_exception = e
    return None, last_exception  # Return None and the last exception if all encodings fail

@app.route('/read_file/', defaults={'file_name': 'file1.txt'})
@app.route('/read_file/<file_name>')
def serve_file(file_name):
    file_path = os.path.join('files', file_name)  # Adjust the path as necessary

    start_line = request.args.get('start', default=1, type=int)
    end_line = request.args.get('end', type=int)

    lines, error = read_file_with_fallback_encodings(file_path)
    if error or lines is None:
        return render_template_string('<h1>Error</h1><p>{{ error }}</p>', error=str(error))

    if end_line:
        lines = lines[start_line-1:end_line]
    else:
        lines = lines[start_line-1:]

    content = ''.join(lines)
    return render_template_string('<pre>{{ content }}</pre>', content=content)
def read_file(file_name):
    valid_files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
    if file_name not in valid_files:
        abort(404)  # If the file is not in the list of valid files, return a 404 error

    file_path = os.path.join('files', file_name)  # Adjust path as necessary

    start_line = request.args.get('start', default=1, type=int)
    end_line = request.args.get('end', type=int)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Ensure UTF-8 encoding to handle Chinese characters
            lines = file.readlines()
            if end_line:
                lines = lines[start_line-1:end_line]
            else:
                lines = lines[start_line-1:]
            content = ''.join(lines)
            return render_template_string('<pre>{{ content }}</pre>', content=content)
    except Exception as e:
        return render_template_string('<h1>Error</h1><p>{{ error }}</p>', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

