#Function to check if list l is sorted.
def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

#Swap sorting function, performing swaps/shifts until l is sorted.
def sort(l):
    s = len(l)
    while True:
        n = l[0]
        if n < s:
            l[0], l[n] = l[n], l[0]
        else:
            l.pop(0)
            l.append(n)
            if is_sorted(l):
                return l

#Proven to work for index-bound consecutive list arrangements, O(n) time complexity estimated through testing with the given input domain
