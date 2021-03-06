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


def consensus(motifs):
    p = profile(motifs)
    size = len(motifs[0])
    s = ""
    for i in range(size):
        picked = None
        val = 0
        for c in 'ACGT':
            if p[c][i] > val:
                picked = c
                val = p[c][i]
        s = s + picked
    return s

def score(motifs):
    cons = consensus(motifs)
    score = 0
    size = len(motifs[0])
    for motif in motifs:
        for i in range(size):
            if motif[i] != cons[i]:
                score = score + 1
    return score


def pr(text, pro):
    prob = 1
    for i in range(len(text)):
        prob = float(prob) * float(pro[text[i]][i])
    return prob


def pmpp(text, k, profile):
    prob = -1
    ppt = None
    for i in range(len(text)-k+1):
        pt = text[i:i + k]
        mp = pr(pt, profile)
        if mp > prob:
            prob = mp
            ppt = pt
    return ppt


def gms(dna, k, t):
    best_motifs = []
    for line in dna:
        best_motifs.append(line[0:k])

    size = len(dna[0])
    for i in range(size-k+1):
        motifs = []
        motifs.append(dna[0][i:i+k])
        for j in range(1, t):
            p = profile(motifs[0:j])
            motifs.append(pmpp(dna[j], k, p))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
k,t = lines[0].split()
k = int(k)
t = int(t)
print('\n'.join(gms(lines[1:],k,t)))