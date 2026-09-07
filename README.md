# JSON Key Extractor Utility

A simple, fast, and flexible Python tool to extract specific keys from flat or deeply nested JSON structures and output them into a clean JSON array.

---

## 🌟 Features

- **Deep Key Extraction:** Recursively searches through nested dictionaries and lists to extract target keys regardless of depth.
- **Multiple Workflows Supported:**
  - Drag-and-drop JSON file execution.
  - Interactive CLI prompts.
  - Command-line argument execution.
  - Pipe streaming via standard input (`stdin`).
- **Zero External Dependencies:** Built entirely with native Python standard libraries (`json`, `sys`, `os`).

---

## 🚀 Quick Start Guide

### Prerequisites

- **Python 3.x** installed on your system.
  - Check your Python installation by running:
    ```bash
    python --version
    # or
    python3 --version
    ```

---

## 📂 Installation

1. **Clone or Download** this repository/script.
2. Place the Python script (`json_extractor.py`) in your project folder.

---

## 🛠️ Usage Methods

### Method 1: Interactive / Drag & Drop (Easiest)

Run the script without arguments. It will prompt you to enter or drag-and-drop a file path and specify the key you want to extract:

```bash
python json_extractor.py
```

**Example Prompt Session:**
```text
Enter path to JSON file (or drag & drop file here): data.json
Enter key to extract: email

Success! Extracted 3 item(s) to: extracted_output.json
```

---

### Method 2: Command-Line Arguments

Pass the input JSON file and target key directly as command-line arguments:

```bash
python json_extractor.py <path_to_json_file> <target_key>
```

**Example:**
```bash
python json_extractor.py users.json name
```


## 📝 Example Output

### Input (`data.json`)
```json
{
  "company": "TechCorp",
  "departments": [
    {
      "department_name": "Engineering",
      "manager": { "name": "Alice", "id": 101, "email": "alice@techcorp.com" },
      "teams": [
        { "team": "Frontend", "lead": { "name": "Bob", "id": 102, "email": "bob@techcorp.com" } },
        { "team": "Backend", "lead": { "name": "Charlie", "id": 103, "email": "charlie@techcorp.com" } }
      ]
    }
  ]
}
```

### Command
```bash
python json_extractor.py data.json email
```

### Result (`extracted_output.json`)
```json
[
  "alice@techcorp.com",
  "bob@techcorp.com",
  "charlie@techcorp.com"
]
```

---

## 🖥️ One-Click Windows Drag & Drop Setup

To make extraction even faster on Windows without using the command terminal:

1. Create a file named `run.bat` in the same directory as `json_extractor.py`.
2. Add the following line to `run.bat`:
   ```cmd
   python json_extractor.py %1
   ```
3. Simply **drag and drop any `.json` file directly onto `run.bat`**.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
