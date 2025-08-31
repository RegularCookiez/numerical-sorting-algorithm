#Function to check if list l is sorted.
def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

#Numerical sorting function, performing shifts until l is sorted.
def sort(l):
    s = len(l)
    while True:
        n = l[0]
        if n < s:
            l.insert(n+1, n)
            l.pop(0)
        else:
            l.insert(s, n)
            l.pop(0)
            if is_sorted(l):
                return l

#Works for index-bound arrangements of consecutive lists (1 to |L|), unproven for non index-bound
#Time complexity of around O(k^n) where k is the smallest number in the list
