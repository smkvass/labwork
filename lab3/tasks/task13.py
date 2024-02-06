#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def num_3(num):
    for i in range(len(num) - 1):
        if nums[i] == 3 and num[i + 1] == 3:
            return True
        return False