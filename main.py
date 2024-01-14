import argparse
from pathlib import Path
import shutil

def parse_argv():
    parser = argparse.ArgumentParser(description = "Copy file in folder")
    parser.add_argument("-s", "--source", type = Path, required = True)
    parser.add_argument("-o", "--output", type = Path, default = Path("dist"))
    return parser.parse_args()


def recursive_copy(source, output):
    for elem in source.iterdir():
        if elem.is_dir():
            recursive_copy(elem, output)
        else:
            folder = elem.name.split('.')[-1]
            folder = output / folder
            folder.mkdir(exist_ok = True, parents = True)
            shutil.copy(elem, folder)


def main():
    args = parse_argv()
    print(args)
    recursive_copy(args.source, args.output)
    print("Done")




if __name__ == '__main__':
    main()