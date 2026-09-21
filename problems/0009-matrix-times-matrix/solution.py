def multiply_vectors(a:list[list[int|float]], b:list[list[int|float]]):
    return sum(el1*el2 for el1, el2 in zip(a,b)); 


def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]]):
   
    momentary_list=[]
    c=[]

    if(len(a[0])==len(b)):
        for row_index, el in enumerate(a):
            c.append([])
            for col_index_b in range(len(b[0])):
                for i in range(len(b)):
                    momentary_list.append(b[i][col_index_b])
                c[row_index].append(multiply_vectors(el,momentary_list))
                momentary_list=[]
    else:
        return -1

    return c

            
            
        
        
        


print(matrixmul([[1,2],[2,4]], [[2,1],[3,4]]))


    
	
