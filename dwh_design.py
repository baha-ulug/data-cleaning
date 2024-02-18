DWH_db_marketplace_create = """CREATE TABLE marketplace (
    mkp_id SERIAL PRIMARY KEY,
    mkp_name VARCHAR(255)
);"""

DWH_db_product_create = """CREATE TABLE product (
    sku_id SERIAL PRIMARY KEY,
    item_sale_price NUMERIC,
    title VARCHAR(255),
    supplier_name VARCHAR(255)
);"""

DWH_db_courier_create = """
CREATE TABLE courier (
    courier_id SERIAL PRIMARY KEY,
    courier_name VARCHAR(255)
);"""


DWH_db_orders_create =  """CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    mkp_id INT,
    sku_id INT,
    order_date_id INT,
    courier_id INT,
    ordoro_id VARCHAR(255),
    item_sale_price NUMERIC,
    item_tax NUMERIC,
    shipping_sale NUMERIC,
    total_per_sku NUMERIC,
    order_status VARCHAR(255),
    item_cost NUMERIC,
    cancelled_value NUMERIC,
    transport_cost_est NUMERIC,
    first_pick_date TIMESTAMP,
    last_delivery_date TIMESTAMP,
    mage_mkp_commission NUMERIC,
    mkp_estimated_commission NUMERIC,
    mkp_actual_commission NUMERIC,
    order_grand_total NUMERIC,
    ordoro_import_date DATE,
    tool_import_date DATE,
    max_shipping_date DATE,
    max_delivery_date DATE,
    cd_status VARCHAR(255),
    is_clogistique_order VARCHAR(3),
    line_status VARCHAR(255),
    transport_cost_actual NUMERIC,
    order_place_time INT,
    order_prep_time INT,
    order_delivery_time INT,
    order_total_time INT,
    gm_estimated NUMERIC,
    FOREIGN KEY (mkp_id) REFERENCES marketplace(mkp_id),
    FOREIGN KEY (sku_id) REFERENCES product(sku_id),
    FOREIGN KEY (courier_id) REFERENCES courier(courier_id)
);"""
