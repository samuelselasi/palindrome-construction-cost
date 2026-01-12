import subprocess
import sys

# --- CONFIGURATION ---
# The scripts to test
scripts = [
    "solution.py",
    "qwen/run_01.py",
    "qwen/run_02.py",
    "qwen/run_03.py"
]

# The 6 Killer Test Cases
# Format: (Description, Input String)
test_cases = [
    ("1. Classic Trap (aba)",   "3 2\naba"),
    ("2. High Val Mid (aza)",   "3 2\naza"),
    ("3. Descending (cba)",     "3 2\ncba"),
    ("4. High Val Seq (zyx)",   "3 2\nzyx"),
    ("5. Even Mirror (abba)",   "4 2\nabba"),
    ("6. Long Mirror (abcba)",  "5 2\nabcba")
]

def run_script(script_path, input_str):
    """Runs a python script with the given input and returns the output."""
    try:
        # Run python3 script_path, pipe input_str to stdin, capture stdout
        result = subprocess.run(
            [sys.executable, script_path],
            input=input_str,
            text=True,
            capture_output=True
        )
        if result.returncode != 0:
            return "ERR"
        return result.stdout.strip()
    except FileNotFoundError:
        return "N/A" # File doesn't exist yet
    except Exception as e:
        return "ERR"

def main():
    print(f"{'TEST CASE':<25} | {'SOLUTION':<10} | {'RUN_01':<10} | {'RUN_02':<10} | {'RUN_03':<10}")
    print("-" * 85)

    for desc, input_data in test_cases:
        row_output = [desc]
        
        # Get the "Ground Truth" from solution.py first
        truth = run_script("solution.py", input_data)
        row_output.append(truth)
        
        # Run the Qwen scripts
        for script in scripts[1:]: # Skip solution.py
            out = run_script(script, input_data)
            
            # Formatting: Add '*' if it fails (differs from truth)
            if out != truth and out not in ["ERR", "N/A"]:
                display = f"{out} *"
            else:
                display = out
            
            row_output.append(display)

        # Print the row
        print(f"{row_output[0]:<25} | {row_output[1]:<10} | {row_output[2]:<10} | {row_output[3]:<10} | {row_output[4]:<10}")

    print("-" * 85)
    print("* Denotes a failure (result differs from solution.py)")

if __name__ == "__main__":
    main()
