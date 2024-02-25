import re
import os
import sys
import time

def print_program_info():
    print("****************************************************************************************************\n")
    print(" JSpy Minify  -  v1.022024")
    print(" (c) 2024 by Marc Sczepanski")
    print(" https://github.com/praetoriani\n")
    print("****************************************************************************************************\n")
    print(" JSpy Minify is a simple Python script that can optimize/compress Javascript files.")
    print(" To continue, please provide the full path to the JS file you want to edit with JSpy Minify below.\n")
    print("****************************************************************************************************\n")
    

def remove_comments(js_code):
    js_code = re.sub(re.compile(r'/\*.*?\*/', re.DOTALL), '', js_code)
    js_code = re.sub(re.compile(r'//.*?\n'), '', js_code)
    return js_code

def remove_empty_lines(js_code):
    lines = js_code.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']
    return '\n'.join(non_empty_lines)

def remove_leading_spaces(js_code):
    lines = js_code.split('\n')
    lines_without_leading_spaces = [line.lstrip() for line in lines]
    return '\n'.join(lines_without_leading_spaces)

def remove_newlines(js_code):
    return js_code.replace('\n', ' ')

def minify_js(file_path):
    try:
        with open(file_path, 'r') as file:
            js_code = file.read()

        print("[1] Removing JS Comments...")
        js_code = remove_comments(js_code)
        time.sleep(1)  # Kurze Pause

        print("[2] Removing empty lines ...")
        js_code = remove_empty_lines(js_code)
        time.sleep(1)  # Kurze Pause

        print("[3] Removing needless whitespaces...")
        js_code = remove_leading_spaces(js_code)
        time.sleep(1)  # Kurze Pause

        print("[4] Removing line beaks ...")
        js_code = remove_newlines(js_code)
        time.sleep(1)  # Kurze Pause

        minified_path = os.path.join(os.path.dirname(file_path), os.path.basename(file_path).replace('.js', '.min.js'))
        with open(minified_path, 'w') as file:
            file.write(js_code)

        print("****************************************************************************************************")
        print(f"JSpy Minify processed the following file:\n{os.path.basename(file_path)}")
        print("****************************************************************************************************")
        print(f"Modified file has been created:\n{os.path.basename(minified_path)}")
        print("****************************************************************************************************")
        print("Press any key to exit")
        input()
    except Exception as e:
        print(f"An error has occurred: {e}")
        print("****************************************************************************************************")
        print("Press any key to exit")
        input()
        sys.exit(1)

def main():
    print_program_info()
    try:
        print("Location of the JS File:")
        file_path = input()
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")

        print(f"\nFile '{os.path.basename(file_path)}' will go through the following steps:")
        print("[1] Remove all JS comments")
        print("[2] Remove all empty lines")
        print("[3] Remov needless whitespaces")
        print("[4] Remove all line breaks")
        user_choice = input("\nEnter Y to start editing and N to cancel editing and exit the program:\n").upper()

        if user_choice == 'N':
            print("Processing canceled by User. The program will exit.")
            sys.exit(0)
        elif user_choice == 'Y':
            minify_js(file_path)
        else:
            raise ValueError("Invalid Input. Please enter Y or N.")

    except FileNotFoundError as e:
        print(e)
        print("****************************************************************************************************")
        print("Press any key to exit the program.")
        input()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("****************************************************************************************************")
        print("Press any key to exit the program.")
        input()

if __name__ == "__main__":
    main()