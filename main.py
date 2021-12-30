import argparse
import json
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("-t", help="untuk mengkonversi logs menjadi file sesuai yang diinginkan",
                        type=str, default="text")
    parser.add_argument("-o", help="untuk menyimpan output sesuai direktori yang diinginkan", type=str,
                        default="")

    args = parser.parse_args()
    convert(args.file, args.t, args.o)

def convert(file_input, file, file_output):
    if file == "json":

        if file_output == "":
            file_output = os.environ.get("DEFAULT_DIR")+"error.json"
            print(file_output)
        dict1 = {}
        with open(file_input) as fh:
            for line in fh:
                command, description = line.strip().split(None, 1)
                dict1[command] = description.strip()
        out_file = open(file_output, "w")
        json.dump(dict1, out_file, indent=4, sort_keys=False)
        out_file.close()
    elif file == "text":
        print(file_input)
        if file_output == "":
            file_output = os.environ.get("DEFAULT_DIR")+"error.txt"
            print(file_output)
        with open(file_output, 'w', encoding='utf-8') as f:
            with open(file_input, "r") as r:
                f.write(r.read())


def line_to_dict(split_Line):
    line_dict = {}
    for part in split_Line:
        key, value = part.split(":", maxsplit=1)
        line_dict[key] = value

    return line_dict

if __name__ == '__main__':
    parser()
