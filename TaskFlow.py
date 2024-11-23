import sys
from pathlib import Path

# Add the `src` directory to the Python path
src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))

# Import and run the main app
from app import main

if __name__ == "__main__":
    main()
