from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['authentication']
collection = db['users']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        image_indexes = [
            request.form['imageIndex1'],
            request.form['imageIndex2'],
            request.form['imageIndex3']
        ]
        pattern_index = request.form['patternIndex']
        color = request.form['color']

        # Check if the username already exists
        existing_user = collection.find_one({'username': username})
        if existing_user:
            return "Username already exists. Please choose a different username."

        # Store the data in MongoDB
        user_data = {
            'username': username,
            'password': password,
            'image_indexes': image_indexes,
            'pattern_index': pattern_index,
            'color': color,
            'image_order': image_indexes,
            'pattern': pattern_index  # Add pattern to user data
        }
        collection.insert_one(user_data)

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query MongoDB to check if user exists
        user = collection.find_one({'username': username})
        if user:
            # Check if the username and password match
            if user['password'] == password:
                session['username'] = username  # Store username in session
                return redirect(url_for('image_order'))
            else:
                return redirect(url_for('login_failed', message='Incorrect password'))
        else:
            return redirect(url_for('login_failed', message='User does not exist'))

    return render_template('login.html')


@app.route('/image_order', methods=['GET', 'POST'])
def image_order():
    if request.method == 'POST':
        username = session.get('username')
        if not username:
            return redirect(url_for('login_failed', message='Session expired. Please login again.'))

        # Validate image order
        image1 = request.form['image1']
        image2 = request.form['image2']
        image3 = request.form['image3']
        user = collection.find_one({'username': username})
        if user['image_order'] == [image1, image2, image3]:
            return redirect(url_for('pattern'))
        else:
            return redirect(url_for('login_failed', message='Incorrect image order'))

    return render_template('image_order.html')


@app.route('/pattern', methods=['GET', 'POST'])
def pattern():
    if request.method == 'POST':
        username = session.get('username')
        if not username:
            return redirect(url_for('login_failed', message='Session expired. Please login again.'))

        # Validate pattern
        pattern = request.form['pattern']
        user = collection.find_one({'username': username})
        if user['pattern'] == pattern:
            return redirect(url_for('color'))
        else:
            return redirect(url_for('login_failed', message='Incorrect pattern'))

    # Exclude username and password from the context passed to the template
    return render_template('pattern.html')


@app.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'POST':
        username = session.get('username')
        if not username:
            return redirect(url_for('login_failed', message='Session expired. Please login again.'))

        # Validate color
        color = request.form['color']
        user = collection.find_one({'username': username})
        if user['color'] == color:
            return redirect(url_for('login_successful', username=username))
        else:
            return redirect(url_for('login_failed', message='Incorrect color'))

    return render_template('color.html')


@app.route('/login_successful')
def login_successful():
    username = session.get('username')
    if username:
        return render_template('login_successful.html', username=username)
    else:
        return redirect(url_for('login_failed', message='Session expired. Please login again.'))

@app.route('/login_failed')
def login_failed():
    message = request.args.get('message', 'Invalid username or password. Please try again.')
    return render_template('login_failed.html', message=message)

@app.route('/logout')
def logout():
    # Clear the session
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
