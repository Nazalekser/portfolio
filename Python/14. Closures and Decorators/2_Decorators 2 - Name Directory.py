'''You are given some information about N people. Each person has a first name, 
last name, age and sex. Print their names in a specific format sorted by their age 
in ascending order i.e. the youngest person's name should be printed first. 
For two people of the same age, print them in the order of their input.'''


import operator


def person_lister(f):
    def inner(people):
        # complete the function
        sorted_list = sorted(people, key=lambda x: x[2])
        formatted = [f(i) for i in sorted_list]
        return formatted
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# def person_lister(f):
#     def inner(people: list[str]):
#         people.sort(key=lambda x: int(x[2]))
#         return [f(person) for person in people]
#     return inner


# # Using itemgetter:

# def person_lister(f):
#     def inner(people: list[str]):
#         get_age = operator.itemgetter(2)
#         people.sort(key=lambda x: int(get_age(x)))
#         return [f(person) for person in people]
#     return inner
