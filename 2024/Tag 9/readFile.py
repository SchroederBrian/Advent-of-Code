import os

def readFile():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'input.txt')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as input_file:
            content = input_file.read()
            return content
    else:
        print(f"Datei {file_path} nicht gefunden.")
        return None