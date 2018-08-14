count = 1
while count < 5:
    print(count)
    count += 1
else:
    print('else')

for i in {1, 2, 3}:
    print(i)

for i in range(1, 3):
    print(i)

list = [n - 1 for n in range(1, 6) if n % 2 == 1]
print(list)

rows = range(1,3)
cols = range(1,3)
list = [(row, col) for row in rows for col in cols]
print(list)


def hoge(*args):
    print(sum(args))


hoge(1,2,3)


def run_lambda(func):
    func()


run_lambda(lambda: print(3))


def range2(first=1,last=10):
    n = first
    while n < last:
        yield n
        n += 2


print(range2(1,10))


def document(func):
    def new_func(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return new_func


@document
def print_hoge():
    print('hoge')


print_hoge()


list = range(1,4)
for l in range(1,5):
    try:
        print(list[l])
    except IndexError as e:
        print(e)
