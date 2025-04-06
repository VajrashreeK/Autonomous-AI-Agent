from fpdf import FPDF

def save_text(data, filename):
    with open(filename, 'w') as f:
        for line in data:
            f.write(f"{line}\n")

def save_summary(reviews, filename):
    with open(filename, 'w') as f:
        for review in reviews:
            f.write("Pros: " + ", ".join(review["pros"]) + "\n")
            f.write("Cons: " + ", ".join(review["cons"]) + "\n\n")

def save_pdf(data, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Renewable Energy Report", ln=True, align='C')
    pdf.ln(10)
    for k, v in data.items():
        pdf.cell(200, 10, txt=f"{k}: {v:.2f}", ln=True)
    pdf.output(filename)
