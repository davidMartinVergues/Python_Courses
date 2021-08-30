# el binary searc solo sirve con una lista ordenada

def run():
    sequence = [1,2,3,4,5,6,7,8,9,10,11]

    print(binary_search(sequence,-5))


def binary_search(list,goal,start=None,end=None):
    
    if start is None:
        start = 0
    if end is None:
        end = len(list)-1
    
    midpoint = (start + end)//2

    if end < start:
        return -1 
    elif list[midpoint] == goal:
        return midpoint
    elif list[midpoint] > goal:
        return binary_search(list,goal,start,midpoint-1)
    else:
        return binary_search(list,goal,midpoint+1,end)
   

if __name__ == "__main__":
    run()





