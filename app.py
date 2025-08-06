import streamlit as st
from PIL import Image
import requests
from generador import generar_problemas_pdf
import os

st.title("ClonaProblemas: Generador de ejercicios matemáticos")
st.write("Sube una imagen con un problema matemático")

uploaded_file = st.file_uploader("Sube tu imagen", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida', use_column_width=True)

    # Reemplazo de pytesseract por OCR.Space API (gratuita)
    api_key = "helloworld"
    url_api = "https://api.ocr.space/parse/image"
    response = requests.post(
        url_api,
        files={uploaded_file.name: uploaded_file.getvalue()},
        data={"apikey": api_key, "language": "spa"},
    )
    result = response.json()
    texto_detectado = result['ParsedResults'][0]['ParsedText'] if 'ParsedResults' in result else ''

    st.subheader("Texto detectado:")
    st.code(texto_detectado)

    if texto_detectado.strip() != "":
        output_path = generar_problemas_pdf(texto_detectado)
        st.success("PDF generado correctamente")
        with open(output_path, "rb") as file:
            st.download_button(
                label="📄 Descargar PDF",
                data=file,
                file_name="ejercicios_generados.pdf",
                mime="application/pdf"
            )
        os.remove(output_path)
