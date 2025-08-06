from fpdf import FPDF
import random
import os

def generar_problema(num):
    elementos = [
        ("el polonio", 138),
        ("el uranio", 703800000),
        ("el torio", 14050000000),
        ("el carbono-14", 5730),
        ("el plutonio", 24100),
        ("el tritio", 12.3),
        ("el cesio-137", 30.17),
        ("el estroncio-90", 28.8),
        ("el kriptón-85", 10.76),
        ("el yodo-131", 8.02),
        ("el americio-241", 432.2),
        ("el neptunio-237", 2140000)
    ]
    elemento, vida_media = random.choice(elementos)
    masa_inicial = random.choice([100, 200, 300, 400, 500])
    masa_final = random.randint(10, int(masa_inicial * 0.9 - 1))
    return (f"{num}. {elemento.capitalize()}, un elemento radiactivo,\n"
            f"   se desintegra exponencialmente. Su vida media\n"
            f"   es de {vida_media} años. ¿Cuánto tardarán\n"
            f"   {masa_inicial} g en reducirse a {masa_final} g?")

def generar_problemas_pdf(texto_detectado):
    problemas = [generar_problema(i + 1) for i in range(12)]

    class PDF(FPDF):
        def header(self):
            self.set_font("Helvetica", size=9)
            self.set_y(20)
            self.cell(0, 5, "Escuela: ______________  Alumno: ______________", ln=1)
            self.cell(0, 5, "Grado: ________________  Sección: _____________", ln=1)
            self.cell(0, 5, "Fecha: ________________", ln=1)

    pdf = PDF()
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.set_font("Helvetica", size=9)

    ancho_caja, alto_caja = 85, 35
    esp_h, esp_v = 10, 10
    inicio_x, inicio_y = 20, 50

    for i, problema in enumerate(problemas):
        if i == 6:
            pdf.add_page()
        col = i % 2
        row = i % 6
        x = inicio_x + col * (ancho_caja + esp_h)
        y = inicio_y + row * (alto_caja + esp_v)
        pdf.set_xy(x, y)
        pdf.multi_cell(ancho_caja, 4.5, problema, border=1)

    os.makedirs("output", exist_ok=True)
    output = "output/Problemas_Similares.pdf"
    pdf.output(output)
    return output
