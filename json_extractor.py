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

    # Support UTF-8 output in terminal
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    # Check if a file was dropped onto the script
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input(
            "Enter path to JSON file (or drag & drop file here): "
        ).strip("'\"")

    target_key = input("Enter key to extract: ").strip()

    try:
        # Read JSON with UTF-8 encoding
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Extract matching values
        output = extract_nested_keys(data, target_key)

        # Save output in the same folder
        out_file = os.path.join(
            os.path.dirname(file_path),
            "extracted_output.json"
        )

        # ensure_ascii=False keeps Arabic characters readable
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(
                output,
                f,
                indent=2,
                ensure_ascii=False
            )

        print(f"\nSuccess! Extracted {len(output)} item(s)")
        print(f"Output saved to: {out_file}")

    except FileNotFoundError:
        print("\nError: File not found.")

    except json.JSONDecodeError as e:
        print(f"\nError: Invalid JSON file: {e}")

    except Exception as e:
        print(f"\nError processing file: {e}")

    input("\nPress ENTER to close...")