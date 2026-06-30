import pdfplumber
import json
import os

PDF_FILE = "pdf/UOS_Bus_Complete_Info.pdf"

def extract_pdf():

    all_text = ""

    with pdfplumber.open(PDF_FILE) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                all_text += text + "\n"

            tables = page.extract_tables()

            for table in tables:

                for row in table:

                    row = [
                        str(cell).strip()
                        if cell else ""
                        for cell in row
                    ]

                    all_text += " | ".join(row) + "\n"

    return all_text


knowledge = {
    "source": PDF_FILE,
    "content": extract_pdf()
}

os.makedirs("data", exist_ok=True)

with open(
    "data/knowledge_base.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        knowledge,
        f,
        ensure_ascii=False,
        indent=4
    )

print("Knowledge base created")