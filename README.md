Fileamass – File Organizer CLI Tool



Description

This tool automatically organizes files into folders based on file type.



&#x20;Features

* Organizes images, documents, videos, etc.
* &#x20;Creates folders automatically
* Simple CLI usage



&#x20;How to Run

```bash

python main.py
```
## How It Works
1. The user provides a folder path.
2. The program reads all files in that folder.
3. It identifies the file type using the extension.
4. It creates folders for each category (if not already present).
5. It moves files into their respective folders.
6. Unrecognized files are moved to an "Others" folder.
