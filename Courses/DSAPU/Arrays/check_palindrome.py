




def check_palindrome(our_string):
    #Check startIDX vs endIDX same char until endIDX !> startIDX

    start_IDX = 0
    end_IDX = len(our_string)-1

    while start_IDX < len(our_string) - 1 - start_IDX:
        if our_string[start_IDX] != our_string[end_IDX]:
            return False
        start_IDX += 1
        end_IDX -= 1

    return True

input_string = 'radar'
input_string2 = 'tacocat'
input_string3 = 'tacocats'
# input_string4 = ''


def check_palindrome_python(our_string):

    if our_string == our_string[::-1]:
        return True
    return False

print(check_palindrome(input_string)) #True
print(check_palindrome(input_string2)) #True
print(check_palindrome(input_string3)) #False
print(check_palindrome_python(input_string)) #True
print(check_palindrome_python(input_string2)) #True
print(check_palindrome_python(input_string3)) #False
# print(check_palindrome(input_string4))