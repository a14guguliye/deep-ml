import  numpy as np
from numpy.linalg import LinAlgError

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    
    try:
        return np.linalg.inv(matrix)
    
    except LinAlgError:
        return None
    pass