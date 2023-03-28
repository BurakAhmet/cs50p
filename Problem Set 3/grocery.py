def main():
    items = []
    try:
        while True:
            item = input().upper().strip()
            items.append(item)
    except EOFError:
        pass
    items.sort()
    for i in range(len(items)):
        count = items.count(items[i])
        try:
            if items[i] != items[i+1]:
                print(items.count(items[i]), items[i])
        except IndexError:
            print(items.count(items[i]), items[i])


main()
