import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


class GitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Git GUI Wrapper")
        self.root.geometry("700x600")
        
        # Current working directory
        self.current_dir = os.getcwd()

        # Git operation buttons
        tk.Button(root, text="Initialize Repository", command=self.init_repo).pack(pady=5)
        tk.Button(root, text="Check Status", command=self.git_status).pack(pady=5)
        tk.Button(root, text="Add Files", command=self.git_add).pack(pady=5)
        tk.Button(root, text="Commit Changes", command=self.git_commit).pack(pady=5)
        tk.Button(root, text="View Logs", command=self.git_log).pack(pady=5)
        tk.Button(root, text="Push to Remote", command=self.git_push).pack(pady=5)
        tk.Button(root, text="Pull from Remote", command=self.git_pull).pack(pady=5)
        tk.Button(root, text="Create New Branch", command=self.git_branch).pack(pady=5)
        tk.Button(root, text="Switch Branch", command=self.git_checkout).pack(pady=5)
        tk.Button(root, text="Merge Branch", command=self.git_merge).pack(pady=5)
        tk.Button(root, text="Clone Repository", command=self.git_clone).pack(pady=5)
        tk.Button(root, text="Change Directory", command=self.change_directory).pack(pady=5)
        
        # Log display
        self.log_text = tk.Text(root, wrap=tk.WORD, height=15)
        self.log_text.pack(pady=10, fill=tk.BOTH, expand=True)
        self.log_text.insert(tk.END, f"Current Directory: {self.current_dir}\n")

    def run_command(self, command):
        """Run a shell command and return the output."""
        try:
            result = subprocess.run(
                command, shell=True, text=True, capture_output=True, cwd=self.current_dir
            )
            output = result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
            self.log_text.insert(tk.END, f"{output}\n")
            self.log_text.see(tk.END)
        except Exception as e:
            self.log_text.insert(tk.END, f"Error: {str(e)}\n")
            self.log_text.see(tk.END)

    def init_repo(self):
        """Initialize a Git repository."""
        self.run_command("git init")

    def git_status(self):
        """Check the status of the Git repository."""
        self.run_command("git status")

    def git_add(self):
        """Add files to staging."""
        files = filedialog.askopenfilenames(title="Select Files to Add")
        if files:
            for file in files:
                rel_path = os.path.relpath(file, self.current_dir)
                self.run_command(f"git add {rel_path}")

    def git_commit(self):
        """Commit staged changes."""
        commit_message = simpledialog.askstring("Commit", "Enter commit message:")
        if commit_message:
            self.run_command(f'git commit -m "{commit_message}"')

    def git_log(self):
        """View the Git log."""
        self.run_command("git log --oneline")

    def git_push(self):
        """Push changes to a remote repository."""
        remote = simpledialog.askstring("Push", "Enter remote name (default: origin):", initialvalue="origin")
        branch = simpledialog.askstring("Push", "Enter branch name (default: main):", initialvalue="main")
        if remote and branch:
            self.run_command(f"git push {remote} {branch}")

    def git_pull(self):
        """Pull changes from a remote repository."""
        remote = simpledialog.askstring("Pull", "Enter remote name (default: origin):", initialvalue="origin")
        branch = simpledialog.askstring("Pull", "Enter branch name (default: main):", initialvalue="main")
        if remote and branch:
            self.run_command(f"git pull {remote} {branch}")

    def git_branch(self):
        """Create a new branch."""
        branch_name = simpledialog.askstring("Create Branch", "Enter new branch name:")
        if branch_name:
            self.run_command(f"git branch {branch_name}")

    def git_checkout(self):
        """Switch to another branch."""
        branch_name = simpledialog.askstring("Switch Branch", "Enter branch name:")
        if branch_name:
            self.run_command(f"git checkout {branch_name}")

    def git_merge(self):
        """Merge a branch into the current branch."""
        branch_name = simpledialog.askstring("Merge Branch", "Enter branch name to merge:")
        if branch_name:
            self.run_command(f"git merge {branch_name}")

    def git_clone(self):
        """Clone a remote repository."""
        repo_url = simpledialog.askstring("Clone Repository", "Enter repository URL:")
        if repo_url:
            directory = filedialog.askdirectory(title="Select Directory to Clone Into")
            if directory:
                self.run_command(f"git clone {repo_url} {directory}")

    def change_directory(self):
        """Change the current working directory."""
        new_dir = filedialog.askdirectory(title="Select Directory")
        if new_dir:
            self.current_dir = new_dir
            self.log_text.insert(tk.END, f"Changed Directory to: {self.current_dir}\n")
            self.log_text.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = GitGUI(root)
    root.mainloop()
