# A  program that reads a file and writes a modified version to a new file
def read_and_modify_file():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            content = file.read()
            print("File read successfully.")
            
            # Modify the content (for example, convert to uppercase)
            modified_content = content.upper() 
            
            # Write the modified content to a new file
            new_filename = f"modified_{filename}"
            with open(new_filename, 'w') as new_file:
                new_file.write(modified_content)
            print(f"Modified content has been written to {new_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    
    except IOError:
        print(f"Error: The file '{filename}' could not be read or written.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Run the program
if __name__ == "__main__":
    read_and_modify_file()
