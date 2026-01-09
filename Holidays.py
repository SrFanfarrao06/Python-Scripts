import holidays
from datetime import date

# Define os feriados para o Brasil
br_holidays = holidays.Brazil()

# Data atual
hoje = date.today()

# Verifica se hoje é feriado
if hoje in br_holidays:
    print(f"Hoje é feriado: {br_holidays[hoje]}")
else:
    print("Hoje não é feriado.")
