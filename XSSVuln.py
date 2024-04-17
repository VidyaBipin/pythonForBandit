from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('<h1>Welcome to our website!</h1>')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        # This is vulnerable to XSS
        return render_template_string('<h1>Search Results for: {{ query }}</h1>', query=query)
    else:
        return render_template_string('''
            <form method="post">
                <label for="query">Search:</label>
                <input type="text" id="query" name="query">
                <button type="submit">Search</button>
            </form>
        ''')

if __name__ == '__main__':
    app.run(debug=True)
