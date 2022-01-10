from flask import Flask, render_template
app = Flask(__name__)

## 메인페이지
@app.route('/')
def home():
    return render_template('mainPage.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)