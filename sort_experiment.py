"""
CSCI-603: LAB 5 (week 5)
Authors: Srushti Kotak

"""

import instrumented_sort
import random
import sys
import time


def generate_data(N):
    """
    The generate_data generates a list of random N numbers
    :param N : number of elements in list
    :return numbers - list of random numbers
    """
    numbers = list(range(N))
    random.shuffle(numbers)
    return numbers


def check_sorted(data):
    """
    Checks if the numbers in data are sorted or not
    :param data
    :return True if numbers are in ascending order else false
    """
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            return False
    return True


def main():
    """
    The main function
    """
    #
    number_of_numbers = sys.argv[1]
    N = [1, 10, 100, 1000, 10000]
    # creates observation.txt and writes the output in tabulated manner
    with open("observations.txt", "w+") as o:
        o.write("ALGORITHM" + "\t\t\t\tN" + "\t\tCOMPARISONS"
                + "\t\tSECONDS" + "\n")
        for n in range(int(number_of_numbers)):
            # generates random list of N[n] numbers
            data = generate_data(N[n])
            # records time before sorting
            before_time = time.time()
            ssorted_list = instrumented_sort.ssort(data)
            # records time after sorting
            after_time = time.time()
            ssort_time = (after_time - before_time)
            o.write("Selection Sort" + "\t\t" + str(N[n])
                    + "\t\t\t" + str(ssorted_list[1])
                    + "\t\t\t" + str(ssort_time) + "\n")
            # generates random list of N[n] numbers

            data = generate_data(N[n])
            # records time before sorting
            before_time = time.time()
            msorted_list = instrumented_sort.msort(data)
            # records time after sorting
            after_time = time.time()
            msort_time = (after_time - before_time)
            if check_sorted(ssorted_list[0]) is False or check_sorted(msorted_list[0]) is False:
                sys.exit("List not sorted")
            o.write("Merge Sort" + "\t\t\t\t" + str(N[n])
                    + "\t\t\t" + str(msorted_list[1]) + "\t\t\t" + str(msort_time) + "\n")


if __name__ == '__main__':
    main()
