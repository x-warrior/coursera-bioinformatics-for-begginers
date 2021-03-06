def count(motifs):
    h = {'A': [], 'C': [], 'G': [], 'T': []}
    size = len(motifs[0])
    for c in range(0, size):
        for k in h.keys():
            h[k].append(0)

    for motif in motifs:
        for c in range(size):
            h[motif[c]][c] = h[motif[c]][c] + 1

    return h


def profile(motifs):
    c = count(motifs)
    size = len(motifs)
    for k in c.keys():
        c[k] = list(map(lambda v: float(v)/float(size), c[k]))
    return c



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(profile(sys.stdin.read().splitlines()))