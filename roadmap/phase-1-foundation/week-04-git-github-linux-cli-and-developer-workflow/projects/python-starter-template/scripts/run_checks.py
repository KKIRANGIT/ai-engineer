"""
Run the same basic check locally that the CI workflow runs.
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Run the starter template unit tests from the project root."""
    project_root = Path(__file__).resolve().parent.parent
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        cwd=project_root,
        check=False,
    )

    if result.returncode == 0:
        print("Checks passed.")
    else:
        print("Checks failed.")
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
