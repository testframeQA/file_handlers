import os
import chardet
import difflib
import argparse

def read_file(file_path):
    """
    Reads a file and returns its content as a list of lines.
    Attempts to detect encoding if it's not UTF-8.
    """
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            encoding = chardet.detect(raw_data)['encoding']

        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
        return lines

    except FileNotFoundError:
        print(f"Error: File Not Found At - {file_path}")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        exit(1)
        
def ensure_directory_exists(file_path):
    """
    Checks if the directory for the specified file path exists, and creates it if missing
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def compare_files(file_1, file_2, output_file='./diff_output.txt'):
    """
    Compares two files and writes the differences to a specified output file
    """
    file_1_lines = read_file(file_1)
    file_2_lines = read_file(file_2)
    
    diff = difflib.unified_diff(
        file_1_lines,
        file_2_lines,
        fromfile=file_1,
        tofile=file_2,
        lineterm=''
    )
    ensure_directory_exists(output_file)
    differences = list(diff)
    with open(output_file, 'w') as output:
        if differences:
            output.write("Differences between files:\n" + "-" * 40 + "\n")
            for line in differences:
                output.write(line + '\n')
            print(f"Differences written to {output_file}")
        else:
            output.write("No differences found")
            print("No differences found between files")

def main():
    """
    Main function to parse arguments and call file comparison function
    """
    parser = argparse.ArgumentParser(description="Compare two files for differences")
    parser.add_argument("file_1", help="Path to the first file")
    parser.add_argument("file_2", help="Path to the second file")
    parser.add_argument(
        "-o", "--output", 
        help="Specify an output file to write differences (default: diff_output.txt)", 
        default="./diff_output.txt"
    )

    args = parser.parse_args()

    compare_files(args.file_1, args.file_2, args.output)

if __name__ == "__main__":
    main()