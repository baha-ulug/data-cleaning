# Project README

## Overview
This project involves data cleaning, exploratory data analysis (EDA), and model creation using a dataset related to order line data from various marketplaces. The dataset contains information about different types of order lines, including details such as marketplace order numbers, order dates, product SKUs, prices, shipping information, order statuses, and various timestamps related to the order processing.

## Dataset Description
The dataset consists of the following columns:
- **line_type**: Describes the type of order line (ORDER LINE, FULL REPLACEMENT, PART REPLACEMENT).
- **mkp_name**: Name of the marketplace where the order was placed.
- **mkp_order_no**: Marketplace order number.
- **order_date**: Date and time of the order.
- **ordoro_id**: Internal order ID.
- **sku**: Product SKU.
- **item_sale_price**: Price charged to the customer for the item.
- **item_tax**: Always 0.
- **shipping_sale**: Shipping price charged to the customer.
- **total_per_sku**: Total price charged to the customer.
- **title**: Product title.
- **supplier_name**: Supplier name.
- **order_status**: Status of the order (e.g., Awaiting Fulfilment, Cancelled, Shipped).
- **item_cost**: Cost of the item.
- **cancelled_value**: Net value of cancelled items.
- **transport_cost_est**: Estimated transport cost.
- **first_pick_date**: Date of the first parcel pick-up.
- **last_delivery_date**: Date of the last delivered parcel.
- **courier**: Name of the courier company used.
- **mage_mkp_commission**: Extra fee charged by some marketplaces.
- **mkp_estimated_commission**: Estimated commission charged by the marketplace.
- **mkp_actual_commission**: Actual commission charged by the marketplace.
- **order_grand_total**: Total price charged to customers including commissions.
- **ordoro_import_date**: Date order was imported to Ordoro.
- **tool_import_date**: Date order was imported to the Tool.
- **max_shipping_date**: Max target shipping date for an order.
- **max_delivery_date**: Max target delivery date for an order.
- **cd_status**: Status information for specific marketplaces.
- **is_clogistique_order**: Flag indicating FBA type fulfillment.
- **line_status**: Segmentation of statuses.
- **transport_cost_actual**: Actual transport costs.
- **order_place_time**: Time taken to place order with supplier.
- **order_prep_time**: Time taken by the supplier to ship order.
- **order_delivery_time**: Time taken by courier to deliver.
- **order_total_time**: Sum of all time from order to delivery.
- **gm_estimated**: Estimated gross margin per order.

## Tasks Performed
1. **Data Cleaning**: The dataset underwent cleaning procedures to handle missing values, incorrect data types, and inconsistencies.
2. **Exploratory Data Analysis (EDA)**: Exploratory data analysis was conducted to gain insights into the distribution of variables, identify patterns, outliers, and relationships among features.
3. **Model Creation**: Various models might have been created using machine learning algorithms depending on the project objectives, such as regression for sales prediction or classification for order status prediction.

## Key Findings
- Insights gained from exploratory data analysis.
- Model performance metrics and evaluation results.

## Files
- **data.csv**: Cleaned dataset used for analysis.
- **order_line.ipynb**: Jupyter Notebook containing the code for data cleaning and EDA.
- **ecommerce.ipynb**: Jupyter Notebook containing the code for EDA, and model creation.
- **model.pkl**: Serialized model object saved for future use. (It will be added)

## Dependencies
- Python
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

## Instructions for Use
1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Open the Jupyter Notebook `notebook.ipynb` to access the code.
4. Execute the cells in the notebook to perform data cleaning, EDA, and model creation.
5. Use the saved model object `model.pkl` for predictions or analysis as needed.

