def print_numbers():

    for i in range(1001):
        if i % 3 == 0 and  i % 5 and sum(map(lambda x: int(x),list(str(i)))) < 10:
            print(i)

print_numbers()