from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Generate a random number between 1 and 100
target =    random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global target
    user_guess = request.json.get('guess')
    
    if user_guess.upper() == 'Q':
        return jsonify({'message': 'Game Over! You quit the game.'})

    try:
        guess = int(user_guess)
    except ValueError:
        return jsonify({'message': 'Please enter a valid number between 1 and 100.'})
    
    if guess < 1 or guess > 100:
        return jsonify({'message': 'Please enter a number between 1 and 100.'})
    
    if guess == target:
        target = random.randint(1, 100)  # Reset the target for a new game
        return jsonify({'message': 'Success: Correct Guess!! Game Over!'})
    elif guess < target:
        return jsonify({'message': 'Your number was too small. Take a bigger guess.'})
    else:
        return jsonify({'message': 'Your number was too big. Take a smaller guess.'})

if __name__ == '__main__':
    app.run(debug=True)
