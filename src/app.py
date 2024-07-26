from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/')
def hello_world():
    return get_hello_world()

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/api/mirror', methods=['GET'])
def mirror():
    # Get the 'word' parameter from the query string
    word = request.args.get('word', '')
    # Process the word using the swap_case_and_reverse function
    result = swap_case_and_reverse(word)
    # Return the result as JSON
    return jsonify({"transformed": result})

def swap_case_and_reverse(s: str) -> str:
    # Swap cases of all alphabetic characters
    swapped = s.swapcase()
    # Reverse the entire string
    reversed_swapped = swapped[::-1]
    return reversed_swapped

def get_hello_world():
    return 'Hello, World!'

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')