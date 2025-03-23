import subprocess
import os

def printFiles():
    # Get the list of all files and directories
    path = ".//compression//"
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "' :")

    # Iterate through files and print their sizes
    for file in dir_list:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):  # Ensure it's a file, not a directory
            size = os.path.getsize(file_path)
            print(f"{file} - {size} bytes")
        else:
            print(f"{file} - [Directory]")

def startCompression():
    # Run a command and capture output
    result = subprocess.run(["paq8px", "-8", "./compression/originalSmall.txt","./compression/compressedSmall.paq8px"], capture_output=True, text=True)

    # Print the output
    print(result.stdout)

def main():
    startCompression()
    printFiles()



main()