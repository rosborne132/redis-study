from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Route to get a player's score
@app.route('/player/<player>', methods=['GET'])
def get_player_score(player):
    player_score = redis_client.get(str(player))

    if not player_score:
        return jsonify({ "message": "User does not exist" })

    return jsonify({ "score": int(player_score) })

# Route to update a player's score
@app.route('/update_score', methods=['POST'])
def update_score():
    data = request.get_json()
    player = data.get('player')
    score = data.get('score')
    
    if not player or not score:
        return jsonify({"error": "Player and score are required."}), 400
    
    # Update the player's score in Redis
    redis_client.set(player, score)
    
    return jsonify({"message": "Score updated successfully."})

if __name__ == '__main__':
    app.run(debug=True)
