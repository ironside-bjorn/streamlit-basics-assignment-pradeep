import streamlit as st
import pandas as pd
# Task 1: Setup the Data
data = {
    "Product": ["Wireless Mouse", "Mechanical Keyboard", "USB-C Cable", "Office Chair", "Desk Lamp", "Monitor Stand"],
    "Category": ["Electronics", "Electronics", "Accessories", "Furniture", "Furniture", "Accessories"],
    "Sales": [120, 450, 25, 300, 85, 60]
}

df = pd.DataFrame(data)

# App Branding
st.title("Sales Performance Dashboard")
st.subheader("Interactive summary for quick category analysis")

# Task 2: Sidebar and Visualization
# Move the filter to the sidebar
category_list = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select a Category:", category_list)

# Filter the data based on selection
filtered_df = df[df["Category"] == selected_category]

# Main Area Display
st.write(f"### {selected_category} Sales Data")
st.dataframe(filtered_df, use_container_width=True)

# Add a visual trend for the selected category
st.write("### Sales Trend")
st.line_path = st.line_chart(filtered_df.set_index("Product")["Sales"])
