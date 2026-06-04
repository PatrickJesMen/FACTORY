from flask import Flask, render_template
from script.ores import generate_ore

app = Flask(__name__)

initial_ore = generate_ore()

# Estado do jogo mantido em memória
game_state = {
    "money": 0,
    "max_health": initial_ore["health"],
    "current_health": initial_ore["health"],
    "ore_name": initial_ore["name"],
    "ore_reward": initial_ore["cash"],
    "ore_image": initial_ore["image"]
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
        game_state["money"] += game_state["ore_reward"]
        game_state["current_health"] = game_state["max_health"]


        new_ore = generate_ore()

        game_state["max_health"] = new_ore["health"]
        game_state["current_health"] = new_ore["health"]
        game_state["ore_name"] = new_ore["name"]
        game_state["ore_reward"] = new_ore["cash"]
        game_state["ore_image"] = new_ore["image"]


    health_percent = (game_state["current_health"] / game_state["max_health"]) * 100

    return f'''
    <div id="health-progress" class="health-bar-progress" style="width: {health_percent}%;"></div>
    
    <span id="money-display" hx-swap-oob="true">{game_state["cash"]}</span>
    
    <h2 id="ore-name" class="ore-display-name" hx-swap-oob="true">{game_state["ore_name"]}</h2>
    
    <img id="ore-image" src="/static/{game_state["ore_image"]}" alt="{game_state["ore_name"]}" class="ore-pixel-art-image" hx-swap-oob="true">
    '''

if __name__ == '__main__':
    app.run(debug=True)