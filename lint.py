"""A script to run Pylint for static code analysis on the 'app' directory."""

import os
import subprocess

def run_pylint():
    """
    Finds all Python files in the 'app' directory and runs Pylint on them.
    """
    project_dir = "app"
    if not os.path.isdir(project_dir):
        print(f"Error: Directory '{project_dir}' not found.")
        return

    py_files = []
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))

    if not py_files:
        print("No Python files found to analyze.")
        return

    print("Running Pylint on the following files:")
    for file in py_files:
        print(f"- {file}")
    
    print("\n" + "="*50 + "\n")

    # Add --rcfile option if .pylintrc exists
    pylint_command = ["pylint"]
    if os.path.exists(".pylintrc"):
        pylint_command.append("--rcfile=.pylintrc")
    
    pylint_command.extend(py_files)
    
    try:
        # Using subprocess.run to execute the command.
        # We explicitly set the encoding to 'utf-8' and ignore errors
        result = subprocess.run(
            pylint_command,
            capture_output=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        print("Pylint Output:\n")
        print(result.stdout)
        
        if result.stderr:
            print("Pylint Errors:\n")
            print(result.stderr)

        print("\n" + "="*50)
        print("Pylint analysis complete.")

    except FileNotFoundError:
        print("Error: 'pylint' command not found.")
        print("Please ensure Pylint is installed and in your system's PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_pylint()
