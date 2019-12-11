from random import randint, choice


def inject_errors(seq_read, error_frequency):
    no_of_replacements = int(len(seq_read) * error_frequency)
    seq_read_list = [base for base in seq_read]

    possible_replacements = ['a', 'g', 'c', 't']
    replaced_indices = []

    while no_of_replacements > 0:
        replace_index = 0
        while replace_index in replaced_indices:
            replace_index = randint(0, len(seq_read_list) - 1)

        replaced_indices.append(replace_index)

        # Random base (other than original) replaces original base in list
        possible_replacements.remove(seq_read_list[replace_index])

        seq_read_list[replace_index] = choice(possible_replacements)
        no_of_replacements -= 1

    seq_read = "".join(seq_read_list)
    return seq_read

def gen_debruijn_graph(seq_read_with_error, k):

    nodes = set()
    edges = []
    g = {'nodes': nodes, 'edges': edges}
    print(seq_read_with_error)
    print(k)

    for i in range(len(seq_read_with_error) - k + 1):
        km1_left = seq_read_with_error[i : (i + (k-1))]
        km1_right = seq_read_with_error[(i + 1) : (i + k)]
        g['edges'].append((km1_left, km1_right))
        g['nodes'].add(km1_left)
        g['nodes'].add(km1_right)

    return g

def eulerian_walk(g):
    print(g)
    reconstructed_sequence = g['edges'][0][0]
    for e in g['edges']:
        reconstructed_sequence += e[1][-1]

    return reconstructed_sequence

def calc_score(assembled_seq, seq_read):

    min_seq_length = min(len(assembled_seq), len(seq_read))
    no_of_matches = 0

    for index in range(min_seq_length):

        if assembled_seq[index] == seq_read[index]:
            no_of_matches += 1

        tail_cost = (len(assembled_seq) - len(seq_read)) / len(seq_read)
        no_of_matches = max(0, (no_of_matches - int(tail_cost)))

        if (min_seq_length == 0):
            score = 0.0
        else:
            score = float(no_of_matches / min_seq_length)

    return score


def compute_accuracy(seq, read_length, k, error_frequency):

    seq_read = seq[:read_length]
    seq_read_with_error = inject_errors(seq_read, error_frequency)

    g = gen_debruijn_graph(seq_read_with_error, k)

    assembled_seq = eulerian_walk(g)

    variance = calc_score(assembled_seq, seq_read)

    return variance

