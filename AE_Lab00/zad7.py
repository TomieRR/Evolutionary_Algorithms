import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = [[11,13,12],[8,11,14]]

tabela = pd.DataFrame(dane)

tabela.to_csv('wyniki.csv',index=False,header=False)