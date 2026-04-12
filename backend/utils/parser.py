import PyPDF2
import docx
from io import BytesIO

async def extract_text(file):
    content = await file.read()

    if file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(BytesIO(content))
        text = ""

        for page in reader.pages:
            text += page.extract_text() + " "

        return text.lower()

    elif file.filename.endswith(".docx"):
        doc = docx.Document(BytesIO(content))
        text = "\n".join([p.text for p in doc.paragraphs])
        return text.lower()

    return ""