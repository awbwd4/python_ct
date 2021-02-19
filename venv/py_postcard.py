import re

#파일 전체 읽기
txt = open('C:\\Users\\JaeukKo\\Desktop\\trading_algorithm\\postcard.txt','rt',encoding='UTF-8').read()

# print("****full text****\n"+txt+"\n")


#본문 추려내기 : 머리말, 본문, 꼬리말 -> 두줄씩 띄어져있음. 본문만 화면에 출력
head, body, tail = tuple(txt.split('\n\n'))

# print("***body******\n"+body+'\n')

# :,.\ 를 없애기
s = re.sub('[:,\.]', '',body)
# print("*******text without punctuation*******\n"+s+'\n')

# 대문자로 변환.
s = s.upper()
# print("******Upper case*******\n"+s+'\n')


secret_words = []
for line in s.split('\n'):
    # print(line)
    secret_words += line.split()[:2]

print(secret_words)


# print(f.readlines())
#
# line = f.readlines()
# print(line)
#
#
# for x in range(5):
#     line = f.readlines()
#     print(line)