#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

MELT = "/Applications/Shotcut.app/Contents/MacOS/melt"

#/Applications/Shotcut.app/Contents/MacOS/melt 01_intro.mlt -consumer avformat:foo.mp4 threads="0" top_field_first="2" target="foo.mp4" vcodec="libx264" rescale="bilinear" crf="23" f="mp4" channels="2" ab="384k" real_time="-1" g="300" movflags="+faststart" bf="3" deinterlace_method="yadif" acodec="aac" mlt_service="avformat" preset="fast" ar="48000"

RENDER_ARGS = {
    'threads':"0",
    'top_field_first':"2",
    'vcodec':"libx264",
    'rescale':"bilinear",
    'crf':"23",
    'f':"mp4",
    'channels':"2",
    'ab':"384k",
    'real_time':"-1",
    'g':"300",
    'movflags':"+faststart",
    'bf':"3",
    'deinterlace_method':"yadif",
    'acodec':"aac",
    'mlt_service':"avformat",
    'preset':"fast",
    'ar':"48000",
}


# ---------------------------------------------------------------------------

parser = argparse.ArgumentParser(description=("Runs melt command on Shotcut "
    "files"))

parser.add_argument('-r', action='store_true', help=('Recursively search for'
    '.mlt files to export'))

parser.add_argument('-o', type=str, default=None, help=('Output directory for '
    'rendering. Defaults to "_rendered" in the current directory'))

parser.add_argument('filenames', help=('.mlt files or directory containing '
    '.mlt files to render'), nargs="*")

if __name__ == '__main__':
    start = datetime.now()
    args = parser.parse_args()

    if not args.r and not args.filenames:
        parser.print_usage()
        quit()

    file_paths = []

    for name in args.filenames:
        path = Path(name)
        if path.is_dir():
            for subpath in path.rglob('*.mlt'):
                file_paths.append(subpath)
        else:
            file_paths.append(path)

    if args.r:
        for path in Path.cwd().rglob('*.mlt'):
            file_paths.append(path)

    for path in file_paths:
        print("**** Rendering", path)

        parms = [MELT, str(path), "-consumer", f"avformat:{path.stem}.mp4",]

        if args.o:
            parms.append(f'target="{args.o}"')
        else:
            parms.append(f'target="_rendered/{path.stem}.mp4"')

        for key, value in RENDER_ARGS.items():
            parms.append(f'{key}="{value}"')

        print(parms)
        subprocess.run(parms)

    finish = datetime.now()
    print(f"\n\nFinished at: {finish} took {finish-start}")
