import os
import shutil
import sys
from datetime import datetime

def backup_files(source_directory, dest_directory):
    # Check if source directory exists
    if not os.path.isdir(source_directory):
        print("Source directory does not exist.")
        return

    # Check if destination directory exists
    if not os.path.isdir(dest_directory):
        print("Destination directory does not exist.")
        return
    
    for filename in os.listdir(source_directory):
        source_file = os.path.join(source_directory, filename)

        if os.path.isfile(source_file):
            dest_file = os.path.join(dest_directory, filename)

            # Check if file already exists in destination
            if os.path.exists(dest_file):
                # Append timestamp to file name before extension
                name, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                new_filename = "{name}_{timestamp}{ext}"
                dest_file = os.path.join(dest_directory, new_filename)

            try:
                shutil.copy2(source_file, dest_file)
                print("Copy Completed")
            except Exception as e:
                print("Failed to copy")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("provide files with source and destination directry")
    else:
        source = r"C:\Users\Anish\OneDrive\Desktop\folder1"
        destination = r"C:\Users\Anish\OneDrive\Desktop\backup"
        backup_files(source, destination)
