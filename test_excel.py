import numpy as np
import pandas as pd
# pathFileQ = filepath
pathFileQ = r'C:\Users\matheus.sampaio.RHAMA0\Desktop\CURSO_DJANGO\PROJETOS\DJANGO_BASICO\dados_mini.csv'
FileQ = open(pathFileQ,'r')         # Abre o arquivo
lines = FileQ.readlines() 

primeira = lines[0]
aux_mini = primeira.split(";")

#aux_mini.pop(0)
data = []
vazao = []
todos = []
for iline in range(1,len(lines)):
   
    data.append(lines[iline].split(";")[0])
    vazao.append(lines[iline].split(";")[1:])
    
    
import pandas as pd 
import io


df = pd.read_csv((pathFileQ), delimiter = ";")

a= []
# =============================================================================
# for i in aux_mini:
#     for j in (range(0, 5)):
#         print(df['data'][j] , df[i][j])
#     print(i)
# =============================================================================



from django.db import models

class mini_bacias(models.Model):
    nome = models.CharField('Mini Bacia', max_length=100)

    vazao = models.DecimalField('Vazão', decimal_places=2, max_digits=9)

    data = models.DateField('Data')
    def __str__(self):
        return self.nome

d = mini_bacias('1050', 25.35, 25/10/2020)
print(d)





