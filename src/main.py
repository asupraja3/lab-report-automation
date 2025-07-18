from src.data_loader import load_and_clean_data
from src.report_generator import generate_visuals, generate_summary, create_pdf_report
from src.email_sender import send_email_report


def main():
    filepath = r"D:\Work_USA\Projects\lab-report-automation\data\kidney_disease.csv"
    df, _ = load_and_clean_data(filepath)

    img_path = generate_visuals(df)
    summary = generate_summary(df)
    pdf_path = create_pdf_report(summary, img_path)

    send_email_report(
        subject="Automated CKD Lab Report",
        body="Please find attached the latest diagnostic report.",
        to_email="asupraja527@gmail.com",
        attachment_path=pdf_path
    )

if __name__ == "__main__":
    main()