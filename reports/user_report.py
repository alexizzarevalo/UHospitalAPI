from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Spacer
from reportlab.platypus import TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

fileName = "report.pdf"

def users_data(users):
    data = [["Nombre de usuario", "Correo electronico"]]
    for lst in map(lambda user: [user["username"], user["email"]], users):
        data.append(lst)

    return data

users = [
    {"username": "alexizzarevalo", "email": "alexizzarevalo.study@gmail.com"},
    {"username": "alisonleiva", "email": "alisonleiva24@gmail.com"},
    {"username": "darwinarevalo", "email": "dalexis.da@gmail.com"},
]

pdf = SimpleDocTemplate(fileName, pagesize=letter)

# Title
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
paragraph = Paragraph("Usuarios registrados", styles['Title'])


# Table
style = TableStyle([
    ('BACKGROUND', (0,0), (1,0), colors.green),
    ('TEXTCOLOR', (0,0), (1,0), colors.white),
])

data = users_data(users)
# data = [
#     ["alexizzarevalo", "alexizzarevalo.study@gmail.com"],
#     ["alisonleiva", "alisonleiva24@gmail.com"],
#     ["darwinarevalo", "dalexis.da@gmail.com"],
# ]

table = Table(data, style=style)

elements = [
    paragraph,
    Spacer(10,10),
    table
]

pdf.build(elements)
