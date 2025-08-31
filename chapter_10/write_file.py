from pathlib import Path

contents = "I love programming."
path = Path("chapter_10/programming.txt")
path.write_text(contents, encoding="utf-8")
