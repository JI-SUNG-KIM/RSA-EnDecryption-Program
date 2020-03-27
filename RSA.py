import random
from parse import *
print("RSA암호화, 복호화 프로그램입니다.")
prinum = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199)
#print(prinum) #테스트용

#공개키 : (n.e) / n = p*q (p,q는 소수), e = (p-1)(q-1)과 서로소인 수
#해독키 : (n,d) / n = p*q (p,q는 소수), ed ≡ 1 {mod(p-1)(q-1)}를 만족하는 최소의 정수

#M =평문, m = 암호문
#암호화 하는 법 : m = M^e mod n
#복호화 하는 법 : M = m^d mod n

while True:
    print("-"*100)
    purpose = int(input("키를 생성하려면 1, 암호화를 하려면 2, 복호화를 하려면 3, 그만두려면 이외의 숫자를 입력하세요 : "))
    
    if purpose == 1:
        #n생성
        p = random.choice(prinum)
        q = random.choice(prinum)
        while p == q:
            q = random.choice(prinum)
        n = p * q
        #print(p, q, n) #테스트용
    
        #e생성
        e = 2
        while (p-1)*(q-1) % e == 0:
            #print(e) #테스트용
            e += 1
    
        #공개키 생성
        print("공개키는 (" + str(n) + "(n),"  + str(e) + "(e)) 입니다.")
    
        #d생성
        d = 1 
        while e*d % ((p-1)*(q-1)) != 1 % ((p-1)*(q-1)):
            #print(d) #테스트용
            d += 1
        
        #암호키 생성
        print("비밀키는 (" + str(n) + "(n),"  + str(d) + "(d)) 입니다.")

    elif purpose == 2:
        #값과 공개키를 입력받아 암호화
        M = int(input("암호화할 숫자를 입력하세요 : "))

        #파싱하여 저장
        openkey = parse("({},{})", input("공개키를 입력하세요 (n,e) : "))
        n = openkey[0]
        e = openkey[1]
        #print(n, e) #테스트용

        if M >=int(n):
            print("암호화하려는 숫자는 n보다 작아야 합니다!")
        else:
            #암호화된 값 출력
            m = M ** int(e) % int(n)
            print("암호화된 값은 " + str(m) + "입니다")

    elif purpose == 3:
        #값과 비밀키를 입력받아 복호화
        m = int(input("복호화할 숫자를 입력하세요 : "))

        #파싱하여 저장
        closekey = parse("({},{})", input("비밀키를 입력하세요 (n,d) : "))
        n = closekey[0]
        d = closekey[1]
        #print(n, d) #테스트용

        #복호화된 값 출력
        M = m ** int(d) % int(n)
        print("복호화된 값은 " + str(M) + "입니다")

    else:
        break