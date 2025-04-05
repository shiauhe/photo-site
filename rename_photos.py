# -*- coding: utf-8 -*-
import os

# Directory containing the photos
photo_dir = "personal-profile/photo"

# Function to rename files by truncating the trailing part
def rename_photos(directory):
    for filename in os.listdir(directory):
        if "-" in filename:
            base_name, _ = filename.rsplit("-", 1)  # Split at the last hyphen
            extension = filename.split(".")[-1]  # Get the file extension
            new_filename = f"{base_name}.{extension}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Handle file name conflicts
            counter = 1
            while os.path.exists(new_path):
                new_filename = f"{base_name}_{counter}.{extension}"
                new_path = os.path.join(directory, new_filename)
                counter += 1
            
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Run the script
if __name__ == "__main__":
    rename_photos(photo_dir)
