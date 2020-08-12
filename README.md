# About Snakemake

[Snakemake](https://snakemake.readthedocs.io/en/stable/) is a Pythonic workflow engine developed by Johannes Köster. It has gained popularity for its concise syntax and robust execution. 

# About the Presenter

Dr. David Koppstein is a researcher at the Berlin Institute of Medical Systems Biology and a graduate of MIT. Although originally trained as a wet lab biologist, he is also enthusiastic about Python and reproducible research. 

# Setup

To setup a minimal snakemake environment, first install Miniconda with Bioconda channels by following the instructions [here](https://bioconda.github.io/user/install.html). 

Then, run 

```
conda create -n ngstutorial -c bioconda snakemake
```

# Exercises

Minimal examples corresponding to the slides can be found in the exercises folder. To run them, use: 


```
conda activate ngstutorial
snakemake -printshellcmds -- all
```

For dummy rules, run them using the `-n` flag. 

For rules with wrappers, use `--use-conda`. 
