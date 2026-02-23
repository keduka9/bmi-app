# 例外処理の練習
def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return None
    
# テスト
print(safe_float("169"))    # 169.0
print(safe_float("abc"))    # None
print(safe_float(""))       # None
print(safe_float("1.75"))   # 1.75