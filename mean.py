def mean(data):
    # Assigned: Samuel Adesola
    # Calculate the mean of a list of numbers
    # data: a list of numbers
    # return: the mean of the list of numbers
    # mean = sum(data) / len(data)
    sum = 0
    for d in data:
        sum += d
    mean = sum / len(data)
    return mean

numbers = [1, 2, 3, 4, 5]
print(mean(numbers))


        