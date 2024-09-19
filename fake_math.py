def divide(first,second):
    if second==0 :
        return "Ошибка. На ноль делить нельзя!"
    else :
        return first/second


def main():
    print(divide(8, 4))
    print(divide(8, 0))


if __name__ == '__main__':
    main()