
'''
    Write function called best_list_pureness which will receive a list of numbers
    and a number K. You have to rotate the list K times (last becomes first) to find
    the variation of the list with the best pureness
    (pureness is calculated by summing all the elements in the list multiplied by their indices).
    For example, in the list [4, 3, 2, 6] with the best pureness is
    (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26.
    At the end the function should return a string containing the highest pureness
    and the amount of rotations that were made to find this pureness
    in the following format: "Best pureness {pureness_value} after {count_rotations} rotations".
    If there is more than one highest pureness, take the first one.
'''

def best_list_pureness(nums, k):
    numbers = [int(i) for i in nums]
    list_pureness = []

    if k > 0:
        for _ in range(k):
            pureness = 0    # pureness must be reset for each run

            # calculate pureness
            for n in numbers:
                recalculate_pureness = n * numbers.index(n)
                pureness += recalculate_pureness

            list_pureness.append(pureness)

            # proceed to the next rotation
            num = numbers.pop()
            numbers.insert(0, num)

        best_pureness = max(list_pureness)
        num_rotations = list_pureness.index(best_pureness)

        return f'Best pureness {best_pureness} after {num_rotations} rotations'
    else:
        return f'Best pureness {0} after {0} rotations'


test = ([4, 3, 2, 6], 0)
#test = ([7, 9, 2, 5, 3, 4], 3)
#test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
