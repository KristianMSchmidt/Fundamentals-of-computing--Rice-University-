
def g(n):
    count = 0
    while n>0:
        count +=1
        n -= 1
    return count

#print g(10**9)

print (3*10**9)/float(63)




# count = 0
# def f(sorted_list, l, r):
#     global count
#     count += 1
#
#     #print "count", count
#     #print "l:",l
#     #print "r:", r
#     if l > r:
#         return -1
#
#     m = (l+r) / 2
#     #print "m:", m
#     #print "A[m]", sorted_list[m]
#     if sorted_list[m] == m:
#         return m
#
#     if sorted_list[m]<m:
#         return f(sorted_list, m + 1, r)
#
#     else:
#         return f(sorted_list, l, m - 1)
#
# example = [n+1 for n in range(2**20)]
# example[0]=0
# left = 0
# right = len(example)-1
# #print "right", right
# print "RESULT:", f(example, left, right)
# print count
