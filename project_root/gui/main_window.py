import tkinter as tk
from tkinter import filedialog, messagebox
from handlers.file_handler import load_file, save_file
from handlers.chatgpt_handler import process_assignment

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("README Generator")
        
        self.label = tk.Label(self, text="Select an assignment.md file:")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(self, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)
        
        self.analyze_button = tk.Button(self, text="Begin Analysis", command=self.begin_analysis, state=tk.DISABLED)
        self.analyze_button.pack(pady=5)
        
        self.progress_label = tk.Label(self, text="")
        self.progress_label.pack(pady=10)
        
        self.save_button = tk.Button(self, text="Save Output", command=self.save_output, state=tk.DISABLED)
        self.save_button.pack(pady=5)
        
        self.file_path = ""
        self.readme_content = ""

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        if self.file_path:
            self.analyze_button.config(state=tk.NORMAL)

    def begin_analysis(self):
        self.progress_label.config(text="Processing...")
        self.update()
        assignment_content = load_file(self.file_path)
        self.readme_content = process_assignment(assignment_content)
        self.progress_label.config(text="Analysis Complete")
        self.save_button.config(state=tk.NORMAL)

    def save_output(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])
        if save_path:
            save_file(save_path, self.readme_content)
            messagebox.showinfo("Success", "README.md saved successfully!")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
