import streamlit as st
import pandas as pd

def calculate_fcc_margin(feedstock, products, operating_costs):
    feedstock_cost = feedstock['volume'] * feedstock['price_per_bbl']
    total_revenue = sum(p['volume'] * p['price_per_bbl'] for p in products)
    fcc_margin = total_revenue - feedstock_cost - operating_costs
    fcc_margin_per_bbl = fcc_margin / feedstock['volume']
    return fcc_margin, fcc_margin_per_bbl

st.title("📊 FCC Margin Tracker")

# Feedstock Input
st.subheader("Feedstock Details")
feedstock_name = st.text_input("Feedstock Name", "Vacuum Gas Oil (VGO)")
feedstock_volume = st.number_input("Feedstock Volume (bbl)", min_value=1, value=10000)
feedstock_price = st.number_input("Feedstock Price ($/bbl)", min_value=1.0, value=80.0)

feedstock = {"name": feedstock_name, "volume": feedstock_volume, "price_per_bbl": feedstock_price}

# Product Yields
st.subheader("Product Yields & Prices")
num_products = st.number_input("Number of FCC Products", min_value=1, value=4)
products = []

for i in range(num_products):
    with st.expander(f"Product {i+1}"):
        product_name = st.text_input(f"Product {i+1} Name", value=f"Product {i+1}")
        product_volume = st.number_input(f"{product_name} Volume (bbl)", min_value=0, value=2000)
        product_price = st.number_input(f"{product_name} Price ($/bbl)", min_value=0.0, value=75.0)
        products.append({"name": product_name, "volume": product_volume, "price_per_bbl": product_price})

# Operating Costs
st.subheader("Operating Costs")
operating_costs = st.number_input("Total Operating Costs ($)", min_value=0, value=50000)

# Calculate FCC Margin
fcc_margin, fcc_margin_per_bbl = calculate_fcc_margin(feedstock, products, operating_costs)

# Display Results
st.subheader("FCC Margin Calculation")
st.write(f"### Total FCC Margin: **${fcc_margin:,.2f}**")
st.write(f"### FCC Margin per Barrel: **${fcc_margin_per_bbl:.2f}/bbl**")

# Summary Table
data = pd.DataFrame(products)
data["Total Revenue"] = data["volume"] * data["price_per_bbl"]
st.dataframe(data)