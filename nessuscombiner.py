import xml.etree.ElementTree as ET
import glob
import os

def merge_nessus_files(input_directory, output_file_name):
    # Build the pattern for .nessus files in the specified directory
    pattern = os.path.join(input_directory, '*.nessus')
    input_files = glob.glob(pattern)
    
    first_file = True
    combined_root = None

    for filename in input_files:
        tree = ET.parse(filename)
        root = tree.getroot()

        if first_file:
            combined_root = root
            first_file = False
        else:
            for block in root:
                combined_root.append(block)

    if combined_root is not None:
        # Write the combined XML to a new file in the input directory
        combined_tree = ET.ElementTree(combined_root)
        output_file = os.path.join(input_directory, output_file_name)
        combined_tree.write(output_file)
        print(f'Merged files into {output_file}')
    else:
        print("No .nessus files found in the specified directory.")

# Example usage
input_directory = input("Enter the directory path containing .nessus files: ")
output_file_name = 'combined.nessus'
merge_nessus_files(input_directory, output_file_name)
