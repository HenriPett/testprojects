import pandas as pd
import camelot
import os
import pikepdf

x = os.path.normpath('C:/Users/henri/OneDrive/Área de Trabalho/NotaNegociacao_2111104_20210121.pdf')

with pikepdf.open(x) as pdf:
    pdf.save('output.pdf')


y = camelot.read_pdf('output.pdf')

read = pd.DataFrame(y[0].df)

read.head

os.remove("output.pdf")
print(read.head)