import subprocess
import hashlib
import os

def startCompression():
    result = subprocess.run(
        ["paq8px", "-8", "./compression/originalSmall.txt", "./compression/compressedSmall.paq8px208fix1"], 
        capture_output=True, text=True
    )

    print(result.stdout)  # Print all output at once (since subprocess.run waits)
    
    if result.returncode != 0:
        print("\nError output:")
        print(result.stderr)  # Print errors if any

def startDecompression():
    result = subprocess.run(
        ["paq8px", "-d", "./compression/compressedSmall.paq8px208fix1"], 
        capture_output=True, text=True
    )

    print(result.stdout)  # Print all output at once (since subprocess.run waits)
    
    if result.returncode != 0:
        print("\nError output:")
        print(result.stderr)  # Print errors if any

def get_md5(file_path):
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):  # Read file in chunks
            md5.update(chunk)
    return md5.hexdigest()

def printFiles():
    # Get the list of all files and directories
    path = ".//compression//"
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "' :")

    # Iterate through files and print their sizes
    for file in dir_list:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(f"{file} - {size} bytes")
        else:
            print(f"{file} - [Directory]")


def main():
    #startCompression()
    startDecompression()
    printFiles()



main()