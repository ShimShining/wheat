# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/27
Describe:
"""


class InsertionSort:
    def sort(self, data):
        for i in range(1, len(data)):
            value = data[i]
            j = i - 1
            while j >= 0 and data[j] > value:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = value




if __name__ == '__main__':
    insertion_sort = InsertionSort()
    data = [5, 2, 1, 4, 10, 3, 6, 7]
    insertion_sort.sort(data)
    assert data == [1, 2, 3, 4, 5, 6, 7, 10]
