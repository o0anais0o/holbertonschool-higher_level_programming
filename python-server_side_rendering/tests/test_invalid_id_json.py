response = requests.get("http://localhost:5000/products?source=json&id=999")
assert 'Product not found' in response.text
