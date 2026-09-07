import numpy as np


def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    a = np.array(a)
    b = np.array(b)

    if a.shape[1] == b.shape[0]:
        answer=np.array([])
        for row in a:
            answer=np.append(answer,np.dot(row,b))
        return answer
    else:
        return -1


