from flask import Flask, render_template
from scrap.main import search_products

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search/<string:word>', methods=['GET'])
def search_word(word):
    if (len(word) == 0):
        products = search_products()
    else:
        products = search_products(word)

    return render_template('products.html', products = products, len=len, range=range, int=int)

if __name__ == "__main__":
    app.run(debug=True)
