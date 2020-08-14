
#In this mini-project you should not use set, sorted, or sort.
#None of these functions should mutate their inputs. You must leave the inputs as they are and return new lists.

"""
Student code for Word Wrangler game
By Kristian Moeller Schmidt, Copenhagen, Denmark
"""

import urllib2
#import codeskulptor
#import poc_wrangler_provided as provided
#codeskulptor.set_timeout(60)

WORDFILE = "assets_scrabble_words3.txt"

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """

    # shortest solution (from instructor)
    return [x for i,x in enumerate(list1,-1) if x != list1[i] or i==-1]

    #the above does the same as the following. The got thing about this is that it is faster to build up
    #a new list, by appending from behind, than to iteratively remove elements from existing list, as this
    #required thousounds or rearrangements and reindixings.

    # i = -1
    # answer = []
    # for x in list1:
    #     if x! = list1[i] or i = -1:
    #         answer.append(x)
    #     i += 1

    #iterative solution
    # copy = list(list1)
    # for index in range(len(list1)-1):
    #     if list1[index] == list1[index+1]:
    #         copy.remove(list1[index])
    # return copy

    #recursive solution (This function should NOT be recursice... to deep for Python)
    # if len(list1) <= 1:
    #     return list1
    # else:
    #     first = list1[0]
    #     second = list1[1]
    #     all_but_first = list1[1:]
    #     if first == second:
    #         return remove_duplicates(all_but_first)
    #     else:
    #         return [first] + remove_duplicates(all_but_first)

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    #recursive solution
    # if list1 == [] or list2 == []:
    #     return []

    # else:
    #     first1 = list1[0]
    #     first2 = list2[0]

    #     if first1 == first2:
    #         return [first1] + intersect(list1[1:], list2[1:])

    #     elif first1 < first2:
    #         return intersect(list1[1:], list2)

    #     else:
    #         return intersect(list1, list2[1:])

    #iterative solution.... I try to avoid pop() as it is slow and unnecesarry

    new_list = []
    indx1 = 0
    indx2 = 0

    while indx1 < len(list1) and indx2 < len(list2):
        focus1 = list1[indx1]
        focus2 = list2[indx2]
        if focus1 == focus2:
            new_list.append(focus1)
            indx1 += 1
            indx2 += 1
        elif focus1 < focus2:
            indx1 += 1
        else:
            indx2 += 1
    return new_list

    #
    # #iterative solution (inefficient)
    # new_list = []
    # copy1 = list(list1)
    # copy2 = list(list2)
    # while copy1 != [] and copy2 != []:
    #     first1 = copy1[0]
    #     first2 = copy2[0]
    #     if first1 == first2:
    #         new_list.append(first1)
    #         copy1.pop(0)
    #         copy2.pop(0)
    #     elif first1 < first2:
    #         copy1.pop(0)
    #     elif first2 < first1:
    #         copy2.pop(0)
    # if copy1 == []:
    #     return new_list
    # else:
    #     return new_list


def merge(list1, list2):
    """
    Merge two sorted lists. (I suppose all elements should be preserved...)

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    Iteration: Each iteration of the loop compares the first element in each list, pops the smaller
    element from
    its containing list and appends this element to the answer

    This function can be written recursively, but better do it iterative, as it will call itself too many
    times when lists get long if resursive
     """

     #iterative solution. Rewritten to avoid to slow "pop" or "remove" list methods
    answer = []
    indx1 = 0
    indx2 = 0
    len1 = len(list1)
    len2 = len(list2)

    while indx1 < len1 and indx2 < len2:
         focus1 = list1[indx1]
         focus2 = list2[indx2]

         if focus1 <= focus2:
             answer.append(focus1)
             indx1 += 1
         else:
             answer.append(focus2)
             indx2 += 1

    if indx1 == len1:
         return answer + list2[indx2:]
    else:
         return answer + list1[indx1:]


    # answer = []
    # copy1 = list(list1)
    # copy2 = list(list2)
    #
    # while copy1 != [] and copy2 != []:
    #     first1 = copy1[0]
    #     first2 = copy2[0]
    #
    #     if first1 <= first2:
    #         answer.append(first1)
    #         copy1.pop(0)
    #
    #     else:
    #         answer.append(first2)
    #         copy2.pop(0)
    #
    # if copy1 == []:
    #     return answer + copy2
    #
    # if copy2 == []:
    #     return answer + copy1
    #

    #Resursive solution

        # if list1 == []:
        #     return list2
        # if list2 == []:
        #     return list1
        #
        # first1 = list1[0]
        # first2 = list2[0]
        #
        # if first1 == first2:
        #     return [first1] + merge(list1[1:], list2[1:])
        # if first1 < first2:
        #     return [first1] + merge(list1[1:], list2)
        # else:
        #     return [first2] + merge(list1, list2[1:])


def merge_sort(list1):
    """
    Sort the elements of list1. Use merge algortithn

    Return a new sorted list with the same elements as list1.

    This function should be recursive.

    Merge algorithm:Another part of this week's mini-project will be implementing a recursive sorting
    algorithm known as merge_sort. The basic idea behind merge_sort is to split the unordered input list
    of size n into two unordered sub-lists of approximately size n/2, recursively call merge_sort to sort
    each of these sublists and, finally, use merge to merge these two sorted sublists.

    """
    list_length = len(list1)

    if list_length <= 1:
        return list1

    else:
        list2 = list1[:list_length/2]
        list3 = list1[list_length/2:]

        return merge(merge_sort(list2), merge_sort(list3))


def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in a word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.

    Algorithm:
    1. Split the input word into two parts: the first character (first) and the remaining
    part (rest).
    2. Use gen_all_strings to generate all appropriate strings for rest
    . Call this list rest_strings.
    3. For each string in rest_strings, generate new strings by inserting the initial character, first,
    in all possible positions within the string.
    4. Return a list containing the strings in rest_strings as well as the new strings generated in step 3.
    return []
    """
    if word == "":
        return [""]

    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)

    new_strings = []

    for string in rest_strings:
        new_strings += [string[:pos] + first + string[pos:] for pos in range(len(string) + 1)]

    return rest_strings + new_strings


def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    netfile = urllib2.urlopen(filename)
    lines = netfile.readlines()
    clean_words = [line[:-1] for line in lines]
    return clean_words


def run():
    """
    Run game.
    """
    words = load_words("http://codeskulptor-assets.commondatastorage.googleapis.com/assets_scrabble_words3.txt")
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()
