from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

shalevImages = ['/static/css/shalev_omega.jpg', 'shalev_shleb.jpg', '/static/css/shalevs.jpg']
accessoriesImages = ['/static/css/shalevGlasses.png', '/static/css/shalevBackpack.avif', "/static/css/shalevChain.png"]
clothingImages = ['static/css/shalevShoes.webp', '/static/css/shalevJeans.png', '/static/css/shalevShirt.jpg']

@app.route('/')
def index():
	return render_template('home.html')


@app.route('/products/<string:productType>')
def products(productType):	
	return render_template('product.html',
		productType = productType,
		shalevImages = shalevImages,
		accessoriesImages = accessoriesImages,
		clothingImages =clothingImages)


@app.route('/cart')
def cart():
	return render_template('cart.html')

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
