# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))\

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.count("n"))

# print("나는 {}살입니다." .format(20))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요" .format(color="빨간", age = 20))

#방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자
# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 '나도코딩' 입니다.")
# print("저는 \"나도코딩\"입니다.")
# print("Red Apple\rPine")

#퀴즈
url = "http://naver.com"
my_str = url.replace("http://","")
print(my_str)
print(url[7:])
my_str = my_str[:my_str.index(".")]
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} ")



