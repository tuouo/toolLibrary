# ！/usr/bin/env/python3
# -*- coding: utf-8 -*-
import unittest


def search(arr, target):
    return bin_search_left2(arr, target, 0, len(arr) - 1)


def bin_search_left(arr, target, left, right):
    end = right
    while left <= right:
        mid = (right + left) // 2
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if left > end or arr[left] != target:
        return - left - 1
    return left


def bin_search_left2(arr, target, start, end):
    left, right = start - 1, end + 1
    while left + 1 != right:
        mid = left + ((right - left) >> 1)
        if target > arr[mid]:
            left = mid
        else:
            right = mid
    if right > end or arr[right] != target:
        return - right - 1
    return right


def bin_search_right(arr, target, start, end):
    left, right = start - 1, end + 1
    while left + 1 != right:
        mid = left + ((right - left) >> 1)
        if target < arr[mid]:
            right = mid
        else:
            left = mid
    if left < start or arr[left] != target:
        return - left - 2
    return left


class Search(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]

    def test_insert(self):
        self.assertEqual(search(self.arr, 2), -1)
        self.assertEqual(search(self.arr, 3), 0)
        self.assertEqual(search(self.arr, 4), -2)
        self.assertEqual(search(self.arr, 5), 1)
        # self.assertEqual(search(self.arr, 5), 11)
        self.assertEqual(search(self.arr, 6), -13)
        self.assertEqual(search(self.arr, 7), 12)
        self.assertEqual(search(self.arr, 8), -14)


def test_bin_search_left(arr, target):
    bin_search_left(arr, target, 0, len(arr))


def test_bin_search_left2(arr, target):
    bin_search_left2(arr, target, 0, len(arr))


if __name__ == '__main__':
    # unittest.main()
    import timeit
    print("start")
    print(timeit.timeit("test_bin_search_left()", setup="from __main__ import test_bin_search_left"))
    print(timeit.timeit("test_bin_search_left2()", setup="from __main__ import test_bin_search_left2"))