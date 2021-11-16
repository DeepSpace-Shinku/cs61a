# print(2.5 in range(2, 4))
deck = [3, 4, 5, 6]
dock = [1, 2, 9, 3]
# print([[deck[i], deck[i + len(deck)//2]] for i in range(0, len(deck)//2)])

# sum([[3, 4], [5, 6]])

# print(sum([3, 4, 5, 6])


def pair_generator(n):
    return [n, n + 1]


# print([pair_generator(i) for i in range(10)])

pairs = list(zip(deck, dock))
print(pairs)
result = [x + y for x, y in pairs]
print(result)



