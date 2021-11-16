f1 = lambda x: x
f2 = lambda x: x**-1
f3 = lambda x: 1-x
f4 = lambda x: (1-x)**-1
f5 = lambda x: (x-1)*(x**-1)
f6 = lambda x: x*(x-1)**-1

fs = [f1, f2, f3, f4, f5, f6]

for i in range(0, 6):
    for j in range(0, 6):
        for k in range(0, 6):
            if fs[j](fs[i](3)) == fs[k](3):
                print('the compose of f{} and f{} is f{}'.format(i+1, j+1, k+1))
                break
            if k == 5:
                print('error in finding the compose of f{} amd f{}'.format(i+1, j+1))
                print('f{}°f{}(3) = {}'.format(i+1, j+1, fs[j](fs[i](3))), [f1(3), f2(3), f3(3), f4(3), f5(3), f6(3)])