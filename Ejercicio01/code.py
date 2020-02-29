# Unicorn Investors
# Rolando Borja Brito

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime       #To access datetime
from pandas import Series           #To work on series
import warnings                     #To ignote the warnings
warnings.filterwarnings("ignore")


train = pd.read_csv("Train_SU63ISt.csv")
test  = pd.read_csv("Test_0qrQsBZ.csv")

# Realizo una copia de los datos de entrenamiento y prueba para que,
# si realizo cambios en este conjunto de datos, no pierda
# el conjunto de datos original

train_original = train.copy()
test_original  = test.copy()


