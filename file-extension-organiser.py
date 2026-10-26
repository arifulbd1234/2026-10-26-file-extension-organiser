"""
Day 20 - 2026-10-26
Tool: File Extension Organiser
What it does: Takes a list of file names and groups them by their
extension into folders like Images, Documents, Audio and Others -
the plan you need before tidying a messy Downloads folder.
Who it helps: Anyone whose Downloads or desktop is full of mixed
files and who wants to sort them in seconds.
"""

GROUPS = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"},
    "Audio": {".mp3", ".wav", ".ogg"},
    "Video": {".mp4", ".mkv", ".mov"},
    "Archives": {".zip", ".rar", ".7z"},
    "Code": {".py", ".js", ".html", ".css"},
}


def group_for(filename):
    """Return which group a file belongs to, based on its extension."""
    dot = filename.rfind(".")
    ext = filename[dot:].lower() if dot != -1 else ""
    for group, extensions in GROUPS.items():
        if ext in extensions:
            return group
    return "Others"


def organise(filenames):
    plan = {}
    for name in filenames:
        plan.setdefault(group_for(name), []).append(name)
    return plan


if __name__ == "__main__":
    files = ["photo.jpg", "report.pdf", "song.mp3", "notes.txt",
             "movie.mp4", "backup.zip", "script.py", "mysteryfile"]
    plan = organise(files)
    for group in sorted(plan):
        print(group + ":", ", ".join(plan[group]))
