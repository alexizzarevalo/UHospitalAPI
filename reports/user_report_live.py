from reportlab.platypus import SimpleDocTemplate, Table, Spacer, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_user_report(name, users):
    pdf = SimpleDocTemplate(name, pagesize=letter)

    my_space = Spacer(10,20)

    my_style = ParagraphStyle(name='Title',
                            fontSize=30,
                            alignment=TA_CENTER,
                            spaceAfter=6)

    paragraph = Paragraph("Usuarios registrados", style=my_style)

    data = []
    cont = 0
    for user in users:
        if cont == 0:
            data.append(["Nombre de usuario", "Correo electronico"])
            cont += 1
            continue
        data.append([user["username"], user["email"]])

    table_style = TableStyle([
        ('BACKGROUND', (0,0), (1,0), colors.green),
        ('TEXTCOLOR', (0,0), (1,0), colors.white),
    ])

    table = Table(data, style=table_style)

    pdf.build([paragraph,my_space, table])
    return None