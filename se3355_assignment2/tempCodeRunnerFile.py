@app.route('/', methods=['GET', 'POST'])
def home():

    products = Product.query.all()
    return render_template('home.html', products=products)