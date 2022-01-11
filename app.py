from flask import request

from pymongo import MongoClient
from flask import Flask, render_template, jsonify


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.childcare

## 메인페이지
@app.route('/')
def home():
    return render_template('mainPage.html')

@app.route('/postingPage')
def post():
    return render_template('postingPage.html')

@app.route('/detail', methods=['GET'])
def read_reviews():
    board_title = request.args.get('title')
    board_info = db.childcare.find_one({'title': '@@아파트'}, {'_id': False})

    print(board_info)
    return render_template('detail.html', title=board_info['title'],location=board_info['location'], population=board_info['population'],details=board_info['details'],cur_cnt=board_info['cur_cnt'], age=board_info['age'],phone=board_info['phone'])


@app.route('/postingPage', methods=['POST'])
def save_post():
    title_receive = request.form["title_give"]
    phone_receive = request.form["phone_give"]
    population_receive = request.form["population_give"]
    age_receive = request.form["age_give"]
    location_receive = request.form["location_give"]
    details_receive = request.form["details_give"]

    doc = {
        "title":title_receive,
        "phone":phone_receive,
        "population":population_receive,
        "age":age_receive,
        "location":location_receive,
        "details":details_receive,
        "cur_cnt": "0"
    }

    db.childcare.insert_one(doc)
    return jsonify({"msg":"게시글이 등록되었습니다"})

@app.route('/postingPage', methods=['DELETE'])
def delete_post():
    post_receive = request.form["post_give"]
    title_receive = request.form["title_give"]
    phone_receive = request.form["phone_give"]
    population_receive = request.form["population_give"]
    age_receive = request.form["age_give"]
    location_receive = request.form["locationpost_give"]
    details_receive = request.form["details_give"]

    doc = {
        "post": post_receive,
        "title": title_receive,
        "phone": phone_receive,
        "population": population_receive,
        "age": age_receive,
        "location": location_receive,
        "details": details_receive,
    }
    db.childcare.insert_one(doc)
    return jsonify({"msg":"게시글이 삭제되었습니다"})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

