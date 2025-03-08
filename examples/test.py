from cpp_for_high_perf import Calculator


def main():
    calc = Calculator()
    print(calc.add(10.0, 20.0))

    print(calc.subtract(30.0, 15.0))


if __name__ == "__main__":
    main()
