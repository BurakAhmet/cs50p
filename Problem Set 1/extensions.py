def main():
    data = input("File name: ")
    determiner(data)
def determiner(data):
    if(".jpeg" in data or ".jpg" in data):
        print("image/jpeg")
    elif(".gif" in data):
        print("image/gif")
    elif(".png" in data):
        print("image/png")
    elif(".pdf" in data or ".PDF" in data):
        print("application/pdf")
    elif(".txt" in data):
        print("text/plain")
    elif(".zip" in data):
        print("application/zip")
    else:
        print("application/octet-stream")
main()
