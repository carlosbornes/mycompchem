# MyCompChemistry
This repository contains scripts I've written over the years to make my computational chemistry workflows a bit more manageable. Since I suck at coding, some might be overly complicated but they work for me. But of course, if you have any suggestions on how to improve them go ahead.

While the main point of this repository is that I don’t lose my scripts (which happens more often than I like to admit 🤦), feel free to use them at your own risk.

I will try to include some descriptions about how to use them, but if any questions remain feel free to contact me.

# Scripts
## conv2x
A simple script that takes advantage of [Atomic Simulation Environment](https://wiki.fysik.dtu.dk/ase/) capabilities to read a geometry optimization trajectory, extract the last step and convert it to a specific file type. See [ASE’s supported codes](https://wiki.fysik.dtu.dk/ase/ase/io/io.html).

In a conventional workflow, I use this script to extract the converged structure from a CP2K calculation and write a CASTEP cell file, by doing something like this:

```
conv2x.py cp2k_output.pdb castep_input.cell
```


