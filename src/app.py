from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
import time
import os

app = Flask(__name__)


#Datbase transaction
def insert_word(original_word, mirrored_word):
    connection = None
    try:
        for i in range(10):  # Retry up to 10 times
            try:
                connection = mysql.connector.connect(
                    host=os.getenv('MYSQL_HOST'),
                    user=os.getenv('MYSQL_USER'),
                    password=os.getenv('MYSQL_PASSWORD'),
                    database=os.getenv('MYSQL_DATABASE')
                )
                if connection.is_connected():
                    print('Successfully connected to the database')
                    cursor = connection.cursor()
                    sql = "INSERT INTO words (original_word, mirrored_word) VALUES (%s, %s)"
                    values = (original_word, mirrored_word)
                    cursor.execute(sql, values)
                    connection.commit()
                    # cursor.execute("SELECT DATABASE();")
                    # record = cursor.fetchone()
                    # print(f'Connected to: {record}')
                    break  # Exit loop on successful connection
            except Error as e:
                print(f'Attempt {i+1}: Error - {e}')
                time.sleep(5)  # Wait before retrying
    except Exception as e:
        print(f'Unexpected error: {e}')
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('Connection closed')

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

    insert_word(word,result)
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