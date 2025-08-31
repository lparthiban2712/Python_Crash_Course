from pathlib import Path

def count_words_in_file(filename):
    """Count the number of words in a file."""
    try:
        path = Path(filename)
        contents = path.read_text(encoding="utf-8")
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' contains about {num_words} words.")
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")   

filenames = ["chapter_10/pi_digits.txt", "chapter_10/test.txt"]
for filename in filenames:
    count_words_in_file(filename)
