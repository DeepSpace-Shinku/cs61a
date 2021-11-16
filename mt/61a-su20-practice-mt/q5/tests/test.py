
for j in range(8):
    print('this is group by {}'.format(j))
    group = []
    for i in range(100):
        if not i*j % 8 in group:
            group.append(i*j % 8)
    print(sorted(group))