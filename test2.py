# クラスの定義
class Person:
    # コンストラクタ（インスタンス生成時に自動で呼ばれる）
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # メソッド
    def greet(self):
        return f"こんにちは、{self.name}です。{self.age}歳です。"
    
    def is_adult(self):
        return self.age >= 18
    
# インスタンスの生成
person1 = Person("毛塚", 50)
person2 = Person("田中", 17)

print(person1.greet())
print(person2.is_adult())

# 練習問題
# BankAccount（銀行口座）クラスを作ってみてください。
# ・属性：口座名義（ower）、残高（balance）
# ・メソッド：
#       ・deposit(amount)  -> 入金する
#       ・withdraw(amount) -> 出金する（残高不足の場合は「残高不足です」と表示）
#       ・show_balance()   -> 残高を表示する

class BankAccount:
    def __init__(self, ower, balance):
        self.ower = ower
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"残高：{self.balance}円")

    def withdraw(self, amount):
        if self.balance < amount:
            print("残高不足です")
        else:
            self.balance -= amount
            print(f"残高：{self.balance}円")

    def show_balance(self):
        print(f"残高：{self.balance}円")

account = BankAccount("毛塚", 10000)
account.deposit(5000)
account.withdraw(3000)
account.withdraw(20000)
account.show_balance()
