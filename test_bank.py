from bank import value

def main():
    test_amount()

def test_amount():
    assert value("Hello") == 0
    assert value("H") == 20
    assert value("Ola") == 100

if __name__ == "__main__":
    main()
