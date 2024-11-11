# a
def my_avg(x: int, y: int) -> float:
    sum_avg = x + y
    result = sum_avg / 2
    return result


avg1: float = my_avg(99, 90)
print(avg1)


# b
def my_headline(word: str) -> str:
    """
    Prints the word or sentence with big letters and adds the '!' sign in the end
    :param word: str: word/sentence
    :return: str: WORD!/SENTENCE!
    """
    return word.upper() + '!'


head1: str = my_headline("python has concurred the world")
print(head1)
print(head1)


# c
def concat_list(list1: list[int], list2: list[int], list3: list[int]) -> list[int]:
    return list1 + list2 + list3


res_con: list[int] = concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9])
print(res_con, f"The length of list - {len(res_con)}")
