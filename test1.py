# 通常のforループ
numbers = [1, 2, 3, 4, 5]
doubled = []

for n in numbers:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6, 8, 10]

# リスト内包表記（1行で書ける）
# 処理手順
#   1. for n in numbers
#       1.1 n -> 1
#           2. n * 2 -> 1 * 2
#               2.1 doubled.append(n) -> doubled = [2]
#       1.2 n -> 2
#           2. n * 2 -> 2 * 2
#               2.2 doubled.append(n) -> doubled = [2, 4]
#       1.3 n -> 3
#           2. n * 2 -> 3 * 2
#               2.3 doubled.append(n) -> doubled = [2, 4, 6]
#       1.4 n -> 4
#           2. n * 2 -> 4 * 2
#               2.4 doubled.append(n) -> doubled = [2, 4, 6, 8]
#       1.5 n -> 5
#           2. n * 2 -> 5 * 2
#               2.5 doubled.append(n) -> doubled = [2, 4, 6, 8, 10]
doubled = [n * 2 for n in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# 条件付き
# 1. for n in numbers
#   1.1 if n(1) % 2 == 0
#       1.1.1 n(1) % 2 == 0 -> False
#   1.2 if n(2) % 2 == 0
#       1.1.2 n(2) % 2 == 0 -> True
#           1.1.1.1 even.append(n) -> even = [2]
#   1.3 if n(3) % == 0
#       1.1.3 n(3) % 2 == 0 -> False
#   1.4 if n(4) % == 0
#       1.1.4 n(4) % 2 == 0 -> True
#           1.1.1.2 even.append(n) -> even = [2, 4]
#   1.5 if n(5) % == 0
#       1.1.5 n(5) % 2 == 0 -> False
# 2. print(even) -> [2, 4]
even = [n for n in numbers if n % 2 == 0]
print(even)     # [2, 4]

print("------------------------------------------------")
# 練習問題
# 以下の２つをリスト内包表記で書いてみてください。

# ⓵ 1から10の数字の中で、3の倍数だけを取り出したリスト
triple = [n for n in range(1, 11) if n % 3 == 0]
print(triple)

# ⓶ 以下の食べ物リストから、3文字以上の食べ物だけ取り出したリスト
foods = ["ラーメン", "寿司", "ナポリタン", "唐揚げ", "カツ丼"]
food_word = [n for n in foods if len(n) >= 3]
print(food_word)