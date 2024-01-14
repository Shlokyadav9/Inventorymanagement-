


import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression


class Transaction:
    def __init__(self, id, customer_name, category, sub_category, city, sales, profit):
        self.id = id
        self.customer_name = customer_name
        self.category = category
        self.sub_category = sub_category
        self.city = city
        self.sales = sales
        self.profit = profit


class GroceryManager:
    def __init__(self):
        # Load your data
        data = pd.read_csv('C:/Users/Shlok/OneDrive/Desktop/GMS/transactions.csv')


        data['Numeric ID'] = data['Order ID'].str.extract('(\d+)').astype(int)


        self.transactions = [Transaction(id=int(row['Numeric ID']), customer_name=row['Customer Name'], category=row['Category'], sub_category=row['Sub Category'], city=row['City'], sales=row['Sales'], profit=row['Profit']) for _, row in data.iterrows()]


        X = data.drop(['Order ID', 'Numeric ID', 'Customer Name'], axis=1)
        y = data['Profit']


        le = LabelEncoder()
        for col in ['Category', 'Sub Category', 'City']:
            X[col] = le.fit_transform(X[col])

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = LinearRegression()

        self.model.fit(X_train, y_train)

    def search_customer(self, customer_name):
        for transaction in self.transactions:
            if transaction.customer_name.lower() == customer_name.lower():
                return f"Transaction ID: {transaction.id}\nCategory: {transaction.category}\nSub Category: {transaction.sub_category}\nCity: {transaction.city}\nSales: {transaction.sales}\nProfit: {transaction.profit}"
        return f"No transaction found for the customer '{customer_name}'."

manager = GroceryManager()

class GroceryManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Grocery Manager GUI")

        self.master.geometry("600x400")

        self.style = ttk.Style()
        self.style.configure('TLabel', background='#EAEAEA')
        self.style.configure('TButton', background='#4CAF50', foreground='white')

        self.create_widgets()

    def create_widgets(self):
        self.label_customer_name = ttk.Label(self.master, text="Enter customer name:", style='TLabel')
        self.label_customer_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_customer_name = ttk.Entry(self.master)
        self.entry_customer_name.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = ttk.Button(self.master, text="Search", command=self.search_customer, style='TButton')
        self.search_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def search_customer(self):
        customer_name = self.entry_customer_name.get()

        result = manager.search_customer(customer_name)

        self.result_text.delete(1.0, tk.END)  
        self.result_text.insert(tk.END, result)

root = tk.Tk()
app = GroceryManagerGUI(root)

root.mainloop()


#code 2

# import tkinter as tk
# from tkinter import ttk
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.linear_model import LinearRegression

# class Transaction:
#     def __init__(self, id, customer_name, category, sub_category, city, sales, profit):
#         self.id = id
#         self.customer_name = customer_name
#         self.category = category
#         self.sub_category = sub_category
#         self.city = city
#         self.sales = sales
#         self.profit = profit

# class GroceryManager:
#     def __init__(self):
#         data = pd.read_csv('C:/Users/Shlok/OneDrive/Desktop/GMS/transactions.csv')

#         data['Numeric ID'] = data['Order ID'].str.extract('(\d+)').astype(int)

#         self.transactions = [Transaction(id=int(row['Numeric ID']), customer_name=row['Customer Name'], category=row['Category'], sub_category=row['Sub Category'], city=row['City'], sales=row['Sales'], profit=row['Profit']) for _, row in data.iterrows()]

#         X = data.drop(['Order ID', 'Numeric ID', 'Customer Name'], axis=1)
#         y = data['Profit']

#         le = LabelEncoder()
#         for col in ['Category', 'Sub Category', 'City']:
#             X[col] = le.fit_transform(X[col])

#         scaler = StandardScaler()
#         X = scaler.fit_transform(X)

#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#         self.model = LinearRegression()

#         self.model.fit(X_train, y_train)

#     def search_customer(self, customer_name):
#         for transaction in self.transactions:
#             if transaction.customer_name.lower() == customer_name.lower():
#                 return f"Transaction ID: {transaction.id}\nCategory: {transaction.category}\nSub Category: {transaction.sub_category}\nCity: {transaction.city}\nSales: {transaction.sales}\nProfit: {transaction.profit}"
#         return f"No transaction found for the customer '{customer_name}'."

# manager = GroceryManager()

# class GroceryManagerGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Grocery Manager GUI")

#         self.create_widgets()

#     def create_widgets(self):
#         self.label_customer_name = ttk.Label(self.master, text="Enter customer name:")
#         self.label_customer_name.grid(row=0, column=0, padx=10, pady=10)

#         self.entry_customer_name = ttk.Entry(self.master)
#         self.entry_customer_name.grid(row=0, column=1, padx=10, pady=10)

#         self.search_button = ttk.Button(self.master, text="Search", command=self.search_customer)
#         self.search_button.grid(row=1, column=0, columnspan=2, pady=10)

#         self.result_text = tk.Text(self.master, height=10, width=50)
#         self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#     def search_customer(self):
#         customer_name = self.entry_customer_name.get()

#         result = manager.search_customer(customer_name)

#         self.result_text.delete(1.0, tk.END)  # Clear previous content
#         self.result_text.insert(tk.END, result)


# root = tk.Tk()
# app = GroceryManagerGUI(root)


# root.mainloop()



#code 1


# import pandas as pd
# import os
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.linear_model import LinearRegression


# class Transaction:
#  def __init__(self, id, customer_name, category, sub_category, city, sales, profit):
#     self.id = id
#     self.customer_name = customer_name
#     self.category = category
#     self.sub_category = sub_category
#     self.city = city
#     self.sales = sales
#     self.profit = profit

# # Create the GroceryManager agent
# class GroceryManager:
#  def __init__(self):
#     
#     data = pd.read_csv('C:/Users/Shlok/OneDrive/Desktop/GMS/transactions.csv')

#     
#     data['Numeric ID'] = data['Order ID'].str.extract('(\d+)').astype(int)

#     
#     self.transactions = [Transaction(id=int(row['Numeric ID']), customer_name=row['Customer Name'], category=row['Category'], sub_category=row['Sub Category'], city=row['City'], sales=row['Sales'], profit=row['Profit']) for _, row in data.iterrows()]

#     
#     X = data.drop(['Order ID', 'Numeric ID', 'Customer Name'], axis=1)
#     y = data['Profit']

#    
#     le = LabelEncoder()
#     for col in ['Category', 'Sub Category', 'City']:
#         X[col] = le.fit_transform(X[col])

#     
#     scaler = StandardScaler()
#     X = scaler.fit_transform(X)

#    
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#   
#     self.model = LinearRegression()

# 
#     self.model.fit(X_train, y_train)

#  def search_customer(self, customer_name):
#     for transaction in self.transactions:
#         if transaction.customer_name.lower() == customer_name.lower():
#             return f"Transaction ID: {transaction.id}\nCategory: {transaction.category}\nSub Category: {transaction.sub_category}\nCity: {transaction.city}\nSales: {transaction.sales}\nProfit: {transaction.profit}"
#     return f"No transaction found for the customer '{customer_name}'."


# manager = GroceryManager()


# customer_name = input("Enter the name of the customer you want to search for: ")


# print(manager.search_customer(customer_name))




