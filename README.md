# Olist-business-analysis

## Introduction
Olist is a Brazilian startup that operates in the e-commerce segment , mainly through the marketplace. It is well spread within the country. This project is a detailed analysis on the comprehensive Olist data. The original Olist dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. The schema of the dataset is as below:-

* olist_order_customers_dataset - This dataset has information about the customer and its location. Use it to identify unique customers in the orders dataset and to find the orders delivery location.
* olist_geolocation_dataset - This dataset has information Brazilian zip codes and its lat/lng coordinates.
* olist_order_items_dataset - This dataset includes data about the items purchased within each order.
* olist_order_payments_dataset - This dataset includes data about the orders payment options.
* olist_order_reviews_dataset - This dataset includes data about the reviews made by the customers.
* olist_orders_dataset - This is the core dataset. Every necessary information is mapped to each order in this.
* olist_products_dataset - This dataset includes data about the products sold by Olist.
* olist_sellers_dataset - This dataset includes data about the sellers that fulfilled orders made at Olist.

Multiple analysis tasks are carried out on the dataset, ranging from descriptive analysis to forecasting and predictive analysis.

## Analysis
The various analysis tasks are listed and explained below:-

### Joining data
The original data is used to derive multiple datasets by joins and manipulations. The [Data manipulation and combinig](https://github.com/rajtulluri/Olist-business-analysis/blob/master/Notebooks/Data%20manipulation%20and%20combining.ipynb) jupyter notebook contains the step by step process and explanations. 
* customer_data - Maps customers to their locations in latitude and longitude
* customer_order - Maps each order to the customer and the products bought
* transaction_data - Transactional dataset
* customer_payment - Information on purchases and payment information aggregated for each customer
* delivery_data - Maps each customer's order to the seller fulfilling it and the seller's location
* product_reviews - Maps the reviews to the products

### Preliminary data analysis
The notebook [Preliminary Data analysis](https://github.com/rajtulluri/Olist-business-analysis/blob/master/Notebooks/Preliminary%20Data%20analysis.ipynb) contains the detailed analysis. This notebook visualizes and summarizes the original and the combined datasets, to find trends, patterns or faults. This analysis gives a holistic view of th dataset.

### Association rule mining
Using the transactional dataset created from the original dataset, association rule mining is performed using Frequent pattern algorithms - FP growth trees. The model returns frequent item sets with a confidence threshold of 10%. The [Association rule mining](https://github.com/rajtulluri/Olist-business-analysis/blob/master/Notebooks/Association%20rule%20mining.ipynb) notebook contains the detailed explanation for this task.

### Product analysis
The objective of this analysis is to find the most popular products, popular product categories and category wise popular products in the Olist ecosystem. Further, the delivery times and product characteristics such as - description lenght, number of photos etc, are compared to popularity to find correlations in the data. The [Product analysis](https://github.com/rajtulluri/Olist-business-analysis/blob/master/Notebooks/Product%20analysis.ipynb) notebook contains the detailed code.

### 

