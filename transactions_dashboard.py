import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bank Transactions Dashboard", layout="centered")

st.title("🏦 Banking Transactions Dashboard")
st.markdown("Upload a CSV file with transaction data to explore trends.")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.dataframe(df)

    # Drop missing values
    df = df.dropna()

    # Clean column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    if 'amount' in df.columns:
        st.subheader("💡 Summary Stats")
        st.metric("Total Amount", f"${df['amount'].sum():,.2f}")
        st.metric("Average Amount", f"${df['amount'].mean():,.2f}")
        st.metric("Transactions", f"{len(df)}")

        st.subheader("📈 Amount Distribution")
        fig, ax = plt.subplots()
        df['amount'].hist(bins=20, ax=ax)
        ax.set_title("Transaction Amounts")
        ax.set_xlabel("Amount")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
    else:
        st.warning("No 'amount' column found. Please upload a valid CSV.")

else:
    st.info("👈 Upload a CSV to begin.")
