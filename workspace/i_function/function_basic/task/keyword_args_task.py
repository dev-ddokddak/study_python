# # 국어, 영어, 수학 점수의 평균 구하기
# 내 풀이 : print를 안에서 해서 return이 필요 없었던 것 강사님 풀이랑 다른 이유
# def f_total_scores(ko_scores, en_scores, math_scores):
#         total_scores = ko_scores + en_scores + math_scores
#         avg_scores = total_scores / 3

#         print(f'국어: {ko_scores}')
#         print(f'영어: {en_scores}')
#         print(f'수학: {math_scores}')
#         print(f'평균: {avg_scores}')
        

# scores = {"ko_scores": 80, "en_scores": 80, "math_scores": 80}
# f_total_scores(**scores)

# 국어, 영어, 수학 점수의 평균 구하기
# def get_average(kor, eng, math):
#     total = kor + eng + math
#     average = total / 3
#     return average

def get_average(**scores):
    kor, eng, math = scores.values()
    total = kor + eng + math
    average = total / 3
    return average

# scores = {'kor': 100, 'eng': 90, 'math': 80}
# average = get_average(**scores)

# average = get_average(kor=100, eng=90, math=80)
# print(average)


scores = {'kor': 100, 'eng': 90, 'math': 80}
average = get_average(**scores)
print(average)

average = get_average(kor=100, eng=90, math=80)
print(average)

# datas = {"a": 1, "b": 2, "c": 3}
#
# a, b, c = datas
# print(a, b, c)
#
# a, b, c = datas.values()
# print(a, b, c)