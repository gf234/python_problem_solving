from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    ans = 0
    for city in cities:
        city = city.upper()
        if city in cache:
            ans += 1
            cache.remove(city)
            cache.append(city)
        else:
            ans += 5
            cache.append(city)
    return ans



cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))
