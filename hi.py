import platform


def inc(x):
    return x + 1

print("hi")
print(platform.python_version())

def test_answer():
    assert inc(3) == 4
    
def test_dummy():
    pass
