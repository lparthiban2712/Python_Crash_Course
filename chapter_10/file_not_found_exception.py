from pathlib import Path


try:
    path=Path("chapter_10/alice.txt") 
    contents=path.read_text() 
    print(contents)# Update with the correct path
except FileNotFoundError:
    print(f"Sorry, the file '{path}' was not found.")