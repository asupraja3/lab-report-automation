import streamlit as st
import pandas as pd
from data_loader import load_and_clean_data
from report_generator import generate_visuals, generate_summary, create_pdf_report
from email_sender import send_email_report

st.set_page_config(layout="wide")
st.title("🧪 Kidney Lab Report Automation Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload CSV Lab Report File", type=["csv"])

if uploaded_file:
    with st.spinner("Processing file..."):
        # Save uploaded file to data dir
        file_path = f"D:\Work_USA\Projects\lab-report-automation\data/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Load and process data
        df, _ = load_and_clean_data(file_path)

        # Show dataframe preview
        st.subheader("🔍 Lab Data Preview")
        st.dataframe(df.head(10), use_container_width=True)

        # Generate and display visual
        st.subheader("📈 Age vs Serum Creatinine")
        visual_path = generate_visuals(df)
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
