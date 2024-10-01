import sre_yield


def main():
    with open("before.txt", "r") as f:
        before = f.read().splitlines()

    result = []

    for text in before:
        print(text)
        urllist = list(sre_yield.AllStrings(text))
        result += urllist

    with open("after.txt", "w+") as f:
        for text in result:
            f.write(text)
            f.write("\n")


if __name__ == "__main__":
    main()
