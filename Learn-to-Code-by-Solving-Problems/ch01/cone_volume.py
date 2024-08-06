"""
ConeVolume - https://dmoj.ca/problem/dmopc14c5p1

입력
입력은 두 줄 텍스트로 구성됩니다. 첫 번째 라인은 원뿔의 반지름인 정수 r이고, 두 번째 라인은
원뿔의 높이인 정수 h입니다. r과 h는 모두 1과 100 사이의 값입니다.
(r과 h의 최소값은 1이고 최대값은 100입니다.)

출력
반지름이 r이고 높이가 h인 직원뿔의 부피를 출력합니다. 부피를 계산하는 공식은(ㅠr^2h)/3입니다.
"""

PI = 3.14

radius = int(input())
if not 1 <= radius <= 100:
  print("오류: 반지름은 1과 100사이의 값이여야 합니다.")
  exit();

height = int(input())
if not 1 <= height <= 100:
  print("오류: 높이는 1과 100사이의 값이여야 합니다.")
  exit();

volume = (PI * radius ** 2 * height) / 3

print(volume)
