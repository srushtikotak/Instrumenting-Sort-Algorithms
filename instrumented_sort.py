"""
CSCI-603: LAB 5 (week 5)
Authors: Srushti Kotak

"""

# Global variable for keeping count of comparisons
comparison = 0


def ssort(data):
    """
    The ssort(data) function : Implements selection sort on data
    :param data: list to be sorted
    :return: data - sorted list
    :return comparison -  number of comparisons done
    """
    comparison = 0
    for i in range(len(data)-1):
        # i is the number of elements sorted so far
        # thus, i is the index where we will put the next one
        for j in range(i+1, len(data)):
            comparison = comparison + 1
            if data[i] > data[j]:
                # now swap the min value into slot i
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
    return data, comparison


def msort(data):
    """
    The msort(data) function : Implements merge sort on data
    :param data: list to be sorted
    :return: data - sorted list
    :return comparison -  number of comparisons done
    """
    global comparison
    if len(data) == 1:
        return data, comparison
    else:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        msort(left)
        msort(right)
        # zip 'em up
        leftindex = rightindex = index = 0
        while leftindex < len(left) and rightindex < len(right):
            comparison = comparison + 1
            if left[leftindex] < right[rightindex]:
                data[index] = left[leftindex]
                leftindex = leftindex + 1
            else:
                data[index] = right[rightindex]
                rightindex = rightindex + 1
            index = index + 1
        # one array is used up
        while leftindex < len(left):
            data[index] = left[leftindex]
            index = index + 1
            leftindex = leftindex + 1

        while rightindex < len(right):
            data[index] = right[rightindex]
            index = index + 1
            rightindex = rightindex + 1

        return data, comparison
