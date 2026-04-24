import os as fsos

filename="C:\Users\Johnny\Desktop\TRABALHO\ATEC\AULAS\CET\PYTHON"


with open(filename, "r", encoding="utf-8") as manipfile:
       texto=manipfile.read()

print("no file ", texto)

texto=input("intrud uma frase")

with open(filename,"w", encoding="utf-8") as manipfile:
    manipfile.write(texto)