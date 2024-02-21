
# typecasting은 int()함수와 float()함수를 통해 할 수 있다
# 괄호 방향 주의! c언어의 (int) p;와 구분. 그리고 파이썬에서 int()와 float()은 함수임
# c언어와 마찬가지로 flaot을 int로 변환할 때는 소수점 아래를 버림

num1 = 34
print( float(num1) )

num2 = 34.87
print( int(num2) )



# input()을 통해 입력받은 내용의 type은 문자열임

var1 = input("입력하세요: ")
print(var1, type(var1))


# 입력받은 소수를 정수로 변환하기
# 1. 잘못된 예시

var2 = input("입력하세요: ")
print( var2, type(int(var2)) )

# float type - 1.1을 입력하면 error가 출력됨
# 왜냐하면 input에서 입력받은 변수 num2는 문자열이기 때문에
# 소수점이 포함된 문자열을 바로 정수로 바꾸려고 하면 error가 나옴


# 2. 올바른 예시

var3 = float( input("입력하세요: ") )
print( int(var3), type(int(var3)) )

# 입력받은 소수를 정수로 변환하기 위해서는 
# 일단 문자열을 float type으로 casting한 뒤, 다시 int로 변환해야 한다