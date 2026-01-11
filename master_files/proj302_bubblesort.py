# List of numbers
listx = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

list1 = [9, 6, 3, 25, 21, 8, 23, 1, 17, 14]

# Bubble Sort Algorithm
n = len(list1)
for i in range(n):
    # Each pass ensures the largest unsorted element is placed at the end
    for j in range(0, n - i - 1):
        # Swap if the element is greater than the next element
        if list1[j] > list1[j + 1]:
            # j + 1 here means the item to the right
            # essentially, you are comparing each item to the one on the right
            list1[j], list1[j + 1] = list1[j + 1], list1[j]


# Print the sorted list
print("Sorted List in Ascending Order:")
print(list1)
