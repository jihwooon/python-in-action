"""
WordCount - https://dmoj.ca/problem/dmopc15c7p2

입력:
입력은 소문자와 공백으로 구성된 한 줄의 텍스트입니다.
각 단어 쌍 사이에는 정확히 하나의 공백이 있으면 첫 번째 단어 앞이나 마지막 단어 뒤에는 공백이 없습니다
(한 라인의 최대 길이는 80자입니다.)

출력:
입력된 라인의 단어 수를 출력합니다.
"""

origin_text = input()
text = origin_text.lower()
text_length = len(text)

if origin_text != text:
  print("오류: 입력은 소문자이여야합니다.")
  exit()

if text[0] == ' ' or text[-1] == ' ':
  exit("오류: 문자열 시작과 끝에 공백이 있습니다.")

if text_length > 80:
  print("오류: 한 라인에 최대 길이는 80자입니다.")
  exit()

if text.count(' ') != 0 or text.count('  ') != 0 or text.count('   ') != 0:
  exit("오류: 문자열에 공백이 연속적으로 있습니다.")

count = text.count(' ') + 1

print(count)
