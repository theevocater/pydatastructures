def fibonacci(count):
    back2 = 0
    if count > 1:
        yield back2

    back1 = 1
    if count > 2:
        yield back1

    count -= 2
    while count > 0:
        yield back2 + back1
        next = back2 + back1
        back2 = back1
        back1 = next
        count -= 1

if __name__ == "__main__":
    for i in fibonacci(5):
        print i
    print

    for i in fibonacci(10):
        print i
