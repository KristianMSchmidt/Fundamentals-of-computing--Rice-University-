import random
x=random.randrange(1,6)

print 51*26
import math
print math.pi

def combine(outcomes, length):
    """
    Takes a list of outcomes and returns a tuple of all tuples of combinations of given
    length.
    """
    ans=[[]]
    for dummy_index in range(length):
        temp=[]
        for seq in ans:
            for outcome in outcomes:
                new_seq=list(seq)
                new_seq.append(outcome)
                temp.append(tuple(new_seq))
               #print temp
        ans=temp
    return tuple(ans)

#a=combine([3,4,7],3)
#print a
#print ""
#sorted_sequences = [tuple(sorted(sequence)) for sequence in a]
#print set(sorted_sequences)
