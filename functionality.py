import os
from tkinter import filedialog

def browse_file():
    filetypes = (
        ("Video files", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv"),
        ("All files", "*.*")
    )

    file_path = filedialog.askopenfilename(
        title="Select video file",
        initialdir=os.path.expanduser("~"),
        filetypes=filetypes
    )

    if file_path:
        return file_path
    
    return None
