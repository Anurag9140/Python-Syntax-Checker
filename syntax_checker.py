def check_python_syntax(file_path):
    try:
        # Read the contents of the file
        with open(file_path, 'r') as file:
            code = file.read()

        # Try compiling the code without executing it
        compile(code, file_path, 'exec')
        print("✅ No syntax errors found. The file is valid.")

    except SyntaxError as e:
        print(f"Syntax Error at line {e.lineno}: {e.msg}")
        print(f" Code: {e.text.strip() if e.text else 'N/A'}")

    except FileNotFoundError:
        print(" File not found. Please check the file path.")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    print("Python Syntax Checker Tool")
    file_path = input("Enter the path to your Python file: ").strip()
    check_python_syntax(file_path)
