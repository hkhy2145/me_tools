def remove_duplicates(input_file, output_file):
    # Create a set to store unique lines
    unique_lines = set()

    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Read each line from the input file
        lines = file.readlines()

        # Iterate through the lines
        for line in lines:
            # Add the line to the set if it's not already there (removing duplicates)
            unique_lines.add(line)

    # Open the output file for writing
    with open(output_file, 'w') as file:
        # Write the unique lines back to the output file
        for line in unique_lines:
            file.write(line)

# Usage
input_file = 'parmter.txt'
output_file = 'dparmter.txt'

remove_duplicates(input_file, output_file)

