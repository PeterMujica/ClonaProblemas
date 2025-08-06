import streamlit as st
from generador import generar_problemas_pdf
from PIL import Image
import pytesseract

st.set_page_config(page_title="ClonaProblemas", layout="centered")
st.title("📄 ClonaProblemas: Generador de ejercicios matemáticos")

uploaded_file = st.file_uploader("Sube una imagen con un problema matemático", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)

    texto_detectado = pytesseract.image_to_string(image, lang="spa")
    st.subheader("🔍 Texto detectado:")
    st.code(texto_detectado)

    if st.button("Generar PDF con problemas similares"):
        output_path = generar_problemas_pdf(texto_detectado)
        with open(output_path, "rb") as file:
            st.download_button("📥 Descargar PDF", data=file, file_name="Problemas_Similares.pdf", mime="application/pdf")
