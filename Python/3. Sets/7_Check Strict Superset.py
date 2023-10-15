# You are given a set A and n other sets.Your job is to find whether A set is a strict superset of each 
# of the n sets. Print True, if A is a strict superset of each of the n sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset. 

def isSuperset(A, n):
    for i in range(n):
        B = set(map(int, input().split()))
        if not A.issuperset(B):
            return False
    return True

if __name__ == '__main__':
    A = set(map(int, input().split()))
    n = int(input())
    print(isSuperset(A, n))