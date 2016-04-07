def numbers_sum(num1, num2):
    if num1 == 0:
        return 0
    result = num1 + num2
    return int(result)

def main():
    print numbers_sum(1, 2)
    print numbers_sum(5, 38)
    print numbers_sum(22, 3)
    print numbers_sum(4, 4)
    print numbers_sum(12, 88)

if __name__ == "__main__":
    main()