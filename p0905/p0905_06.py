# 숫자를 입력받아서 
# 100 보다 큰수 이면 100보다 큰수입니다 
# 100 보다 작은 수면 100보다 작은 수 입니다를 출력

# 1. 숫자입력받기 
num1 = int(input("숫자를 입력해주세요 >> "))
# 2. 조건문으로 비교하여 출력하기 
if num1 >= 100:
    print("100보다 큰수 입니다.")
else:
    print("100보다 작은 수 입니다. ")

# 짝수인지 홀수 인지 
# 짝수는 입력받은 숫자를 2로 나누어서 
# 나머지가 0이면 짝수 나머지가 1이면 홀수 

if num1%2 == 0:
    print("짝수 입니다")
else:
    print("홀수 입니다")
    
# if 안에 if를 쓸수 있다 
if num1 > 100: 
    print("100보다 큼")
    if num1%2 == 0:
        print("짝수")
    else:
        print("홀수")
else:
    print("100보다 작음")
