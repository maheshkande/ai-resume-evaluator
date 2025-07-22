import fitz  # PyMuPDF

def extract_text_from_resume(uploaded_file):
    try:
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.read())

        doc = fitz.open("temp_resume.pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    except Exception as e:
        return f"❌ Error: {e}"
