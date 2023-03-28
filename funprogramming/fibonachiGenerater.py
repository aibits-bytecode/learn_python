def fibGenarator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in fibGenarator():
    if f > 50:
        break
    else:
        print(f)
