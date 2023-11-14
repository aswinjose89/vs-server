@app.route('/unsafe_login', methods=['POST'])
def unsafe_login():
    username = request.form['username']
    password = request.form['password']

    # Unsafe SQL query construction
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)