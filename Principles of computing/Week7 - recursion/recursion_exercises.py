





def gray_to_bin(gray_code):
    """
    Our solution for make_gray returns a list of Gray codes ordered in ascending value. For standard
    binary numbers, the function bin_to_dec computes the value of a binary number. To compute the decimal
    value of a Gray code, we will implement a function gray_to_bin that converts a Gray code to the
    standard binary number with same value. This function can then be used to compute the value of a Gray code
     by evaluating bin_to_dec(gray_to_bin(gray_code)).
    Challenge problem: Your final task is to write a recursive function gray_to_bin(gray_code) that performs
    this conversion. Again, this function is remarkably simple. However, deriving this function on your own may
    prove to be quite difficult. So, we recommend that you read up further on Gray codes as you work on this
    problem. In particular, we suggest that you focus on the next to
    last paragraph in the Wikipedia section referenced above.
    """
    if len(gray_code) <= 1:
        return gray_code
    else:
        first_digit = gray_code[0]
        second_digit = int(gray_code[1])
        next_first_digit = str((int(first_digit)+second_digit) % 2)
        new_code = next_first_digit + gray_code[2:]
        return (first_digit + gray_to_bin(new_code))


def test_gray_to_bin():
    print "Computed: ", gray_to_bin('0'), "Expected: 0"
    print "Computed: ", gray_to_bin('1'), "Expected: 1"
    print "Computed: ", gray_to_bin('00'), "Expected: 00"
    print "Computed: ", gray_to_bin('01'), "Expected: 01"
    print "Computed: ", gray_to_bin('11'), "Expected: 10"
    print "Computed: ", gray_to_bin('10'), "Expected: 11"
    print "Computed: ", gray_to_bin('1000'), "Expected: 1111"
    print "Computed: ", gray_to_bin('111'), "Expected: 101"
#test_gray_to_bin()

def make_gray(length):
    """
    For the third problem, your task is to write a recursive function make_gray(length) that generates a list of
    binary strings of the specified length ordered such that consecutive strings differ by exactly one bit.
    Your recursive solution should be very similar to make_binary which generated a list of all binary strings
    ordered by their standard values. If the length is zero, the answer is the list consisting of the empty string.
    Otherwise, your function should recursively compute make_gray(length-1) and use this list to construct
    make_gray(length).
    """
    if length == 0:
        return [""]
    else:
        tail = make_gray(length-1)
        ans = ["0" + num for num in tail]
        tail.reverse()
        return(ans + ["1" + num for num in tail])

    # else:
    #     tail = make_gray(length-1)
    #     copy = list(tail)
    #     copy.reverse()
    #     return (["0" + num for num in tail] + ["1" + num for num in copy])


def test_make_gray():
    """
    """
    print "Computed: ", make_gray(0), "Expected: ['']"
    print "Computed: ", make_gray(1), "Expected: ['0','1']"
    print "Computed: ", make_gray(2), "Expected: ['00','01','11','10']"
    print "Computed: ", make_gray(3), "Expected: ['000','001','011','010','110','111','101','100']"

        # print "Computed: ", make_gray(0), "Expected: 0"
    # print "Computed: ", make_gray(0), "Expected: 0"
test_make_gray()

def bin_to_dec(bin_num):
    """
    Converts a binary string to a decimal number, using recursion
    """
    if len (bin_num) == 0:
        return 0
    else:
        unit_digit = int(bin_num[-1])
        shortened = bin_num[0:-1]
        return unit_digit + 2 * bin_to_dec(shortened)


def test_bin_to_dec():
    print "Comp:", bin_to_dec("0"), "Exp: 0"
    print "Comp:", bin_to_dec("000"), "Exp: 0"
    print "Comp:", bin_to_dec("01"), "Exp: 1"
    print "com:", bin_to_dec("10110"), "Exp: 22"
#test_bin_to_dec()


def make_binary(length):
    """
    Return a list of all binary numbers of given length, each as a string
    """
    if length == 0:
        return [""]
    else:
        tail = make_binary(length-1)
        return (["0" + num for num in tail] + ["1" + num for num in tail])
#print make_binary(3)

def test_make_binary():
    print "Comp:", make_binary(0), "Exp: ['']"
    print "Comp:", make_binary(1), "Exp: ['0','1']"
    print "Comp:", make_binary(2), "Exp: ['00', '01', '10', '11']"
    print "com:", len(make_binary(5)), "Exp: 32"
#test_make_binary()

#print make_binary(6)

def gcd(num1, num2):
    """
    Challenge: Write a function gcd(num1, num2) that takes two non-negative integers and computes the
    greatest common divisor of num1 and num2. To simplify the problem, you may assume that the greatest
    common divisor of zero and any non-negative integer is the integer itself. For an extra challenge,
    your programs should only use subtraction. Hint: If you get stuck, try searching for "Euclid's Algorithm".
    Solution... Kudos to Eudclid!
    """
    if num2 > num1:
        return gcd(num2, num1)
    elif num2 == 0:
        return num1
    else:
        return gcd(num1 - num2, num2)



def test_gcd():
    print "Comp", gcd(0,0), "Exp 0"
    print "Comp", gcd(0,6), "exp 6"
    print "comp", gcd(1,9), "exp 1"
    print "com", gcd(2,7), "exp 1"
    print "com", gcd(2,8), "exp 2"
    print "comp", gcd(15,25), "exp 5"
#test_gcd()


def slice(my_list, first, last):
    """
    Write a slice funktin that does not use build in list slicing
    """
    if len(my_list) == last - first:
        return my_list
    else:
        if last < len(my_list):
            my_list.pop(-1)
        if first > 0:
            my_list.pop(0)
            first -= 1
            last -= 1
        return slice(my_list, first, last)

def test_slice():
    pass
    print "Computed:", slice([],0,0), "Expected: []"
    print "Computed:", slice([6],0,1), "Expected: [6]"
    print "Computed:", slice([5,3],0,1), "Expected: [5]"
    print "Computed:", slice(["a", "sog", "b"],1,3), "Expected: ['sog', 'b']"
    print "Computed:", slice(["a", "sog", "b", "xx"],0,2), "Expected: ['a', 'sog']"
#test_slice()

def test_slice2():
    """
    Some test cases for slice
    """
    print "Computed:", slice([], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 1), "Expected: [1]"
    print "Computed:", slice([1, 2, 3], 0, 3), "Expected: [1, 2, 3]"
    print "Computed:", slice([1, 2, 3], 1, 2), "Expected: [2]"

#test_slice2()

def list_reverse(my_list):
    """Write a function list_reverse(my_list) that takes a list and returns a new list whose elements appear
    in reversed order. For example, list_reverse([2, 3, 1]) should
    return [1, 3, 2]. Do not use the reverse() method for lists.
    """
    if my_list == []:
        return my_list
    else:
        last = my_list[-1]
        rest_reversed = list_reverse(my_list [:-1])
        return [last] + rest_reversed


def test_list_reverse():
    print "Computed:", list_reverse([]), "Expected: []"
    print "Computed:", list_reverse([5]), "Expected: [5]"
    print "Computed:", list_reverse([1,2]), "Expected: [2,1] "
    print "Computed:", list_reverse(["a", "sog", "b"]), "Expected: ['b', 'sog', 'a']"
    print "Computed:", list_reverse(["a", "sog", "b", "xx"]), "Expected: ['xx','b', 'sog', 'a']"
#test_list_reverse()



def insert_x(my_string):
    """
    Write a function insert_x(my_string) that takes the string my_string and adds
    the character 'x' between each pair of consecutive characters in the string. For example,
    insert_x("catdog") should return "cxaxtxdxoxg"
    """
    if len(my_string) <= 1:
        return my_string
    else:
        first_char = my_string[0]
        rest_inserted = insert_x(my_string[1:])
        return first_char + rest_inserted

def test_insert_x():
    print "Computed:", insert_x(""), "Expected:"
    print "Computed:", insert_x("a"), "Expected: a"
    print "comp", insert_x("ab"), "Expected: axb"
    print "comp", insert_x("catdog"), "exp: cxaxtaxdxoxg"

#test_insert_x()

def remove_x(my_string):
    "Removes all x's from any given string "
    if my_string == "":
        return my_string
    else:
        first_letter = my_string[0]
        rest = my_string[1:]
        if first_letter == "x":
            return remove_x(rest)
        else:
            return first_letter + remove_x(rest)

def test_remove_x():
    """
    Some test cases for remove_x
    """
    print "Comuted: ", remove_x(""), "Expected: "
    print "Computed:", remove_x("a"), "Expected: a"
    print "Computed:", remove_x("ax"), "Expected: a"
    print "Computed:", remove_x("catxxdogx"), "Expected: catdog"

#test_remove_x()





def is_member(my_list, element):
    if len(my_list) == 0:
        return False
    else:
        if my_list[0] == element:
            return True
        else:
            return is_member(my_list[1:], element)

def test_is_member():
    """
    Some test cases for is_member
    """
    print "Computed:", is_member([], 1), "Expected: False"
    print "Computed:", is_member([1], 1), "Expected: True"
    print "Computed:", is_member(['c', 'a', 't'], 't'), "Expected: True"
    print "Computed:", is_member(['c', 'a', 't'], 'd'), "Expected: False"

#test_is_member()



def triangular_sum(num):
    if num == 0:
        return num
    else:
        return num + triangular_sum(num - 1)

#print triangular_sum(1)

def number_of_threes(num):
    """
    Takes a non-negative integer num and compute the
    number of threes in its decimal form
    Returns an integer
    """
    if num == 0:
        return 0
    else:
        unit_digit = num % 10
        threes_in_rest = number_of_threes(num // 10)
        if unit_digit == 3:
            return threes_in_rest + 1
        else:
            return threes_in_rest

def num_of_threes(num):
    str_num = str(num)
    if len(str_num) == 1:
        if str_num == "3":
            return 1
        else:
            return 0
    else:
        return num_of_threes(str_num[-1]) + num_of_threes(str_num[:-1])

#print num_of_threes(3133)
