# 무슨 질문을 하더라도 항상 같은 답을 하는 함수 만들기
# 답: 아 그렇군요!


def qu_and_a(question):
    return "아 그렇군요!"

print(qu_and_a("dd"))


def 공칠게(공):
    data = 2
    result = None
    if data == 1:
        result = "홈런"
    elif data == 2:
        result = "파울"
    else:
        result = "아웃"
    return result


print(공칠게("야구공"))

def 굽자(제육볶음):
    후라이팬 = 제육볶음
    제육볶음 = "요리"
    return 제육볶음

def 제육볶음만들어(고기):
    제육볶음 = 고기 + "양파" + "마늘" + "소스"
    return 제육볶음


print(굽자(제육볶음만들어("돼지고기")))