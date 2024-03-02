import pandas as pd
import time

try:
    df = pd.read_excel(r'Especificar o local do arquivo original aqui.')
    df = df.dropna(how="all")
    
    escrever = pd.ExcelWriter(r'Especificar o local de salvamento do novo arquivo aqui.')
    df.to_excel(escrever, index=False)
    
    escrever.close()
    
    time.sleep(10)

except Exception as e:
    print(e)
    time.sleep(10)