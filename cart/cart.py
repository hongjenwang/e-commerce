from store.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        cart = self.session.get('session_key', {})

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product.id)  # Use product ID
        product_qty = int(quantity)
        if product_id in self.cart:
            self.cart[product_id] += product_qty
        else:
            self.cart[product_id] = product_qty

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart).replace("'", '"')
            current_user.update(old_cart=carty)

    def add(self, product, quantity):
        product_id = str(product.id)  # Use product ID
        product_qty = int(quantity)
        if product_id in self.cart:
            self.cart[product_id] += product_qty
        else:
            self.cart[product_id] = product_qty

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart).replace("'", '"')
            current_user.update(old_cart=carty)

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total = 0
        for product in products:
            quantity = self.cart[str(product.id)]
            if product.is_sale:
                total += product.sale_price * quantity
            else:
                total += product.price * quantity
        return total

    def __len__(self):
        return sum(self.cart.values())

    def get_prods(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.cart

    def update(self, product, quantity):
        product_id = str(product.id)  # Use product ID
        product_qty = int(quantity)
        self.cart[product_id] = product_qty
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart).replace("'", '"')
            current_user.update(old_cart=carty)

    def delete(self, product):
        product_id = str(product)
		# Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

		# Deal with logged in user
        if self.request.user.is_authenticated:
			# Get the current user profile
	        current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
	        carty = str(self.cart)
	        carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
	        current_user.update(old_cart=str(carty))
