import streamlit as st
from PIL import Image
import pytesseract
from generador import generar_problemas_pdf
import os

st.title("ClonaProblemas: Generador de ejercicios matemáticos")
st.write("Sube una imagen con un problema matemático")

uploaded_file = st.file_uploader("Sube tu imagen", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida', use_column_width=True)
    
    texto_detectado = pytesseract.image_to_string(image, lang="spa")
    st.subheader("Texto detectado:")
    st.code(texto_detectado)
    
    if texto_detectado.strip() != "":
        output_path = generar_problemas_pdf(texto_detectado)
        st.success("PDF generado correctamente")
        with open(output_path, "rb") as file:
            btn = st.download_button(
                label="📄 Descargar PDF",
                data=file,
                file_name="ejercicios_generados.pdf",
                mime="application/pdf"
            )
