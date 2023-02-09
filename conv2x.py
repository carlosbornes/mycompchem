import sys
from ase.io import read, write

# Check if input and input files are provided 
if len(sys.argv) != 3:
    print('Please provide the input and output files: conv2x.py traj_file.ext input_file.ext.')
else:
    # Read name of the input file from the command line
    input_file = sys.argv[1]

    # Read name of the output file from the command line
    output_file = sys.argv[2]

    # Read trajectory from the input file
    traj = read(input_file, index = ':')

    # Select the last frame of the trajectory
    last = traj[-1]

    # Write the last frame to the output file
    write(output_file, last)
