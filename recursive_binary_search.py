def binary_search(int_array, lower, upper, target, NOT_IN_ARRAY, ARRAY_UNORDERED, LIMITS_REVERSED):
    range = upper - lower
    if range < 0:
        return LIMITS_REVERSED
    elif range == 0 and int_array[lower] != target:
        return NOT_IN_ARRAY

    if int_array[int(lower)] > int_array[int(upper)]:
        return ARRAY_UNORDERED

    centre = (range / 2) + lower
    print("target = " + str(target) + ", centre = " + str(centre))
    if target == int_array[int(centre)]:
        print("centre is at index " + str(int(centre)))
        return centre
    elif target < int_array[int(centre)]:
        return binary_search(int_array, lower, centre - 1, target,
                                  NOT_IN_ARRAY, ARRAY_UNORDERED, LIMITS_REVERSED)
    else:
        return binary_search(int_array, centre - 1, upper, target,
                                  NOT_IN_ARRAY, ARRAY_UNORDERED, LIMITS_REVERSED)

NOT_IN_ARRAY = -1;
ARRAY_UNORDERED = -2;
LIMITS_REVERSED = -3;
int_array = [1, 2, 5, 7, 12, 24, 36, 55, 64, 99, 1024]
binary_search(int_array, 0, len(int_array)-1, 55, NOT_IN_ARRAY, ARRAY_UNORDERED, LIMITS_REVERSED)