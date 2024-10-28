import argparse

def split_file(input_file, number_of_subfiles):
    """
    Splits parent file into n number of subfiles determined by user at command line
    """
    filename_with_extension = input_file.split('/')[-1]
    base_name = filename_with_extension.rsplit('.txt', 1)[0]

    with open(input_file, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    lines_per_part = total_lines // number_of_subfiles
    extra_lines = total_lines % number_of_subfiles

    start_index = 0

    for part in range(number_of_subfiles):
        extra_line = 1 if part < extra_lines else 0
        end_index = start_index + lines_per_part + extra_line

        part_file_name = f'./test_data/split_files/{base_name}_{part + 1}.txt'
        with open(part_file_name, 'w') as part_file:
            part_file.writelines(lines[start_index:end_index])
        start_index = end_index

def main():
    """
    Main function to parse arguments, assign filetype variables, and call file splitter function
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input_file', help='Input File Name')
    parser.add_argument('-o', '--output_number', help='How Many Output Files to Generate')

    args = parser.parse_args()

    input_file = f'./test_data/{args.input_file}'
    split_number = f'{args.output_number}'
    number_of_subfiles = int(split_number)
    print(f'Input File: {input_file}')
    print(f'Number of Parts: {number_of_subfiles}')
    print(f'Splitting {input_file} into {number_of_subfiles} parts...')
    split_file(input_file, number_of_subfiles)

if __name__ == "__main__":
    main()
