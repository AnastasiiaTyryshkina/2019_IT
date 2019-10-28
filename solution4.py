import numpy as np
import matplotlib.pyplot as plt


def pareto(ind, X):
    for i, element in enumerate(X):
        if i != ind and not np.any(element < X[ind:]):
            return False
    return True

def pareto_indicator(X)
	pareto_el=[]
	not_el=[]
	for ind in range(X.shape[0]):
        if is_pareto(ind, X):
            pareto_el.append(ind)
        else:
            not_el.append(ind)
    return pareto_el, not_el

if __name__ == "__main__":

    m = 3
    n = 7
    sp = 100
    X = np.trunc(np.random.rand(n, m)*sp)
	indpareto, indnot = pareto_indicator(X)
	X = np.append(X, np.reshape(X[:, 0], (n, 1)), axis=1)

    vec_pareto, vec_not_pareto = X[indpareto, :], X[indnot, :]
    per = 2 * np.pi * np.arange(m + 1, dtype=int) / m

    _, axes = plt.subplots(ncols=3, subplot_kw=dict(polar=True))

    for ax in axes:
        ax.set_rmax(sp)
        ax.set_thetagrids(np.arange(0, 360, 360 / m), labels=(np.arange(m) + 1))
        ax.grid(True)

    axes[0].set_title('Pareto front')
    for vec in vec_pareto:
        axes[0].plot(per, vec)

    axes[1].set_title('Not Pareto vectors')
    for vec in vec_not_pareto:
        axes[1].plot(per, vec)
	axes[2].set_title('All vectors')
    for vec in X:
        axes[2].plot(per, vec)
		
    plt.show()