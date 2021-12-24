




def reverse_integer(n):

    reversed_num = 0

    while n > 0:
        digit_to_move = n % 10
        reversed_num = reversed_num * 10 + digit_to_move
        n = n//10
    return reversed_num
print(reverse_integer(4321))