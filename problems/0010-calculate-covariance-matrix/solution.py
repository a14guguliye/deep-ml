import numpy as np 

def calculate_mean(vectors:list[float])->float:
    S=0;

    for val in vectors:
        S=S+val

    return S/len(vectors)


def calculate_covariance(vector1:list[float], vector2:list[float])->float:
    mean_vector_1=calculate_mean(vector1)
    mean_vector_2=calculate_mean(vector2)
    S=0
    for val1, val2, in zip(vector1, vector2):
       S=S+(val1-mean_vector_1)*(val2-mean_vector_2)

    return S/(len(vector1)-1)
        
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	vectors = np.array(vectors)
	result_array=np.zeros(((vectors.shape[0]), (vectors.shape[0])))

	for i in range(result_array.shape[0]):
		for j in range(result_array.shape[1]):
				result_array[i][j]=calculate_covariance(vectors[i],vectors[j])
	return result_array
				