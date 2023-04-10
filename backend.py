

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')

@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')


@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')


@app.route('/ask', methods=['POST','GET'])
def ask():
    content = request.args.get('content')
    print(content)
    return jsonify(reply=content)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)

