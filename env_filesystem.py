import os
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def save_text(filename, data):
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)
    print(f"[Filesystem] File saved: {os.path.abspath(path)}") 


def save_summary(reviews, filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        for review in reviews:
            f.write("Pros: " + ", ".join(review["pros"]) + "\n")
            f.write("Cons: " + ", ".join(review["cons"]) + "\n\n")
    print(f"[Filesystem] Saved summary to: {path}")

def save_pdf(data, filename):
    path = os.path.join(BASE_DIR, filename)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Renewable Energy Report", ln=True, align='C')
    pdf.ln(10)
    for k, v in data.items():
        pdf.cell(200, 10, txt=f"{k}: {v:.2f}", ln=True)
    pdf.output(path)
    print(f"[Filesystem] Saved PDF to: {path}")
