#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def unique_elem(listt):
    listt = []
    for i in listt:
        if i not in listt:
            listt.append(i)
    return listt
