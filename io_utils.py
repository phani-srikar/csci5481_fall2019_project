import pandas as pd

## Read in the Sequence from input file
def read_sequence(filepath):
    input_sequence = ""
    with open(filepath) as f:
        for line in f:
            if line[0] == '>':
                continue
            else:
                input_sequence += line.replace('\n', '')

    return str.lower(input_sequence)


def store_list(l, file_name, colnames):
    df = pd.DataFrame(l, columns = colnames)
    df.to_csv(file_name, index = False)
