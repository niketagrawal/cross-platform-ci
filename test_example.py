# code to add two lists

import os
import sys
def add_lists(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    return list3

def test_add_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = add_lists(list1, list2)
    assert list3 == [5, 7, 9]
