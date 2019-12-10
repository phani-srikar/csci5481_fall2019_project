import random

def sequence_genome(seq):

    fragments = make_fragments(seq)
    assembled_sequence = assemble_fragments(fragments)
    return assembled_sequence

def make_fragments(seq):

    # remaining nucleotides that are not
    # covered by substrings
    remaining_indices = list(range(len(seq)))

    # length of substrings
    #len_substring = random.randrange(100, 1001)
    len_substring = 1000

    # represents direction of read
    direction = ["Forward", "Backward"]

    # list of random substrings
    substrings = []

    while len(remaining_indices) != 0:
        # find random start index
        start = remaining_indices[random.randrange(len(remaining_indices))]

        # Picks random read dirction
        read_direction = direction[random.randrange(2)]

        # Checks to make sure start index +- len_substring is valid
        # After this check we will always read forward starting at start
        if (read_direction == "Backward"):
            start -= len_substring
            if start < 0:
                start = 0
        else:
            if start + len_substring >= len(seq):
                start -= len_substring + 1

        # Added random overlapping shotgun sequence
        substrings.append(seq[start:start+len_substring])

        # remove covered indices from remaining indeces
        for i in range(start, start+len_substring+1):

            for x in remaining_indices:
                if x == i:
                    remaining_indices.remove(i)

    return substrings

def assemble_fragments(substrings):
    s = substrings[0]
    del substrings[0]

    while len(substrings) > 0:

        # stores best matching remaining
        # substring to stich, length
        # of overlap, side to attach to s
        best_match = [0, 0, "start"]

        index_of_sub = 0
        for o in substrings:
            for i in range(len(o) - 1):
                start = o[:-(i + 1)]
                end = o[(i + 1):]
                if s.endswith(start):
                    if best_match[1] < len(start):
                        best_match = [index_of_sub, len(start), "start"]

                if s.startswith(end):
                    if best_match[1] < len(end):
                        best_match = [index_of_sub, len(end), "end"]

            index_of_sub += 1

        # stitch the best matching string to beggining or end
        # of s
        if best_match[2] == "start":
            s += substrings[best_match[0]][best_match[1]:]
            del substrings[best_match[0]]
        else:
            s = substrings[best_match[0]][:-best_match[1]] + s
            del substrings[best_match[0]]

    return s
