from flask import Flask, render_template
from script.ores import generate_ore

app = Flask(__name__)

initial_ore = generate_ore()

game_state = {
    "cash": 0,
    "max_health": initial_ore._health,
    "current_health": initial_ore._health,
    "ore_name": initial_ore._name,
    "ore_reward": initial_ore._cash,
    "ore_image": initial_ore._image
}

@app.route('/')
def index():
    return render_template('index.html', state=game_state)

@app.route('/health')
def health():
    health_percent = (game_state["current_health"] / game_state["max_health"]) * 100
    return f'<div id="health-progress" hx-get="/health" hx-trigger="load" hx-swap="outerHTML" class="health-bar-progress" style="width: {health_percent}%;"></div>'

@app.route('/mine', methods=['POST'])
def mine():
    damage = 1
    game_state["current_health"] -= damage

    if game_state["current_health"] <= 0:
        game_state["cash"] += game_state["ore_reward"]
        
        new_ore = generate_ore()
        
        game_state["max_health"] = new_ore._health
        game_state["current_health"] = new_ore._health
        game_state["ore_name"] = new_ore._name
        game_state["ore_reward"] = new_ore._cash
        game_state["ore_image"] = new_ore._image

    health_percent = (game_state["current_health"] / game_state["max_health"]) * 100

    return f'''
    <div id="health-progress" hx-get="/health" hx-trigger="load" hx-swap="outerHTML"></div>
    
    <span id="money-display" hx-swap-oob="true">{game_state["cash"]}</span>
    
    <h2 id="ore-name" class="ore-display-name" hx-swap-oob="true">{game_state["ore_name"]}</h2>
    
    <img id="ore-image" src="/static/{game_state["ore_image"]}" alt="{game_state["ore_name"]}" class="ore-pixel-art-image" hx-swap-oob="true">
    '''

if __name__ == '__main__':
    app.run(debug=True)