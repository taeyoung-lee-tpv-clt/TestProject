import pandas as pd

# Excel 파일 경로
npay_path = "C:/Users/phot1/algorithm/test/this/macro/Npay_1.xlsx"
shin_path = "C:/Users/phot1/algorithm/test/this/macro/shinhan_2.xls"

# Excel 파일 읽기
df_npay = pd.read_excel(npay_path)
df_shin = pd.read_excel(shin_path, engine='openpyxl')

# "합계" 열의 값들만 리스트로 추출
sum_npay = df_npay["합계"].tolist()
sum_shin = df_shin["이용금액"].tolist()
amount = sum_shin + sum_npay
# 추출한 값 출력
print(amount)
