"""
CardGame - https://dmoj.ca/problem/ccc99s1

입력:
입력은 총 52줄로 구성됩니다. 각 라인에는 테크에 있는 카드 유형 중 하나가 포함되며,
플레이어가 데크에서 카드를 가져가는 순서대로 입력됩니다.
첫 번째 라인은 데크에서 가져온 첫 번째 카드이고, 두 번째 라인은 데크에서 가져온 두 번째 카드인 식입니다.

출력:
플레이어가 득점할 때마다 플레이어 X 득점 n점이라고 인쇄합니다.
여기서 X는 플레이어의 이름(A 또는 B)이고 n는 득점한 점수(1, 2, 3 또는 4)입니다.
게임이 끝나면 각 플레이어의 총 점수를 두 줄로 출력합니다.
"""

def calculate_scores(deck):
  high_cards = {'jack': 1, 'queen': 2, 'king': 3, 'ace': 4}
  player_scores = {'A': 0, 'B': 0}
  current_player = 'A'

  i = 0
  while i < len(deck):
    card = deck[i]
    if card in high_cards:
      required_cards = high_cards[card]
      if i + required_cards < len(deck) and all(deck[i + j] in high_cards for j in range(1, required_cards + 1)):
        player_scores[current_player] += required_cards
        print(f"Player {current_player} 득점 {required_cards}점")
    current_player = 'B' if current_player == 'A' else 'A'
    i += 1

  print(f"Player A: {player_scores['A']} point(s).")
  print(f"Player B: {player_scores['B']} point(s).")

# Example usage:
deck = [
  'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace',
  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace',
  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace',
  '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king'
]

calculate_scores(deck)
