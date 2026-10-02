from pyscript import display, document

def SKU_generator(e): # generates an SKU code for a product based on what is inputted
    document.getElementById('sku_output').innerHTML = " "
    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
    display("SKU: ", sku, target='sku_output')

def create_order(e):
# Get input values
    prod1 = document.getElementById("Cheese Burger")
    prod2 = document.getElementById("Fries")
    prod3 = document.getElementById("Cheese Pizza Slice")
    prod4 = document.getElementById("Coca Cola")
    prod5 = document.getElementById("Water")
    # Calculate total by multiplying value by checked status (1 or 0)
    # Calculate subtotal, tax, and total

    # subtotal checks if the prices are (checked), adds the total price of said products
    subtotal = (float(prod1.value) * prod1.checked +
    float(prod2.value) * prod2.checked +
    float(prod3.value) * prod3.checked +
    float(prod4.value) * prod4.checked +
    float(prod5.value) * prod5.checked)

    tax_rate = 0.12 # 12% VAT, no need for excise tax. too complicated
    tax = subtotal * tax_rate # multiply tax rate and subtotal to get the tax
    total = subtotal + tax

    # display(f"==== Receipt ==== <br> Subtotal: ₱ {subtotal:.2f} ", target="show")
    # display(f"Subtotal: ₱ {subtotal:.2f} ", target="show")
    # display(f"VAT: ₱ {tax:.2f} ", target="show")
    # display(f"Total: ₱ {total:.2f} ", target="show")
    receipt = f"""
    <h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>Tax: ₱{tax:.2f}</p>
    <p><strong>Total: ₱{total:.2f}</strong></p>
    """
    document.getElementById("show").innerHTML = receipt # use this instead of display to avoid displaying the HTML tags
