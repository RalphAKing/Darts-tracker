from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/dartsgame')
def dartsgame():
    return render_template('dartsgame.html')

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

