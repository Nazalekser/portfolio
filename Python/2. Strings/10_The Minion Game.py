# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# Print the winner's name and score, separated by a space on one line, or Draw if there is no winner


# def minion_game(string):
#     count_stuart = 0
#     count_kevin = 0
#     for a in range(len(string)):
#         if all(string[a] != x for x in ('A', 'E', 'I', 'O', 'U')):
#             for i in range(len(string) - a):
#                 if string[a:a+i+1]:
#                     count_stuart += 1
#         else:
#             for i in range(len(string) - a):
#                 if string[a:a+i+1]:
#                     count_kevin += 1
#
#     if count_stuart > count_kevin:
#         print('Stuart', count_stuart)
#     elif count_stuart < count_kevin:
#         print('Kevin', count_kevin)
#     else:
#         print('Draw')

def minion_game(string):
    k, s = 0, 0
    for i in range(len(string)):
        if string[i] in {'A', 'E', 'I', 'O', 'U'}:
            k += len(string) - i
        else:
            s += len(string) - i

    print('Draw' if k == s else f'Kevin {k}' if k > s else f'Stuart {s}')


if __name__ == '__main__':
    s = input()
    minion_game(s)
