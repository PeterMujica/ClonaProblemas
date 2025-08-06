import streamlit as st
import pytesseract
from PIL import Image
from generador import generar_problemas_pdf

st.title("ClonaProblemas: Generador de ejercicios matemáticos")
st.write("Sube una imagen con un problema matemático")

imagen = st.file_uploader("Selecciona una imagen", type=["png", "jpg", "jpeg"])

if imagen:
    image = Image.open(imagen)
    st.image(image, caption='Imagen cargada', use_column_width=True)

    # OCR
    texto_detectado = pytesseract.image_to_string(image, lang="spa")
    st.subheader("Texto detectado:")
    st.text(texto_detectado)

    # Generar PDF
    if st.button("Generar PDF con problemas similares"):
        output_path = generar_problemas_pdf(texto_detectado)
        with open(output_path, "rb") as file:
            st.download_button(label="Descargar PDF", data=file, file_name="problemas_generados.pdf", mime="application/pdf")
