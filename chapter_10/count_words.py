from pathlib import Path

path=Path("chapter_10/pi_digits.txt")  # Update with the correct path
contents=path.read_text()
words=contents.split()
print(words)
num_words=len(words)
print(f"The file contains about {num_words} words.")