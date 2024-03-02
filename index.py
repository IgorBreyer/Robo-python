import pandas as pd
import time

try:
    df = pd.read_excel(r'C:\Users\igor.mori\Documents\Projetos\Robo python\dist\entrada.xlsx')
    df = df.dropna(how="all")
    
    escrever = pd.ExcelWriter(r'C:\Users\igor.mori\Documents\Projetos\Robo python\saida.xlsx')
    df.to_excel(escrever, index=False)
    
    escrever.close()
    
    time.sleep(10)

except Exception as e:
    print(e)
    time.sleep(10)