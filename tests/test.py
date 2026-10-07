import  sys
sys.path.append("src")


from main import greet


def test_greet():
    assert greet("Tiger") =="hello Tiger"
    