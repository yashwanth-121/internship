# from flask import Flask, request, render_template, redirect, flash
# import os
# import pandas as pd
# from single import process_data  # Import the process_data function from single.py

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder for uploaded files
# app.secret_key = 'your_secret_key'  # Required for flash messages

# # Ensure the upload folder exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Retrieve form data
#     sales = request.form.get('sales')
#     quantity = request.form.get('quantity')
#     shipping_cost = request.form.get('shipping_cost')
#     profit = request.form.get('profit')
#     discount = request.form.get('discount')
#     segment = request.form.get('segment')
#     category = request.form.get('category')
#     competitor_price = request.form.get('competitor_price')
    
#     # Check if a file is uploaded
#     file = request.files.get('file')

#     if file and file.filename.endswith('.csv'):
#         # Save the file to the upload folder
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)

#         # Load the uploaded CSV file into a pandas DataFrame
#         data = pd.read_csv(file_path)

#         # Process the data using the machine learning function
#         predictions = process_data(data)

#     else:
#         # If no file is uploaded, process the manually entered form data
#         if not all([sales, quantity, shipping_cost, profit, discount, segment, category, competitor_price]):
#             flash('Please fill out all form fields or upload a CSV file.')
#             return redirect(request.url)
        
#         # Create a dictionary with the form data
#         Order_id = 1
#         Product_id = 1
#         ship_date = 1
#         state = "TN"
#         order_priority = 1
#         year = "2024"
#         country = "India"
#         Prod_name = "Py"
#         Order_date = ""
#         Ship_mode = ""
#         market = ""
#         region = ""
#         sub = ""
#         form_data = {
#             'order_id': int(Order_id),
#             'product_id': int(Product_id),
#             'customer_name': "me",
#             'state': state,
#             'year': year,
#             'ship_date': ship_date,
#             'order_priority': order_priority,
#             'country': country,
#             'product_name': Prod_name,
#             'order_date': Order_date,
#             'ship_mode': Ship_mode,
#             'market': market,
#             'region': region,
#             'sub_category': sub,
#             'sales': float(sales),
#             'quantity': int(quantity),
#             'shipping_cost': float(shipping_cost),
#             'profit': float(profit),
#             'discount': float(discount),
#             'segment': segment,
#             'category': category,
#             'competitor_price': float(competitor_price)
#         }
#         # Convert the form data to a DataFrame
#         data = pd.DataFrame([form_data])

#         # Process the manually entered data
#         predictions = process_data(data)

#     # Convert predictions to HTML
#     predictions_html = predictions.to_html(classes='table table-striped')

#     # Render the results in result.html
#     return render_template('result.html', tables=[predictions_html])

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template, redirect, flash
import os
import pandas as pd
from single import process_data  # Import the process_data function from single.py

app = Flask(__name__)
#app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    sales = request.form.get('sales')
    quantity = request.form.get('quantity')
    shipping_cost = request.form.get('shipping_cost')
    profit = request.form.get('profit')
    discount = request.form.get('discount')
    segment = request.form.get('segment')
    category = request.form.get('category')
    competitor_price = request.form.get('competitor_price')
    
    # Check if a file is uploaded
    file = request.files.get('file')

    if file and file.filename.endswith('.csv'):
        # Load the uploaded CSV file directly into a pandas DataFrame without saving it
        data = pd.read_csv(file)

        # Process the data using the machine learning function
        predictions = process_data(data)

    else:
        # If no file is uploaded, process the manually entered form data
        if not all([sales, quantity, shipping_cost, profit, discount, segment, category, competitor_price]):
            flash('Please fill out all form fields or upload a CSV file.')
            return redirect(request.url)
        
        # Create a dictionary with the form data
        Order_id = 1
        Product_id = 1
        ship_date = 1
        state = "TN"
        order_priority = 1
        year = "2024"
        country = "India"
        Prod_name = "Py"
        Order_date = ""
        Ship_mode = ""
        market = ""
        region = ""
        sub = ""
        form_data = {
            'order_id': int(Order_id),
            'product_id': int(Product_id),
            'customer_name': "me",
            'state': state,
            'year': year,
            'ship_date': ship_date,
            'order_priority': order_priority,
            'country': country,
            'product_name': Prod_name,
            'order_date': Order_date,
            'ship_mode': Ship_mode,
            'market': market,
            'region': region,
            'sub_category': sub,
            'sales': float(sales),
            'quantity': int(quantity),
            'shipping_cost': float(shipping_cost),
            'profit': float(profit),
            'discount': float(discount),
            'segment': segment,
            'category': category,
            'competitor_price': float(competitor_price)
        }
        # Convert the form data to a DataFrame
        data = pd.DataFrame([form_data])

        # Process the manually entered data
        predictions = process_data(data)

    # Convert predictions to HTML
    predictions_html = predictions.to_html(classes='table table-striped')

    # Render the results in result.html
    return render_template('result.html', tables=[predictions_html])

if __name__ == '__main__':
    app.run(debug=True)






