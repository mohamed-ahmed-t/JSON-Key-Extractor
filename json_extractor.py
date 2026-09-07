import json
import sys
import os

def extract_nested_keys(data, target_key):
    results = []
    def search(item):
        if isinstance(item, dict):
            for k, v in item.items():
                if k == target_key:
                    results.append(v)
                search(v)
        elif isinstance(item, list):
            for elem in item:
                search(elem)
    search(data)
    return results

if __name__ == "__main__":
    # Check if a file was dropped onto the script
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter path to JSON file (or drag & drop file here): ").strip("'\"")

    target_key = input("Enter key to extract: ").strip()

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        output = extract_nested_keys(data, target_key)

        # Saves output automatically to 'extracted_output.json' in the same folder
        out_file = os.path.join(os.path.dirname(file_path), "extracted_output.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)

        print(f"\nSuccess! Extracted {len(output)} item(s) to: {out_file}")

    except Exception as e:
        print(f"\nError processing file: {e}")

    input("\nPress ENTER to close...")