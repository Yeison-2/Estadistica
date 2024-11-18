import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

ruta_archivo = r'C:\Users\yeiso\OneDrive\Escritorio\estadistica\Nueva carpeta\basededatos.csv'
df = pd.read_csv(ruta_archivo)

# Select the variables 'App Usage Time (min/day)' and 'User Behavior Class'
uso_app = df['App Usage Time (min/day)']
comportamiento_usuario = df['User Behavior Class']


# Calculate mean, median, mode for 'App Usage Time (min/day)'
media_app = uso_app.mean()
mediana_app = uso_app.median()
moda_app = uso_app.mode()[0]

# Calculate mean, median, mode for 'User Behavior Class'
media_comportamiento = comportamiento_usuario.mean()
mediana_comportamiento = comportamiento_usuario.median()
moda_comportamiento = comportamiento_usuario.mode()[0]

# Calculate variance, standard deviation, coefficient of variation, skewness, kurtosis for 'App Usage Time (min/day)'
varianza_app = uso_app.var()
desviacion_estandar_app = uso_app.std()
coef_variacion_app = desviacion_estandar_app / media_app
asimetria_app = skew(uso_app)
curtosis_app = kurtosis(uso_app)

#calcular el histograma de la variable 'App Usage Time (min/day)'
plt.figure(figsize=(10, 6))
plt.hist(uso_app, bins=20, color='blue', edgecolor='black')
plt.title('Histograma de Tiempo de Uso de la App (min/día)')
plt.xlabel('Tiempo de Uso de la App (min/día)')
plt.ylabel('Frecuencia')
plt.savefig('histograma.png')
plt.close()

#grafico pastel para la variable 'App Usage Time (min/day)'
plt.figure(figsize=(10, 6))
plt.pie([df[df['App Usage Time (min/day)'] < 60].shape[0], df[df['App Usage Time (min/day)'] >= 60].shape[0]], labels=['Menos de 60 min/día', '60 o más min/día'], autopct='%1.1f%%', colors=['blue', 'red'])
plt.title('Proporción de Tiempo de Uso de la App')
plt.savefig('grafico_pastel.png')
plt.close()


#calcular el histograma de la variable 'User Behavior Class'
plt.figure(figsize=(10, 6))
plt.hist(comportamiento_usuario, bins=5, color='blue', edgecolor='black')
plt.title('Histograma de Comportamiento del Usuario')
plt.xlabel('Comportamiento del Usuario')
plt.ylabel('Frecuencia')
plt.savefig('histograma_comportamiento.png')
plt.close()

# grafico pastel para la variable 'User Behavior Class'
plt.figure(figsize=(10, 6))
plt.pie([df[df['User Behavior Class'] == 1].shape[0], df[df['User Behavior Class'] == 2].shape[0], df[df['User Behavior Class'] == 3].shape[0], df[df['User Behavior Class'] == 4].shape[0], df[df['User Behavior Class'] == 5].shape[0]], labels=['Excelente', 'Bueno', 'Regular', 'Malo', 'Muy Malo'], autopct='%1.1f%%', colors=['blue', 'red', 'green', 'purple', 'orange'])
plt.title('Proporción de Comportamiento del Usuario')
plt.savefig('grafico_pastel_comportamiento.png')
plt.close()



# Calculate variance, standard deviation, coefficient of variation, skewness, kurtosis for 'User Behavior Class'
varianza_comportamiento = comportamiento_usuario.var()
desviacion_estandar_comportamiento = comportamiento_usuario.std()
coef_variacion_comportamiento = desviacion_estandar_comportamiento / media_comportamiento
asimetria_comportamiento = skew(comportamiento_usuario)
curtosis_comportamiento = kurtosis(comportamiento_usuario)

# a) Find the linear regression equation for 'App Usage Time (min/day)' and 'User Behavior Class'
X = uso_app.values.reshape(-1, 1)
y = comportamiento_usuario.values
regresion_lineal = LinearRegression()
regresion_lineal.fit(X, y)
pendiente = regresion_lineal.coef_[0]
intercepto = regresion_lineal.intercept_

# b) Plot the scatter diagram with the regression line for 'App Usage Time (min/day)' and 'User Behavior Class'
plt.figure(figsize=(10, 6))
plt.scatter(uso_app, comportamiento_usuario, color="blue",label='Datos')
plt.plot(uso_app, regresion_lineal.predict(X), color='red', label='Línea de Regresión')
plt.title('Diagrama de Dispersión con Línea de Regresión')
plt.xlabel('Tiempo de Uso de la App (min/día)')
plt.ylabel('Comportamiento del Usuario')
plt.legend()
plt.savefig('diagrama_dispersion.png')
plt.close()

# c) Calculate the coefficient of determination for 'App Usage Time (min/day)' and 'User Behavior Class'
r_cuadrado = r2_score(y, regresion_lineal.predict(X))

# d) Calculate the Pearson correlation coefficient for 'App Usage Time (min/day)' and 'User Behavior Class'
coef_corr_pearson = pearsonr(uso_app, comportamiento_usuario)[0]

# e) Make three predictions for 'App Usage Time (min/day)' and 'User Behavior Class'
valores_x = [30, 60, 90]
predicciones = [pendiente * x + intercepto for x in valores_x]


# Generate Markdown report
reporte = f"""
yeison stiven romero
2024

# Analisis de el uso de aplicaciones moviles y el comportamiento del usuario

## Introduccion
Este informe presenta un análisis detallado del tiempo de uso de aplicaciones y la clase de comportamiento del usuario en un grupo de 700 personas. El objetivo principal es comprender los patrones de uso de aplicaciones y el comportamiento del usuario, y extraer conclusiones significativas basadas en los datos proporcionados.

## Objetivos
1. Analizar la distribución del tiempo de uso de aplicaciones entre los participantes.
2. Identificar las medidas estadísticas clave como la media, mediana, moda, varianza, y desviación estándar para el tiempo de uso de aplicaciones y la clase de comportamiento del usuario.
3. Evaluar la asimetría y curtosis de la distribución de datos
4. Generar visualizaciones que representen claramente los patrones de uso de aplicaciones y el comportamiento del usuario.
5. Proporcionar conclusiones basadas en el análisis de los datos.

## Medidas Estadisticas de Tiempo de Uso de la App (min/dia)
- **Descripcion**: Esta variable representa el tiempo diario que los usuarios pasan utilizando una aplicación móvil.
- **Media**: {media_app} en promedio, los usuarios pasan aproximadamente 271.13 minutos al día utilizando aplicaciones móviles.
- **Mediana**: {mediana_app} La mitad de los usuarios pasan 227.5 minutos o menos al día utilizando aplicaciones móviles, y la otra mitad pasa más tiempo.
- **Moda**: {moda_app} El tiempo de uso más común entre los usuarios es de 64 minutos al día.
- **Varianza**: {varianza_app} Hay una alta variabilidad en el tiempo de uso de aplicaciones móviles entre los usuarios.
- **Desviacion Estandar**: {desviacion_estandar_app} En promedio, el tiempo de uso de aplicaciones móviles varía en 177.20 minutos respecto a la media.
- **Coeficiente de Variacion**: {coef_variacion_app} La desviación estándar es el 65% de la media, lo que muestra una alta variabilidad relativa en el tiempo de uso.
- **Asimetria**: {asimetria_app} La distribución de los datos tiene una ligera asimetría positiva, indicando que hay más usuarios con tiempos de uso por encima de la media.
- **Curtosis**: {curtosis_app} La distribución es más plana que una distribución normal (leptocúrtica), indicando menos valores extremos.

## Analisis de Distribucion
### Histograma de Tiempo de Uso de la App (min/dia)
![Histograma de Tiempo de Uso de la App](histograma.png)

### Grafico de torta de Tiempo de Uso de la App
![Grafico de torta de Tiempo de Uso de la App](grafico_pastel.png)


## Medidas Estadisticas de Comportamiento del Usuario
- **Descripcion**: Esta variable representa el comportamiento general de los usuarios al utilizar aplicaciones móviles de 1 a 5 (1: Excelente, 2: Bueno, 3: Regular, 4: Malo, 5: Muy Malo). 
- **Media**: {media_comportamiento} el comportamiento del usuario es aproximadamente 3, lo que indica un comportamiento "Regular".
- **Mediana**: {mediana_comportamiento} La mitad de los usuarios tienen un comportamiento igual o mejor que "Regular" y la otra mitad igual o peor.
- **Moda**: {moda_comportamiento} El comportamiento más común entre los usuarios es "Bueno".
- **Varianza**: {varianza_comportamiento} Hay una variabilidad moderada en el comportamiento del usuario.
- **Desviacion Estandar**: {desviacion_estandar_comportamiento} En promedio, el comportamiento del usuario varía en 1.40 unidades respecto a la media.
- **Coeficiente de Variacion**: {coef_variacion_comportamiento} La desviación estándar es el 47% de la media, lo que muestra una variabilidad relativa moderada.
- **Asimetria**: {asimetria_comportamiento} La distribución de los datos es casi simétrica.
- **Curtosis**: {curtosis_comportamiento} La distribución es más plana que una distribución normal (leptocúrtica), indicando menos valores extremos.

## Analisis de Distribucion
### Histograma de Comportamiento del Usuario
![Histograma de Comportamiento del Usuario](histograma_comportamiento.png)

### Grafico de torta de Comportamiento del Usuario
![Grafico de torta de Comportamiento del Usuario](grafico_pastel_comportamiento.png)


## Analisis de Regresion Lineal

### Ecuacion de Regresion Lineal
La ecuación de regresión lineal entre el uso de datos y el comportamiento del usuario es:
Comportamiento = {pendiente:.2f} * Uso de Datos + {intercepto:.2f}


### Diagrama de Dispersión
![Diagrama de Dispersión](diagrama_dispersion.png)

### Coeficiente de Determinacion
El coeficiente de determinación (R²) es: {r_cuadrado:.2f}

### Coeficiente de Correlacion de Pearson
El coeficiente de correlación de Pearson es: {coef_corr_pearson:.2f}

### Predicciones
Usando la ecuación de regresión lineal, las predicciones para el comportamiento del usuario son:
- Para un uso de las aplicaciones  de 30 min/día: {predicciones[0]:.2f}
- Para un uso de las aplicaciones  de 60 min/día: {predicciones[1]:.2f}
- Para un uso de las aplicaciones  de 90 min/día: {predicciones[2]:.2f}



## Conclusiones
- Se observa una relación {'positiva' if pendiente > 0 else 'negativa' if pendiente < 0 else 'sin relación'} entre el uso de datos y el comportamiento del usuario.
- El coeficiente de determinación indica que el modelo de regresión lineal explica el {r_cuadrado:.2f}% de la variabilidad en el comportamiento del usuario.
- El coeficiente de correlación de Pearson indica una {'correlación positiva' if coef_corr_pearson > 0 else 'correlación negativa' if coef_corr_pearson < 0 else 'ausencia de correlación'} entre el uso de datos y el comportamiento del usuario.
- Se concluyo que el tiempo de uso de aplicaciones y el comportamiento del usuario están relacionados.
- La relacion entre las variables es positiva, lo que significa que a medida que aumenta el tiempo de uso de la aplicación, el comportamiento del usuario tiende a empeorar.

## Anexos
- Fuente de los datos: [Kaggle](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)
- Fecha de la base de datos: 18 de octubre del 2024
- Población: 700 personas
- Columnas: 11
- Hombres: {df[df['Gender'] == 'Male'].shape[0]}
- Mujeres: {df[df['Gender'] == 'Female'].shape[0]}
- Edad menor: {df['Age'].min()} años
- Edad mayor: {df['Age'].max()} años
- Sistema Operativo iOS: {df[df['Operating System'] == 'iOS'].shape[0]}
- Sistema Operativo Android: {df[df['Operating System'] == 'Android'].shape[0]}
- El informe esta alojado en: [GitHub](https://github.com/Yeison-2/Estadistica)
"""



with open('reporte.md', 'w', encoding='utf-8') as f:
    f.write(reporte)