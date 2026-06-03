from flask import Flask, render_template

app = Flask(__name__)

game_state = {
    "cash": 0,
    "production-rate": 1
}

@app.route('/')
def index():
    return render_template('index.html', money=game_state["cash"])

@app.route('/tick')
def tick():
    game_state["cash"] += game_state["production-rate"]
    return str(game_state["cash"])

if __name__ == '__main__':
    app.run(debug=True)