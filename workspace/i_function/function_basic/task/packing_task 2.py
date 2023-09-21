# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# list에 국어, 영어, 수학 점수를 각각 담은 후 unpacking 발생시키기

def f_total_scores(en_scores, ma_scores, ko_scores):
    print(f'총점: {en_scores + ma_scores + ko_scores}')

data_list = [100, 80, 70]

# 문자열에서 'A'가 몇 개 있는 지 검사하는 함수
# packing
def total_a(*num):
    count = 0
    for i in num:
        if i == 'A':
            count += 1
    return count
datas = 'AAAAVVV'
print(total_a(*datas))