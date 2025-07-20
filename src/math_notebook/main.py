import subprocess
import os

_NOTEBOOK_DIR = os.path.expanduser('~/math-notebooks')

if __name__ == "__main__":
    subprocess.run([
        "jupyter", "lab",
        "--notebook-dir", _NOTEBOOK_DIR,
        "--no-browser",
        "--port", "8888"
    ])
