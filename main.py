import os
import shutil
from pathlib import Path


def main():
    src = Path(os.environ.get('MAKEFUN_BOT_DIR', '.')) / 'entry.png'

    # fallback: writes to ./out if /output is unavailable
    output_dir = Path('/output')
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        test_file = output_dir / '.test_write'
        test_file.touch()
        test_file.unlink()
    except OSError:
        output_dir = Path('./out')
        output_dir.mkdir(parents=True, exist_ok=True)

    dst = output_dir / 'entry.png'

    if src.exists():
        shutil.copy(src, dst)


if __name__ == '__main__':
    main()
