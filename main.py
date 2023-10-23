import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Dummy data, gantilah dengan data sesuai kebutuhan
all_df = pd.read_csv("all_dataset.csv")

# Visualisasi Pertama
st.subheader("10 Negara Bagian Dengan Jumlah Pelanggan Aktif Terbanyak")
data1 = (
    all_df[all_df["status"] == "Active"]
    .groupby(by="customer_state")
    .customer_id.nunique()
    .sort_values(ascending=False)
    .reset_index()
    .head(10)
)
fig1, ax1 = plt.subplots()
sns.barplot(x="customer_id", y="customer_state", data=data1, palette="viridis", ax=ax1)
ax1.set_title("10 Negara Bagian Dengan Jumlah Pelanggan Aktif Terbanyak")
ax1.set_xlabel("Jumlah Pelanggan Unik")
ax1.set_ylabel("Negara Bagian")
st.pyplot(fig1)

# Visualisasi Kedua
st.subheader("Top 10 Kategori Produk Dengan Jumlah Penjualan Tertinggi")
grouped_data = (
    all_df.groupby(by="product_category_name_english")
    .agg({"order_id": "nunique"})
    .sort_values(by="order_id", ascending=False)
    .head(10)
    .reset_index()
)
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.barplot(
    x="order_id",
    y="product_category_name_english",
    data=grouped_data,
    palette="viridis",
    ax=ax2,
)
ax2.set_title("Top 10 Kategori Produk Dengan Jumlah Penjualan Tertinggi")
ax2.set_xlabel("Jumlah Pesanan")
ax2.set_ylabel("Kategori Produk")
st.pyplot(fig2)

# Visualisasi Ketiga
st.subheader("Top 10 Kategori Produk Dengan Omset Penjualan Tertinggi")
grouped_data = (
    all_df.groupby(by="product_category_name_english")
    .agg({"order_id": "nunique", "price": "sum"})
    .sort_values(by="price", ascending=False)
    .head(10)
    .reset_index()
)
fig3, ax3 = plt.subplots(figsize=(12, 6))
sns.barplot(
    x="price",
    y="product_category_name_english",
    data=grouped_data,
    palette="viridis",
    ax=ax3,
)
ax3.set_title("Top 10 Kategori Produk Dengan Omset Penjualan Tertinggi")
ax3.set_xlabel("Omset")
ax3.set_ylabel("Kategori Produk")
st.pyplot(fig3)

# Visualisasi Keempat
st.subheader("Top 10 Toko Dengan Penjual Terbanyak")
grouped_data = (
    all_df.groupby(by="seller_id")
    .agg({"order_id": "nunique", "price": "sum"})
    .sort_values(by="order_id", ascending=False)
    .head(10)
    .reset_index()
)
fig4, ax4 = plt.subplots(figsize=(12, 6))
sns.barplot(x="order_id", y="seller_id", data=grouped_data, palette="viridis", ax=ax4)
ax4.set_title("Top 10 Toko Dengan Penjual Terbanyak")
ax4.set_xlabel("Jumlah Pesanan")
ax4.set_ylabel("Penjual ID")
st.pyplot(fig4)

# Visualisasi Kelima
st.subheader("Payment Type Distribution")
grouped_data = (
    all_df.groupby(by="payment_type").agg({"payment_sequential": "sum"}).reset_index()
)

total_payments = grouped_data["payment_sequential"].sum()

grouped_data["percentage"] = (grouped_data["payment_sequential"] / total_payments) * 100

fig5, ax5 = plt.subplots(figsize=(8, 8))
ax5.pie(
    grouped_data["percentage"],
    labels=grouped_data["payment_type"],
    autopct="%1.1f%%",
    startangle=140,
)
ax5.set_title("Payment Type Distribution")
st.pyplot(fig5)

# Visualisasi Keenam
st.subheader("Perbandingan antara Penjualan dan Omset berdasarkan 10 State teratas")
grouped_data = (
    all_df.groupby(by=["customer_state"])
    .agg({"order_item_id": "sum", "price": "sum"})
    .sort_values(by="order_item_id", ascending=False)
    .head(10)
)

grouped_data = grouped_data.reset_index()

fig6, ax6 = plt.subplots(figsize=(12, 8))
sns.scatterplot(
    x="order_item_id", y="price", hue="customer_state", data=grouped_data, s=100, ax=ax6
)
ax6.set_xlabel("Total Order Items")
ax6.set_ylabel("Total Price")
ax6.set_title("Perbandingan antara Penjualan dan Omset berdasarkan 10 State teratas")
ax6.legend(title="Customer State", bbox_to_anchor=(1.05, 1), loc="upper left")
st.pyplot(fig6)
