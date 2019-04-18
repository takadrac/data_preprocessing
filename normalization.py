import numpy as np

def normalization(max, min, a):
    scale = max - min
    a = (np.array(a) - min) / scale
    return a

test = np.array([np.array(range(5)), np.array(range(6,11)), np.array(range(100))])
maxes = [10, 11, 200]
mins = [0, 6, 0]
def main(test):
    norm_test = []
    for i, elem in enumerate(test):
        norm_elem = normalization(maxes[i], mins[i], elem)
        norm_test.append(norm_elem)
    print(norm_test)

#TODO: max and min to normarize



if __name__ == "__main__":
    main(test)