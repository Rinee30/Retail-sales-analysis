from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report/final_report.pdf")
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("Retail Sales Data Analysis Report", styles["Title"]))
elements.append(Spacer(1, 20))

elements.append(Paragraph("1. Monthly Sales Trend", styles["Heading2"]))
elements.append(Image("report/monthly_sales.png", width=400, height=200))
elements.append(Spacer(1, 20))

elements.append(Paragraph("2. Top 10 Best-Selling Items", styles["Heading2"]))
elements.append(Image("report/top_items.png", width=400, height=200))

doc.build(elements)
print("✅ PDF Report Generated: report/final_report.pdf")
