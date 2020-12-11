import re


def solution(files):
    parser = re.compile(r'(\D+)(\d{1,5}).*')

    def sortRule(x):
        arr = re.findall(parser, x)
        head = arr[0][0].lower()
        number = int(arr[0][1])
        return (head, number)
    files.sort(key=sortRule)
    return files


files = ["img12.png", "img10.png", "img02.png",
         "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
