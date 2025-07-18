import matplotlib.pyplot as plt
import seaborn as sns
import os
from fpdf import FPDF

def generate_visuals(df, out_dir=r"D:\Work_USA\Projects\lab-report-automation\src\visualizations"):
    os.makedirs(out_dir, exist_ok=True)
    plot_path = os.path.join(out_dir, "age_vs_creatinine.png")
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x='age', y='sc', hue='classification')
    plt.title("Age vs Serum Creatinine")
    plt.savefig(plot_path)
    return plot_path

def generate_summary(df):
    ckd_ratio = df['classification'].mean()
    avg_age = df['age'].mean()
    avg_creatinine = df['sc'].mean()
    return f"""
CKD Patient Summary:
- % CKD Cases: {ckd_ratio * 100:.2f}%
- Avg Age: {avg_age:.1f} years
- Avg Serum Creatinine: {avg_creatinine:.2f} mg/dL
"""

def create_pdf_report(summary_text, image_path, output_path=r"D:\Work_USA\Projects\lab-report-automation\src\reports/lab_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary_text)
    pdf.image(image_path, x=10, y=80, w=180)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    return output_path
