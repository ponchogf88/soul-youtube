from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

src = Path(__file__).resolve().parents[1] / "ORQUESTADOR_PRINCIPAL_24_7.md"
out = Path(__file__).resolve().parents[1] / "ORQUESTADOR_PRINCIPAL_24_7.pdf"
text = src.read_text(encoding="utf-8")
styles = getSampleStyleSheet()
title = ParagraphStyle("Title", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, leading=24, spaceAfter=16)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=14, leading=17, spaceBefore=10, spaceAfter=6)
body = ParagraphStyle("Body", parent=styles["BodyText"], fontSize=9, leading=13, spaceAfter=5)
story = []
for raw in text.splitlines():
    line = raw.strip()
    if not line:
        story.append(Spacer(1, 5)); continue
    if line.startswith("# "):
        story.append(Paragraph(line[2:], title))
    elif line.startswith("## "):
        story.append(Paragraph(line[3:], h1))
    elif line.startswith("### "):
        story.append(Paragraph(line[4:], h1))
    elif line.startswith("```"):
        continue
    elif line.startswith("-") or line[:2].isdigit():
        story.append(Paragraph("• " + line.lstrip("- "), body))
    else:
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        story.append(Paragraph(safe.replace("**", ""), body))
SimpleDocTemplate(str(out), pagesize=letter, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=42).build(story)
print(out)
