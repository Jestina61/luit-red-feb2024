import os

def generate_file_info():
    # Get the current working directory
    cwd = os.getcwd() 
    
    # List all files and directories in the current working directory
    files = os.listdir(cwd)
    
    # Initialize an empty list to store file information dictionaries
    file_info_list = []
    
    # Iterate through each file in the directory
    for file_name in files:
        # Construct the full file path
        file_path = os.path.join(cwd, file_name)      
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get file size in bytes
            file_size = os.path.getsize(file_path)
            
            # Get file last modified timestamp
            last_modified = os.path.getmtime(file_path)
            
            # Create a dictionary with file information
            file_info = {
                "file_name": file_name,
                "file_path": file_path,
                "file_size": file_size,
                "last_modified": last_modified
            }
            
            # Append the dictionary to the list
            file_info_list.append(file_info)
    
    return file_info_list

# Function call to generate file information
files_info = generate_file_info()

# Print the list of dictionaries
for file_info in files_info:
    print(file_info)
