import argparse
import csv

def convert_file(origin_file, converted_file):
    """
    Converts target file to format defined by user at command line
    """
    with open(origin_file, 'r') as file:
        reader = csv.reader(file)
        with open(converted_file, 'w') as txt:
            for row in reader:
                txt.write(','.join(row) + '\n')

def main():
    """
    Main function to parse arguments, assign filetype variables, and call file convert function
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file_name', help='Input file name')
    parser.add_argument('-o', '--origin_file_type', help='Input file type')
    parser.add_argument('-c', '--convert_file_type', help='Input file type to convert to')

    args = parser.parse_args()

    origin_file_type = args.origin_file_type
    final_file_type = args.convert_file_type

    origin_file = f'../test_data/{args.file_name}.{origin_file_type}'
    converted_file = f'../test_data/{args.file_name}.{final_file_type}'

    convert_file(origin_file, converted_file)

if __name__ == "__main__":
    main()
