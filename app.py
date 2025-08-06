import streamlit as st
from PIL import Image
import pytesseract
from generador import generar_problemas_pdf
import os

st.title("ClonaProblemas: Generador de ejercicios matemáticos")
st.write("Sube una imagen con un problema matemático")

uploaded_file = st.file_uploader("Elige una imagen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    texto_detectado = pytesseract.image_to_string(image, lang="spa")
    st.write("📄 Texto detectado:")
    st.code(texto_detectado)

    if st.button("Generar PDF con ejercicios similares"):
        output_path = generar_problemas_pdf(texto_detectado)
        with open(output_path, "rb") as file:
            btn = st.download_button(
                label="📥 Descargar ejercicios en PDF",
                data=file,
                file_name="ejercicios_generados.pdf",
                mime="application/pdf"
            )
        os.remove(output_path)
