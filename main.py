from flask import Flask, render_template, request
from scrap.main import search_products

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/', methods=['POST'])
def search_word():
    word = request.form['word']
    print(word)
    products = search_products(word)

    return render_template('products.html', products = products)

if __name__ == "__main__":
    app.run(debug=True)
