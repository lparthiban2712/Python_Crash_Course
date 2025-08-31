from pathlib import Path
import json
numbers = list(range(1, 11))
path = Path("chapter_10/numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)