def brackets_only(my_string: str):
    new_string = ""
    for char in my_string:
        if char in "()[]":
            new_string += char
    return new_string

def balanced_brackets(my_string: str):
    my_string = brackets_only(my_string)
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')'):
        if not (my_string[0] == "[" and my_string[-1]== "]"):
            return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])


if __name__ == "__main__":

    ok = balanced_brackets("(((())))")
    print(ok)

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok)

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok)

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok)


    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)