def shuffle_array(nums, n):
    first_half = nums[:n]
    second_half = nums[n:]

    result = []

    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    return result


# Test 
test_cases = [([2, 5, 1, 3, 4, 7], 3), ([1, 2, 3, 4, 4, 3, 2, 1], 4), ([1, 1, 2, 2], 2)]

for nums, n in test_cases:
    print("Original: " + str(nums))
    print("n = " + str(n))
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()
