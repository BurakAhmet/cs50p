import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "youtube" not in s or "<iframe" not in s:
        return None
    url = ""
    if extension := re.search(r"(https?://)(www\.)?youtube\.com/(embed/)?\w+", s):
        url += extension.group(0)
    url = url.replace("http:", "https:")
    url = url.replace("www.", "")
    url = url.replace("youtube.com/embed", "youtu.be")

    return url


if __name__ == "__main__":
    main()
    
