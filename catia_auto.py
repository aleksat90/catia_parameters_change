# import python modules
import os
from win32com.client import Dispatch
import re

# Connecting to windows COM
CATIA = Dispatch('CATIA.Application')
# optional CATIA visibility
CATIA.Visible = True

# Check if Catia active document is Part
print(CATIA.activedocument.Name, 7)



paraneter_instance = CATIA.activedocument.part.Parameters.rootparameterset.allparameters.Count

parameter_value = []
param_names = []

#Rutina za iscitavanje paraneter_instance
for i in range(1,paraneter_instance+1):
    param_names.append(CATIA.activedocument.part.Parameters.rootparameterset.allparameters.Item(i).Name)
    parameter_value.append(CATIA.activedocument.part.Parameters.rootparameterset.allparameters.Item(i).Value)


#Setting the parameter value to 0 in this case
CATIA.activedocument.part.Parameters.rootparameterset.allparameters.Item(1).Value = 0

#CATIA UPDATE
try:
    CATIA.ActiveDocument.Product.Update()
except Exception as e:
    print("Didn't succed")


print("End")
