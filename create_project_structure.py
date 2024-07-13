import os

# Define the file structure
file_structure = {
    "project_root": {
        "gui": ["__init__.py", "main_window.py", "progress_bar.py", "file_dialog.py"],
        "handlers": ["__init__.py", "file_handler.py", "chatgpt_handler.py"],
        "templates": ["readme_template.md"],
        "data": {
            "input": [],
            "output": []
        },
        "tests": ["__init__.py", "test_file_handler.py", "test_chatgpt_handler.py"],
        "files": ["main.py", "requirements.txt", "README.md"]
    }
}

# Function to create file structure
def create_file_structure(base_path, structure):
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_file_structure(path, value)
        elif isinstance(value, list):
            os.makedirs(path, exist_ok=True)
            for file in value:
                open(os.path.join(path, file), 'a').close()

# Create the file structure
base_path = "project_root"
create_file_structure(base_path, file_structure["project_root"])

print("File structure created successfully.")