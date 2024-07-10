class test1:
    def __init__(self, name, age):  # 생성자(Constructor) 생성 시 자동 수행
        self.name = name
        self.age = age + 5  # 변수 생성 후 파라미터로 보낸 값 할당
        print("[생성자] self와 변수 비교 " + str(self.age) + " age : " + str(age))
        print("[생성자] 이름 : " + self.name + " 나이 : " + str(self.age))


a = test1("철수", 20)  # 객체화 (ClassExample의 정보를 a에 담음)

b = 40
var = '12314'
print(b + int(var))