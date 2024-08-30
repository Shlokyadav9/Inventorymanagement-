Grocery Manager GUI
Description: The Grocery Manager GUI is a desktop application built using Python's Tkinter library. It allows users to search for customer transactions and view detailed information such as transaction ID, category, sub-category, city, sales, and profit. The application also integrates a simple machine learning model using scikit-learn to predict profit based on various transaction details.

Features:

Search Functionality: Users can search for transactions by customer name.
Data Loading: Transaction data is loaded from a CSV file and processed.
Machine Learning: The application uses a Linear Regression model to predict profit from sales data.
User-Friendly Interface: The GUI is designed with Tkinter, making it accessible and easy to use.
Installation:

Clone the repository to your local machine.
Install the required Python packages:
bash
Copy code
pip install pandas scikit-learn tkinter
Run the application:
bash
Copy code
python grocery_manager.py
Files:

grocery_manager.py: The main Python script containing the application code.
transactions.csv: The dataset used for the application.
Usage:

Enter a customer name in the input field and click "Search" to find their transaction details.
The application will display the results in the text box below.
Requirements:

Python 3.6+
pandas
scikit-learn
tkinter
