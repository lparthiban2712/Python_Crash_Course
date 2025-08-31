from pathlib import Path
import json

def get_stored_username(filename):
    """Get stored username if available."""
    path = Path(filename)
    content=path.read_text()
    username=json.loads(content)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path("chapter_10/user.json")
    if path.exists():
        username = get_stored_username(path)
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = input("What is your name? ")
            path.write_text(json.dumps(username))
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = input("What is your name? ")
        path.write_text(json.dumps(username))
        print(f"We'll remember you when you come back, {username}!")
greet_user()