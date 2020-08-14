"""
Word Wrangler implementation by Philippe Malot for PoC-2
Some fancy stuff to look at at some point... is this clever or "clever"?
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"

# For slow computers
codeskulptor.set_timeout(600)


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if not list1:
        return list1
    new_list = [list1[0]]
    add_elem = new_list.append
    for val in list1:
        if val != new_list[-1]:
            add_elem(val)
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = []
    add_elem = new_list.append
    index = 0
    len1 = len(list1)
    len2 = len(list2)
    if len1 < len2:
        list1, list2 = list2, list1
        len2 = len1
    for val in list1:
        while index < len2 and list2[index] < val:
            index += 1
        if index < len2:
            if val == list2[index]:
                add_elem(val)
        else:
            break
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    if not list1 or not list2:
        return list1 + list2
    if list1[-1] > list2[-1]:
        loop, gen = list2, (val for val in list1)
    else:
        loop, gen = list1, (val for val in list2)
    merged = []
    add_elem = merged.append
    val = gen.next()
    for lvl in loop:
        while val < lvl:
            add_elem(val)
            val = gen.next()
        add_elem(lvl)
    add_elem(val)
    merged.extend(gen)
    return merged

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    mid = len(list1) / 2
    if mid:
        return merge(merge_sort(list1[:mid]), merge_sort(list1[mid:]))
    else:
        return list1



def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if not word:
        return [""]
    lst = gen_all_strings(word[1:])
    initial = word[0]
    new_strings = [gen_word[:pos] + initial + gen_word[pos:]
                   for gen_word in lst
                   for pos in range(len(gen_word) + 1)]
    lst.extend(new_strings)
    return lst


def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    net_file = urllib2.urlopen(codeskulptor.file2url(filename))
    return net_file.read().split('\n')

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

if __name__ == "__main__":
    run()
