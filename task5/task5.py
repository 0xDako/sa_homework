import json
import ast
import numpy as np


def task(rank1_str: str, rank2_str: str) -> str:
    r1 = json.loads(rank1_str)
    r2 = json.loads(rank2_str)

    y_a = matrix(r1)
    y_a_t = y_a.transpose()

    y_b = matrix(r2)
    y_b_t = y_b.transpose()

    y_a_b = np.multiply(y_a, y_b)
    y_a_b_t = np.multiply(y_a_t, y_b_t)

    conflicts = []

    for i in range(y_a_b.shape[0]):
        for j in range(y_a_b[i].shape[1]):
            if int(y_a_b[i, j]) == 0 and int(y_a_b_t[i, j]) == 0:
                if [str(j+1), str(i+1)] not in conflicts:
                    conflicts.append([str(i+1), str(j+1)])

    return conflicts


def matrix(rank):
    ranks=dict()
    rlen=rlength(rank)
    for i, rank in enumerate(rank):
        if type(rank) is str:
            ranks[int(rank)]=i
        else:
            for r in rank:
                ranks[int(r)]=i

    return np.matrix([[1 if ranks[i+1] <= ranks[j+1] else 0 for j in range(rlen)] for i in range(rlen)])

def rlength(ranking) -> int:
    l=0
    for i in ranking:
        if type(i) is str:
            l += 1
        else:
            l += len(i)
    return l


