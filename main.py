import sre_yield


def main():
    regex = r"http://xxx/abc[x-z]/image(9|10|11)\.png"
    urllist = list(sre_yield.AllStrings(regex))
    print(urllist)


if __name__ == "__main__":
    main()
