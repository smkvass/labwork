#Write a function that accepts string from user, return a sentence with the words reversed. 
# We are ready -> ready are We
def do_reverse(str):
    strings = str.split()[::-1]
    reversed_list = []
    for i in strings:
        reversed_list.append(i)
    return " ".join(reversed_list)

input_str = input("Enter words: ")
res = do_reverse(input_str)
print(res)