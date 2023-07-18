import os

# Change directories
os.chdir(r'C:\Users\Username\Desktop')
current_path = os.getcwd()
extensions = []

# Loop through all the files and folders of the directory
for filename in os.listdir():
    if os.path.isdir(filename) or '.' not in filename:
        # If the filename is of type folder or if it have no extension, then we will pass
        pass
    else:
        extension = filename.split('.')[-1]
        folder_name = extension.capitalize()

        if extension not in extensions:
            extensions.append(extension)
            try:
                os.mkdir(folder_name)
            except FileExistsError:
                extensions.append(extension)

        file_path: str = os.path.join(current_path, filename)
        new_path: str = os.path.join(current_path, folder_name, filename)
        
        #Add the File to the directory based on extension
        os.replace(file_path, new_path)

