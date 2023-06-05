def reverse_subsequence(length):
    if length == 0:
        return ' '
    element = input("write something: ")
    return reverse_subsequence(length - 1) + element + " "
print(reverse_subsequence(4))