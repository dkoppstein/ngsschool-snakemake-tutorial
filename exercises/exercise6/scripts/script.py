import sys

with open(snakemake.output[0], "w") as outh:
    for handle in (outh, sys.stderr):
        print("I am processing file {}".format(snakemake.wildcards.sample), file=handle)
