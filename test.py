
def count_ss(main_string, sub_string):
    count = 0
    for i in range(len(main_string) - len(sub_string) + 1):
        if main_string[i: i + len(sub_string)] == sub_string:
            count += 1
    return count


def minion_game(string):
    consonent_string = "".join(set(string))
    for char in string:
        if char not in 'aeiou' and

# your code goes here


if __name__ == '__main__':
