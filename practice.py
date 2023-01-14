# weather="비"
# if weather=="비":     # if 조건:
#     print("우산챙겨")  #  실행명령문

weather="눈"
if weather=="비":     
    print("우산챙겨")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else:
        print("준비물 필요없어요")


weather=input("오늘날씨 어때요?:") #input: 사용자가 값을 직접 입력하도록 함
if weather=="비" or weather =="눈":     #or로 조건추가가능
    print("우산챙겨")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else:
        print("준비물 필요없어요")


temp=int(input("기온은 어떄요?")) #숫자로 값을 받아서 int로 감쌈
if 30<= temp:
    print("너무 더워요.나가지마요")
elif 10<=temp and temp<30:
    print("괜찮은 날씨에요")
elif 0<=temp <10:
    print("외투챙겨요")
else:
    print("너무추워요.나가지마요")