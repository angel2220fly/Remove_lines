def remove_empty_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Remove empty lines and lines with only spaces
        cleaned_lines = [line for line in lines if line.strip()]
        
        with open(file_path, 'w') as file:
            file.writelines(cleaned_lines)
        
        print("Empty lines removed successfully.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the path to your Python file
file_path = "Black_Hole_5.py"
remove_empty_lines(file_path)
