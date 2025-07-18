import streamlit as st
import pandas as pd
from data_loader import load_and_clean_data
from report_generator import generate_visuals, generate_summary, create_pdf_report
from email_sender import send_email_report

st.set_page_config(layout="wide")
st.title("Kidney Lab Report Automation Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload CSV Lab Report File", type=["csv"])

if uploaded_file:
    with st.spinner("Processing file..."):
        # Save uploaded file to data dir
        file_path = fr"D:\Work_USA\Projects\lab-report-automation\data/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Load and process data
        df, _ = load_and_clean_data(file_path)

        # Show dataframe preview
        st.subheader("🔍 Lab Data Preview")
        st.dataframe(df.head(10), use_container_width=True)

        # Generate and display visual
        st.subheader("Select age range for visualization")
        age_bins = [0,10,20,30,40,50,60,70,80,90,100]
        age_labels = [f"{age_bins[i]}-{age_bins[i+1]}" for i in range(len(age_bins)-1)]
        selected_age_range = st.selectbox("Select the range", age_labels)

        age_low, age_high = map(int, selected_age_range.split('-'))
        filtered_df = df[(df['age'] >= age_low) & (df['age'] <= age_high)]

        st.subheader("📈 Age vs Serum Creatinine")
        visual_path = generate_visuals(filtered_df)
        st.image(visual_path)

        # Show summary
        st.subheader("📝 Summary")
        summary_text = generate_summary(df)
        st.code(summary_text)

        # Generate PDF
        if st.button("📄 Generate PDF Report"):
            pdf_path = create_pdf_report(summary_text, visual_path)
            st.success("Report generated!")
            with open(pdf_path, "rb") as f:
                st.download_button("⬇️ Download Report", data=f, file_name="lab_report.pdf")

        # Optional: Email functionality
        st.subheader("✉️ Send Report via Email (Optional)")
        email = st.text_input("Recipient Email")
        if st.button("Send Email") and email:
            pdf_path = create_pdf_report(summary_text, visual_path)
            send_email_report(
                subject="Kidney Lab Report",
                body="Attached is your diagnostic lab report.",
                to_email=email,
                attachment_path=pdf_path
            )
            st.success("Email sent!")
