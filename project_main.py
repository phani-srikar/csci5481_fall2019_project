import collections
import sys, os
import argparse
from io_utils import *
from shotgun_utils import *
from tqdm import tqdm
from time import time
from kmer_utils import *


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

def generate_readlength_vs_accuracy(sequenced_genome):

    k = 50
    accuracy = []
    runtime = []

    for read_length in tqdm(range(100, 10000, 100)):
        start_time = time()

        accuracy = compute_accuracy(sequenced_genome, read_length, k, 0.01)
        runtime = time() - start_time

        accuracy.append((read_length, accuracy))
        runtime.append((read_length, runtime))

    store_list(accuracy, "readlength_accuracy.csv", ['reads', 'accuracy'])
    store_list(runtime, "readlength_runtime.csv", ['reads', 'runtime'])

def generate_k_vs_accuracy(sequenced_genome):

    read_length = 1000
    accuracy = []
    runtime = []
    for k in tqdm(range(3, 1000, 2)):
        start_time = time()
        accuracy = compute_accuracy(sequenced_genome, read_length, k, 0.01)
        runtime = time() - start_time

        accuracy.append((k, accuracy))
        runtime.append((k, runtime))

    store_list(accuracy, "k_accuracy.csv", ['k_size', 'accuracy'])
    store_list(runtime, "k_runtime.csv", ['k_size', 'runtime'])


if __name__ == '__main__':
    # parser = make_arg_parser()
    # args = parser.parse_args()
    # input_sequence = read_sequence(filepath=args.sequence)
    # sequenced_genome = sequence_genome(input_sequence)
    sequenced_genome = read_sequence("test1.fa")
    print(sequenced_genome)

    generate_readlength_vs_accuracy(sequenced_genome)
    generate_k_vs_accuracy(sequenced_genome)


