def load_file(file_path):
    """Load the content of a file."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def save_file(file_path, content):
    """Save content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)
