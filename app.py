from flask import Flask, render_template

app = Flask(__name__)

# Estado do jogo mantido em memória
game_state = {
    "money": 0,
    "max_health": 100,
    "current_health": 100
}

@app.route('/')
def index():
    return render_template('index.html', money=game_state["money"])

# Nova rota que renderiza a barra de vida sem dar erro no editor HTML
@app.route('/health')
def health():
    health_percent = (game_state["current_health"] / game_state["max_health"]) * 100
    return f'<div id="health-progress" class="health-bar-progress" style="width: {health_percent}%;"></div>'

@app.route('/mine', methods=['POST'])
def mine():
    damage = 20 
    game_state["current_health"] -= damage

    if game_state["current_health"] <= 0:
        game_state["current_health"] = game_state["max_health"]
        game_state["money"] += 50

    health_percent = (game_state["current_health"] / game_state["max_health"]) * 100

    return f'''
    <span id="money-display" hx-swap-oob="true">{game_state["money"]}</span>
    <div id="health-progress" class="health-bar-progress" style="width: {health_percent}%;" hx-swap-oob="true"></div>
    '''

if __name__ == '__main__':
    app.run(debug=True)