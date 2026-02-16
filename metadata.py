import re

def extract_metadata(text, category):
    data = {}
    text_lower = text.lower()
    category_lower = category.lower()

    # ---------------------------
    # INVOICE
    # ---------------------------
    if "invoice" in category_lower:

        invoice_no = re.search(
            r"invoice\s*(number|no\.?|#)?[:\s]*([a-z0-9\-]+)",
            text_lower
        )

        total_amount = re.search(
            r"total\s*(amount|due)?[:\s]*\$?\s*([\d,]+(\.\d{2})?)",
            text_lower
        )

        date = re.search(
            r"(invoice\s*date|date)[:\s]*([a-z0-9,\-/ ]+)",
            text_lower
        )

        data["invoice_number"] = invoice_no.group(2) if invoice_no else None
        data["total_amount"] = total_amount.group(2) if total_amount else None
        data["date"] = date.group(2).strip() if date else None


    # ---------------------------
    # EMAIL
    # ---------------------------
    elif "email" in category_lower:

        pattern = r"""
            from:\s*([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,})\s*
            to:\s*([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,})\s*
            subject:\s*(.*?)\s*
            body:\s*(.*?)(?=from:|\Z)
        """

        matches = re.findall(pattern, text_lower, re.DOTALL | re.VERBOSE)

        emails = []

        for match in matches:
            sender, recipient, subject, body = match

            emails.append({
                "sender": sender.strip(),
                "recipient": recipient.strip(),
                "subject": subject.strip(),
                "body": body.strip()
            })

        data["emails"] = emails if emails else None


    # ---------------------------
    # SCIENTIFIC DOCUMENT
    # ---------------------------
    elif "scientific" in category_lower:

        title = re.search(r"(title)[:\s]*(.+)", text_lower)
        author = re.search(r"(author[s]?)[:\s]*(.+)", text_lower)
        abstract = re.search(r"(abstract)[:\s]*(.+)", text_lower)

        data["title"] = title.group(2).strip() if title else None
        data["author"] = author.group(2).strip() if author else None
        data["abstract"] = abstract.group(2).strip() if abstract else None


    # ---------------------------
    # PROJECT REPORT
    # ---------------------------
    elif "project report" in category_lower:

        title = re.search(r"(project\s*title|title)[:\s]*(.+)", text_lower)
        team = re.search(r"(team\s*members?|members?)[:\s]*(.+)", text_lower)
        supervisor = re.search(r"(supervisor|advisor)[:\s]*(.+)", text_lower)

        data["project_title"] = title.group(2).strip() if title else None
        data["team_members"] = team.group(2).strip() if team else None
        data["supervisor"] = supervisor.group(2).strip() if supervisor else None


    # ---------------------------
    # RESUME
    # ---------------------------
    elif "resume" in category_lower:

        name = re.search(r"(name)[:\s]*([a-z ]+)", text_lower)
        email = re.search(r"([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,})", text_lower)
        phone = re.search(r"(\+?\d[\d\-\(\) ]{7,}\d)", text_lower)
        skills = re.search(r"(skills)[:\s]*(.+)", text_lower)

        data["name"] = name.group(2).strip() if name else None
        data["email"] = email.group(1) if email else None
        data["phone"] = phone.group(1) if phone else None
        data["skills"] = skills.group(2).strip() if skills else None

    return data
