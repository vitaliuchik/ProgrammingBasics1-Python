def selection_sort(numbers):
    """
    list(int) -> None

    Sort lst using selection sorting algorithm
    >>> selection_sort([5, 4, 7, 2, 1])
    """
    for el in range(len(numbers)):
        min_el = el
        for i in range(el + 1, len(numbers)):
            if numbers[min_el] > numbers[i]:
                min_el = i
        numbers[el], numbers[min_el] = numbers[min_el], numbers[el]



def calculate(numbers):
    """
    list(int) -> tuple
    Retirn list, amount, sum of numbers, min and max number, average and median
    >>> print(calculate([4, 2, 32, 8, 16]))
    ([4, 2, 32, 8, 16], 5, 62, 2, 32, 12.4, 8)
    """
    old_lst = numbers[::]
    selection_sort(numbers)
    if len(numbers) % 2 == 1:
        median = numbers[len(numbers) // 2]
    else:
        median = (numbers[len(numbers) // 2] + numbers[(len(numbers) // 2) - 1]) / 2
    average = sum(numbers) / len(numbers)

    return old_lst, len(numbers), sum(numbers), min(numbers), max(numbers), \
           average, median



if __name__ == '__main__':
    numbers = []
    while True:
        number = input("enter a number or Enter to finish")
        if number:
            try:
                numbers.append(int(number))
            except ValueError as err:
                print(err)
        else:
            break
    print(calculate(numbers))
