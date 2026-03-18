import os
import shutil

# Folder to organize
path = input("Enter folder path: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

# Get all files
files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)

                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                shutil.move(file_path, os.path.join(folder_path, file))
                moved = True
                break

        # If no match then Others
        if not moved:
            other_path = os.path.join(path, "Others")
            if not os.path.exists(other_path):
                os.mkdir(other_path)

            shutil.move(file_path, os.path.join(other_path, file))

print(" Files organized successfully!")
