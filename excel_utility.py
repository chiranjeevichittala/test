import argparse
import sys
import pandas as pd


def file_read_utility(args):
    if args.file_path is not None:
        loc = args.file_path
        reader = pd.read_excel(loc, engine='openpyxl')
        # print(f"These are Columns in Excel: {reader.columns}")
        # print(reader['Name'][0])
        # for i in reader:
        #     print(i)
        return reader


if __name__ == '__main__':
    print(sys.argv[1])
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file_path', help="This will read Excel file")

    args = arg_parser.parse_args()
    sys.stdout.write(str(file_read_utility(args)))
