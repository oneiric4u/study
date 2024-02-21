print("\n1. 정수 출력 형태")

# 정수
a1 = "{:d}".format(52)

# 너비 조정
a2 = "{:5d}".format(52)
a3 = "{:8d}".format(-52)

# 빈칸을 0으로 채우기
a4 = "{:05d}".format(52)
a5 = "{:05d}".format(-52) # 기호 ' - ' 도 자리수에 포함

print(a1 +"\n" + a2 +"\n" + a3 +"\n" + a4 +"\n" + a5)



print("\n\n2. 부호 출력 형태")

print("\n1) b1 ~ b6")

b1 = "{:+d}".format(52)

b2 = "{:+d}".format(-52)

b3 = "{: d}".format(52)

b4 = "{: d}".format(-52)

b5 = "{:-d}".format(52)

b6 = "{:-d}".format(-52)

print(b1 +"\n" + b2 +"\n" + b3 +"\n" + b4 + "\n" + b5 +"\n" + b6)


print("\n2) b7 ~ b10")

b7 = "{:+5d}".format(52)

b8 = "{:+5d}".format(-52)

b9 = "{:-5d}".format(52)

b10 = "{:-5d}".format(-52)

print(b7 +"\n" + b8 +"\n" + b9 +"\n" + b10)


print("\n\n3. zero padding과 부호")

c1 = "{:05d}".format(52)

c2 = "{:+05d}".format(52)

c3 = "{:+05d}".format(-52)

c4 = "{:-05d}".format(52)

c5 = "{:-05d}".format(-52)

print(c1 +"\n" + c2 +"\n" + c3 +"\n" + c4 +"\n" + c5)


print("\n\n4. 조합 형태")

# 기호 ' = ' 은 기호 ' + '나 ' - '를 맨 앞으로 보낸다

print("\n1) d1 ~ d4")

d1 = "{:=+5d}".format(52)

d2 = "{:=+5d}".format(-52)

d3 = "{:=-5d}".format(52)

d4 = "{:=-5d}".format(-52)

print(d1 +"\n" + d2 +"\n" + d3 +"\n" + d4)


print("\n2) d5 ~ d8")

d5 = "{:=+05d}".format(52)

d6 = "{:=+05d}".format(-52)

d7 = "{:=-05d}".format(52)

d8 = "{:=-05d}".format(-52)

print(d5 +"\n" + d6 + "\n" + d7 +"\n" + d8)


print("\n\n5. 변형 형태")
e1 = "{:+=5d}".format(52)
e2 = "{:#=5d}".format(52)
print(e1 +"\n" + e2)