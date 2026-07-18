#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-18 01:46:53.764178

import re
import email

def is_phishing(email):
    # Check if the email contains any suspicious links or attachments
    for part in email.iter_parts():
        if part.get_content_type() == "text/html":
            soup = BeautifulSoup(part.get_payload(), "html.parser")
            if soup.find("a", href=re.compile(r"(\bhttp://)|(https://)")):
                return True
        elif part.get_content_type() == "application/pdf":
            # Check if the PDF contains any malicious code
            with open(part, "rb") as f:
                pdf = PyPDF2.PdfFileReader(f)
                for page in range(pdf.getNumPages()):
                    text = pdf.getPage(page).extractText()
                    if re.search(r"(\bhttp://)|(https://)", text):
                        return True
    # Check if the email contains any suspicious headers
    for header in email.items():
        if header[0].lower().startswith("x-phishing"):
            return True
    # Check if the email contains any suspicious content
    if re.search(r"\bhttp://|https://", email.get_payload()):
        return True
    return False