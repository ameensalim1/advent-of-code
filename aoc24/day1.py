# distance between left and right lists
from collections import Counter

def read_input(filename):
    left = []
    right = []
    
    with open(filename) as f:
        for line in f:
            # Split on whitespace and convert to integers
            l, r = map(int, line.strip().split())
            left.append(l)
            right.append(r)
            
    return left, right

def distance(left, right):
    left.sort()
    right.sort()
    
    total_distance = 0
    for i in range(len(left)):
        currmax = max(left[i], right[i])
        currmin = min(left[i],right[i])

        distance = currmax - currmin
        total_distance += distance

    

    return total_distance

def similarity(left, right):
    similarity_score = 0
    counts = Counter(right)
    for l in left:
        temp = l * counts[l]
        similarity_score += temp
    
    print(similarity_score)


left, right = read_input("aocday1.txt")
output = distance(left, right)
similarity(left, right)

