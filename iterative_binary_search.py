def iter_binary_search(int_array, lower, upper, target, NOT_IN_ARRAY, ARRAY_UNORDERED, LIMITS_REVERSED):
    print("in iter_binary_search")

    if int_array[lower] > int_array[upper]:
        print("LIMITS_REVERSED")
        return LIMITS_REVERSED

    while True:
        range = upper - lower
        if range == 0 and int_array[lower] != target:
            print("NOT_IN_ARRAY")
            return NOT_IN_ARRAY

        if int_array[lower] > int_array[upper]:
            print("ARRAY_UNORDERED")
            return ARRAY_UNORDERED

        centre = int((range/2) + lower)
        print("target = " + str(target) + ", centre = " + str(centre))
        if target == int_array[centre]:
            print("centre is at index " + str(centre))
            return centre
        elif target < int_array[centre]:
            upper = centre-1
        else:
            lower = centre+1

NOT_IN_ARRAY = -1;
ARRAY_UNORDERED = -2;
LIMITS_REVERSED = -3;
int_array = [1, 2, 5, 7, 12, 24, 36, 55, 64, 99, 1024]
iter_binary_search(int_array, 0, len(int_array)-1, 55, NOT_IN_ARRAY, ARRAY_UNORDERED, LIMITS_REVERSED)