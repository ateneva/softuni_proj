
# ---------------------problem 6: longest intersection-------------------------

'''
Write a program that finds the longest intersection.
You will be given a number N. On the next N lines you will be given two
ranges in the format: "{first_start},{first_end}-{second_start},{second_end}".
Find the intersection of these two ranges and save the longest one of all N intersections.

At the end print the numbers that are included in the longest intersection and
its length in the format:
 "Longest intersection is {longest_intersection} with length {length_longest_intersection}"

Note: in each range, there will always be intersection.
If there are two equal intersections, print the first one
'''

N = int(input())
longest_intersection = ''

for n in range(N):
    line = input().split('-')
    a = [int(i) for i in line[0].split(',')]
    b = [int(i) for i in line[1].split(',')]
    #print(a, b)

    set_a = set([i for i in range(a[0], a[1]+1)])
    set_b = set([j for j in range(b[0], b[1]+1)])
    intersection = list(set_a & set_b)

    #print(intersection)
    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection

print(f'Longest intersection is {longest_intersection} '
        f'with length {len(longest_intersection)}')
