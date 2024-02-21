# format()함수 : 문자열로 변환


string = "{}{}{}".format(1, 2, 3.1)
print(type(string)) # 이 두 줄을 c언어처럼 
# print(type(str1 = "{}{}{}".format(1,2,3.1)))로 통합할려고 시도하면 error뜸
# type()함수와 같은 함수를 사용할 때는 값의 할당이 아니라 변수나 값 자체를 인자로 전달해야 한다


str1 = "{}{}{}".format(1,2,3.1)

str2 = "{}만원 그리고".format(1000)

str3 = "{}과 {}과 {}와 {}".format(1, "문자열", True, 2.41)

print(str1,"\n" + str2, str3)
# print 함수의 콤마로 구분된 인자들 사이에는 공백이 자동으로 추가됨
# 만약 print(str1,"\n", str2, str3)과 같이 쓴다면 1000만원 앞에 공백이 생기므로
# 이를 없애기 위해 콤마 대신 + 기호를 사용하면 공백이 생기지 않음

# 프롬프트 창에 "{} {}".format(1,2,3,4,5)을 입력하면 '1 2' 가 정상출력되지만
# "{} {} {}".format(1,2)을 입력하면 index error가 뜨며 소스코드도 마찬가지이다

num1 = "{:15.3f}".format(52.273)
num2 = "{:015.2f}".format(52.273)
num3 = "{:15.1f}".format(52.273)

print(num1 + "\n" + num2 + "\n" + num3)