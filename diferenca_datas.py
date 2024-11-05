from datetime import datetime

# Definindo as datas como strings no formato dia/mês/ano
datafim_str = "15/10/2024"
datainicio_str = "15/10/2024"

# Calculando a diferença em dias
diferenca = (datetime.strptime(datainicio_str, "%d/%m/%Y") - datetime.strptime(datafim_str, "%d/%m/%Y")).days

# Imprimindo a mensagem formatada em português
print(f"Entre {datafim_str} e {datainicio_str}, se passaram {diferenca} dias.")