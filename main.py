def corresponding_parenthesis(text):
    left_bracket = 0
    right_bracket = 0
    sorted_characters = sorted(str(text))
    print(sorted_characters)

    for item in sorted_characters:
        if item == "(":
            left_bracket += 1
        elif item == ")":
            right_bracket += 1
    if left_bracket > right_bracket:
        return f'{(left_bracket - right_bracket)* "("}'
    elif left_bracket < right_bracket:
        return f'{(right_bracket - left_bracket)* ")"}'
    else:
        return ""


def remove_more_than_two_repetitions(text):
    output = ""
    for index, ele in enumerate(text):
        if not(ele == text[index-2] and ele == text[index-1]):
            output += ele
    return output

    



