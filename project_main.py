import collections
import sys, os
import argparse


def make_arg_parser():
    parser = argparse.ArgumentParser(prog='project_main.py',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--version', action='version', version='%prog 1.0')
    parser.add_argument("-i","--sequence",
                        default=argparse.SUPPRESS,
                        required=True,
                        help="Path to query fasta [required]")
    parser.add_argument("-k","--kmer_length",
                        default=argparse.SUPPRESS,
                        required=True,
                        help="Length of k-mer[required]")
    return parser


## Read in the Sequence from input file
def read_sequence(filepath):
    input_sequence = ""
    with open(filepath, 'r') as f:
        for line in f:
            if line[0] == '>':
                continue
            else:
                input_sequence += line.replace('\n', '')

    return str.lower(input_sequence)


if __name__ == '__main__':
    parser = make_arg_parser()
    args = parser.parse_args()
    input_sequence = read_sequence(filepath=args.sequence)

