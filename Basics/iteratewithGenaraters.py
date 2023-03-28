def remote_controller_next():
    yield "cnn"
    yield "espn"
    yield "netflix"


iter = remote_controller_next()

print(next(iter))
print(next(iter))


for c in remote_controller_next():
    print(c)