import numpy as np
from numpy.linalg import inv
from numpy.linalg import LinAlgError

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	try:
		Tinv=inv(T)
		Sinv=inv(S)
	except LinAlgError:
		return -1 
	
	transformed_matrix = Tinv @ A @ S
	
	return transformed_matrix