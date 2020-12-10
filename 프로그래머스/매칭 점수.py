from collections import defaultdict
import re


def solution(word, pages):
    word = word.lower()
    basic_score = dict()
    link_score = defaultdict(lambda: 0)
    links_dict = dict()
    for i, page in enumerate(pages):
        page = page.lower()
        meta_parser = re.compile('<meta .* content="(\S*)"/>')
        url = re.findall(meta_parser, page)[0]
        a_parser = re.compile('<a href="(\S*)">')
        links = re.findall(a_parser, page)
        links_dict[url] = links
        word_parser = re.compile('(?<![a-z])('+word+')(?![a-z])')
        words = re.findall(word_parser, page)
        bs = len(words)
        basic_score[url] = (bs, i)

    for url, links in links_dict.items():
        if len(links) == 0:
            continue
        score = basic_score[url][0]/len(links)
        for link in links:
            link_score[link] += score

    max_score = -1
    max_ind = float('inf')
    for url, val in basic_score.items():
        bs, i = val
        matching_score = (bs+link_score[url])
        if max_score < matching_score:
            max_score = matching_score
            max_ind = i
    return max_ind


word = "Muzi"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution(word, pages))
