from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bmi.db"
db = SQLAlchemy(app)

# データベースのテーブル定義
class BmiRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    judgment = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

def bmi_calculator(height, weight):
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def bmi_judgment(bmi):
    if bmi < 18.5:
        return "低体重"
    elif bmi < 25:
        return "普通体重"
    elif bmi < 30:
        return "肥満（1度）"
    else:
        return "肥満（2度以上）"

@app.route("/")
def index():
    return render_template("index.html")    

def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return None

@app.route("/result", methods=["POST"])
def result(): 
    index_height = request.form.get("height", "")
    index_weight = request.form.get("weight", "")

    
    height_val = safe_float(index_height)
    weight_val = safe_float(index_weight)

    if height_val is None or weight_val is None:
        message = "数字を入力してください。"
        return render_template("index.html", message=message)

    height = float(index_height) / 100    # cmをmに変換
    weight = float(index_weight)
    
    if height <= 0 or weight <= 0:
        message = "0より大きい数値を入力してください。"
        return render_template("index.html", message=message)
            
    bmi = bmi_calculator(height, weight)
    judgment = bmi_judgment(bmi)

    # データベースに保存
    record = BmiRecord(height=height, weight=weight, bmi=bmi, judgment=judgment)
    db.session.add(record)
    db.session.commit()

    return render_template("result.html", bmi=bmi, judgment=judgment)

@app.route("/history")
def history():
    records = BmiRecord.query.order_by(BmiRecord.created_at.desc()).all()
    return render_template("history.html", records=records)

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    
    # この書き方は非推奨 record = BmiRecord.query.get(id)
    record = db.session.get(BmiRecord, id)
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for('history'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)