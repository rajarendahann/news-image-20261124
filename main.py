import os
import shutil
from pathlib import Path
from gen_image import generate_image

def main():
    bot_dir = Path(os.environ.get("MAKEFUN_BOT_DIR", "."))
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate the entry image first
    img_path = bot_dir / "entry.png"
    generate_image(str(img_path))
    
    src = img_path
    dst = output_dir / "entry.png"
    
    if src.exists():
        shutil.copy(src, dst)
        print(f"Successfully copied {src} to {dst}")
    else:
        print(f"Source {src} not found!")

if __name__ == "__main__":
    main()
