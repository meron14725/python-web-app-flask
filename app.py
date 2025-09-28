from flask import Flask
from flask import render_template

app = Flask(__name__)

memo_list=[
    {'title':'memo1', 'body':'memo1の内容'},
    {'title':'memo2', 'body':'memo2の内容'},
    {'title':'memo3', 'body':'memo3の内容'},
    # {'title':'memo4', 'body':'memo4の内容'},
    # {'title':'memo5', 'body':'memo5の内容'},
    # {'title':'memo2', 'body':'memo2の内容'},
    # {'title':'memo2', 'body':'memo2の内容'},
    # {'title':'memo2', 'body':'memo2の内容'},
    # {'title':'memo2', 'body':'memo2の内容'},
    # {'title':'memo2', 'body':'memo2の内容'},
    # {'title':'memo2', 'body':'memo2の内容'},
    # {'title':'memo2', 'body':'memo2の内容'},
]

@app.route("/")
@app.route("/top")
def top():
    return render_template('index.html', memo_list=memo_list)

if __name__ == "__main__":
    app.run(debug=True)