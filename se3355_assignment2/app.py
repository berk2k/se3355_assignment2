from flask import Flask, render_template, request,abort
from product import db, Product



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:berkberk09@localhost:3306/se3355_assignment2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



'''
products = [
    Product(product_no=1, description="%100 Pamuk Slim Fit Dar Kesim Bisiklet Yaka Kısa Kollu Tshirt", price=90, image_url="ürün1.jpg",gender = "Erkek" ,category="Tshirt"),
    Product(product_no=2, description="Oversize Beyaz", price=75, image_url="ürün2.jpg",gender="Erkek", category="Tshirt"),
    Product(product_no=3, description="Mavi gömlek", price=100, image_url="ürün3.jpg",gender="Kadın", category="Gömlek"),
    Product(product_no=4, description="Siyah Tayt", price=40, image_url="ürün4.jpg",gender="Kadın", category="Tayt"),
    Product(product_no=5, description="Mavi Kot Pantalon", price=70, image_url="ürün5.jpg",gender="Erkek", category="Pantalon"),
    Product(product_no=6, description="Yeşil Pantalon", price=80, image_url="ürün6.jpg",gender="Kadın", category="Pantalon"),
    Product(product_no=7, description="Siyah Hoodie", price=120, image_url="ürün7.jpg",gender="Erkek", category="Hoodie"),
    Product(product_no=8, description="Beyaz Hoodie", price=110, image_url="ürün8.jpg",gender="Kadın", category="Hoodie"),
    Product(product_no=9, description="Curry 2", price=140, image_url="ürün9.jpg",gender="Erkek", category="Ayakkabı"),
    Product(product_no=10, description="Siyah Spor Ayakkabı", price=140, image_url="ürün10.jpg",gender="Kadın", category="Ayakkabı"),
]
'''


@app.route('/', methods=['GET', 'POST'])
def home():

    products = Product.query.all()
    return render_template('home.html', products=products)       

@app.route('/search', methods=['GET', 'POST'])
def search():
    searched = request.args.get('searched', '')
    if searched:
        search_results = Product.query.filter(Product.description.ilike(f'%{searched}%') | Product.category.ilike(f'%{searched}%'))
    else:
        search_results = Product.query.all()
    return render_template('search.html', search_results=search_results)   

@app.route('/details/<int:product_no>')
def details(product_no):
    product = Product.query.get(product_no)
    
    if product is None:
        abort(404)  

    return render_template('details.html', product=product)

@app.route('/category/<category>')
def category(category):
    products = Product.query.filter_by(category=category).all()
    return render_template('category.html', products=products)



if __name__ == '__main__':
    app.run(debug=True)
