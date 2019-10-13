import numpy as np

def get_indices(N, n_batches, split_ratio):
    inds = np.array([0, 0, 0])
    inds[0] = 0
    inds[2] = int((N - 1) / (1 + (split_ratio / (1 + split_ratio)) * (n_batches - 1)))
    inds[1] = int((1/(1+split_ratio)) * inds[2])
    raz = inds[2]-inds[1]
    yield inds
    for i in range(n_batches - 1):
        inds[0] += raz
        inds[1] += raz
        if (i==n_batches - 2): inds[2] = N - 1
        else: inds[2] += raz
        yield inds
def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
if __name__ == "__main__":
    main() 