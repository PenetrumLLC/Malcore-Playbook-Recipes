import os
import re
import json


RECIPE_DIR = "recipes"
DB_PATH = "assets/dbs"
OUTPUT_FILE = os.path.join(DB_PATH, "files.json")


def extract_metadata(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    def grab(pattern, default="N/A"):
        match = re.search(pattern, content)
        return match.group(1) if match else default

    return {
        "filename": os.path.basename(filepath),
        "version": grab(r'__version__\s*=\s*["\'](.+?)["\']'),
        "hashsum": grab(r'__hashsum__\s*=\s*["\'](.+?)["\']'),
        "author": grab(r'__author__\s*=\s*["\'](.+?)["\']')
    }


def update_recipe_count():
    count_badge_path = "assets/dbs/recipe-count-badge.json"
    recipe_count_path = "assets/dbs/files.json"
    total_count = len(json.load(open(recipe_count_path)))
    with open(count_badge_path, "w") as fh:
        data = {
            "schemaVersion": 1,
            "label": "Available Recipes",
            "message": f"{total_count}",
            "color": "blue"
        }
        json.dump(data, fh)


def main():
    entries = []
    for file in os.listdir(RECIPE_DIR):
        if file.endswith(".py"):
            full_path = os.path.join(RECIPE_DIR, file)
            entries.append(extract_metadata(full_path))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        json.dump(entries, out, indent=2)
    print(f"Metadata written to: {OUTPUT_FILE}")
    update_recipe_count()
    print("Recipe count badge updated")


if __name__ == "__main__":
    main()
