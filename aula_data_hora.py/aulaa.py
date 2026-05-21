"""from datetime import datetime

torre_gemeas = datetime(2001, 7, 11, 13, 22, 1)
print(torre_gemeas.minute)"""

from datetime import datetime
from zoneinfo import ZoneInfo

# Pega o horário atual no fuso horário de Brasília
horario_br = datetime.now(ZoneInfo("America/Sao_Paulo"))

print(horario_br) 
# Saída: 2026-05-19 13:31:00-03:00 (dependendo do seu horário local)
