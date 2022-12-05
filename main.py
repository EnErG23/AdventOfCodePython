year = 2019


def run():
    printheader()
    for y in range(2019, 2022):
        for d in range(1, 25):
            print()
            printday(y, d)


def printheader():
    print("############################")
    print("###                      ###")
    print("###    Advent of Code    ###")
    print(f"###         {year}         ###")
    print("###                      ###")
    print("############################")


def printday(y, d):
    if d < 10:
        d = "0" + str(d)
    exec(open(str(y) + "/Days/" + d + ".py").read())


if __name__ == '__main__':
    run()

