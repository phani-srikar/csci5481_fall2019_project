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

    for i in range(len(seq_read_with_error) - k + 1):
        km1_left = seq_read_with_error[i : (i + (k-1))]
        km1_right = seq_read_with_error[(i + 1) : (i + k)]
        g['edges'].append((km1_left, km1_right))
        g['nodes'].add(km1_left)
        g['nodes'].add(km1_right)

    return g

def eulerian_walk(g):

    reconstructed_sequence = g['edges'][0][0]
    for e in g['edges']:
        reconstructed_sequence += e[1][-1]

    return reconstructed_sequence

def calc_score(assembled_seq, seq_read):

    return 0.0


def compute_accuracy(seq, read_length, k, error_frequency):

    seq_read = seq[:read_length]
    seq_read_with_error = inject_errors(seq_read, error_frequency)

    nodes, edges = gen_debruijn_graph(seq_read_with_error, k)

    assembled_seq = eulerian_walk(edges)

    variance = calc_score(assembled_seq, seq_read)

    return variance
