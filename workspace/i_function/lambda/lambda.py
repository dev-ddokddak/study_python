def add(x, y):
    return x + y

# 람다(lambda): 이름이 없는 함수, 일회성, 매개변수 혹은 리턴값에 작성 가능
# lambda 매개변수,...: 리턴값

add = lambda x, y: x + y
result = add(1, 2)
print(result)

# map(function, iterator)
datas = [1, 2, 3, 4, 5]
# result = []

# for i in datas:
#     result.append(i * 2)
#
# print(result)

print(list(map(lambda number: number * 2, datas)))

for i in map(lambda number: number * 2, datas):
    print(i)


# 내 풀이 리스트 안에 담기를 안했다
# # 경로(/a, /b, ..) 앞에 /app 연결시키기
# route = ['/a', '/b', '/c', '/d', '/e', '/f', '/j']

# for i in map(lambda rou: '/app' + rou, route):
#     print(i)

urls = ['/game', '/news', '/fashion', '/ranking']
real_urls = list(map(lambda url: f'/app{url}', urls))
print(real_urls)

# filter(function, iterator)
# '/app/game'.split("/")[-1] == 'game'
print(list(filter(lambda url: url.split("/")[-1] == 'game', real_urls)))

# 1 ~ 10까지 중 짝수만 추출
# 내 풀이 필터 사용법 알아둘 것
# number = []
# for i in range(10):
#     number.append(i + 1)
# print(list(filter(lambda number: number % 2 == 0, number)))


#강사님 풀이
print(list(filter(lambda number: number % 2 == 0, [i + 1 for i in range(10)])))