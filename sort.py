import pandas as pd
# Lista de letras y sus porcentajes para la palabra encefalograma
letras = ['E', 'N', 'C', 'F', 'A', 'L', 'O', 'G', 'R', 'M']
porcentajes = [13.68, 6.71, 4.68, 0.69, 12.53, 4.97, 8.68, 1.01, 6.87, 3.15]

# Creo el dataframe
df = pd.DataFrame({'Letra': letras, 'Porcentaje': porcentajes})

# Ordeno de mayor a menor
df_sorted = df.sort_values(by='Porcentaje', ascending=False)

df_sorted[['Letra', 'Porcentaje']]
# Imprimo
print(df_sorted)
