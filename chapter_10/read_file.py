from pathlib import Path

path = Path("chapter_10\pi_digits.txt")
contents = path.read_text("utf-8")
print(contents.rstrip())