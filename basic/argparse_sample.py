import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n1", "--number1", help="number 1", required=False)
    parser.add_argument("-n2", "--number2", help="number 2", required=False)
    args = parser.parse_args()
    print(args)