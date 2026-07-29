import numpy as np

def calculate(lists):

    if(len(lists)) !=9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(lists).reshape(3,3)

    calculation = {
        'mean': [matrix.mean(axis = 0).tolist(), matrix.mean(axis = 1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis = 0).tolist(), matrix.var(axis = 1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis = 0).tolist(), matrix.std(axis = 1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis = 0).tolist(), matrix.max(axis = 1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis = 0).tolist(), matrix.min(axis = 1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis = 0).tolist(), matrix.sum(axis = 1).tolist(), matrix.sum().tolist()]
        }
    
    return calculation

def main():
    lists = [1,2,3,4,5,6,7,8,9]
    result = calculate(lists)
    print(result)

if __name__ == "__main__":
    main()

