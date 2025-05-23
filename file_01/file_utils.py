import os

def check_files(path):
    if os.path.isfile(path):
        try:
            with open(path, 'r') as f:
                size_kb = os.path.getsize(path) / 1024
                print(f"✅ File is readable: {path}")
                print(f"📦 Size in KB: {size_kb:.2f}\n")
        except PermissionError:
            print(f"🚫 Permission denied: {path}\n")
    else:
        print(f"❌ File does not exist: {path}\n")

