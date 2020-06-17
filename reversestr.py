def reverse(str):
    length = len(str)
    for i in range(length -1, -1, -1):
        yield str[i]


while True:
    inp = input("plz type string that you want to be reverse(press q to exit): ")

    for char in reverse(inp):
        print(char)
    if inp == "q":
        break

