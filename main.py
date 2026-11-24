import os
import shutil
import sys
from pathlib import Path

def main():
    bot_dir = Path(os.environ.get("MAKEFUN_BOT_DIR", "."))
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out")).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    src = bot_dir / "entry.png"
    dst = output_dir / "entry.png"
    
    if src.exists():
        shutil.copy(src, dst)
        print(f"Successfully copied {src} to {dst}")
    else:
        sys.stderr.write(f"Error: Source {src} not found!\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
