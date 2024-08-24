def recursive_sum(numbers:list) -> int:
    if len(numbers) == 1:
        return numbers[0]
    else:
        return recursive_sum(numbers[1:]) + numbers[0]

if __name__ == '__main__':
    result = recursive_sum([5,6,7,8,9,10])
    print(result)