yeison stiven romero
2024

# Analisis de el uso de aplicaciones moviles y el comportamiento del usuario

## Introduccion

Este informe presenta un an�lisis detallado del tiempo de uso de aplicaciones y la clase de comportamiento del usuario en un grupo de 700 personas. El objetivo principal es comprender los patrones de uso de aplicaciones y el comportamiento del usuario, y extraer conclusiones significativas basadas en los datos proporcionados.

## Objetivos

1. Analizar la distribuci�n del tiempo de uso de aplicaciones entre los participantes.
2. Identificar las medidas estad�sticas clave como la media, mediana, moda, varianza, y desviaci�n est�ndar para el tiempo de uso de aplicaciones y la clase de comportamiento del usuario.
3. Evaluar la asimetr�a y curtosis de la distribuci�n de datos
4. Generar visualizaciones que representen claramente los patrones de uso de aplicaciones y el comportamiento del usuario.
5. Proporcionar conclusiones basadas en el an�lisis de los datos.

## Medidas Estadisticas de Tiempo de Uso de la App (min/dia)

- **Descripcion**: Esta variable representa el tiempo diario que los usuarios pasan utilizando una aplicaci�n m�vil.
- **Media**: 271.12857142857143
- **Mediana**: 227.5
- **Moda**: 64
- **Varianza**: 31399.6572654813
- **Desviacion Estandar**: 177.19948438266206
- **Coeficiente de Variacion**: 0.653562564243972
- **Asimetria**: 0.3715135303691814
- **Curtosis**: -1.2591977822617888

## Medidas Estadisticas de Comportamiento del Usuario

- **Descripcion**: Esta variable representa el comportamiento general de los usuarios al utilizar aplicaciones m�viles de 1 a 5 (1: Muy malo, 2: Malo, 3: Regular, 4: Bueno, 5: Excelente).
- **Media**: 2.99
- **Mediana**: 3.0
- **Moda**: 2
- **Varianza**: 1.9641344778254648
- **Desviacion Estandar**: 1.4014758213488612
- **Coeficiente de Variacion**: 0.46872101048456893
- **Asimetria**: 0.017781063982686602
- **Curtosis**: -1.277777445214311

## Analisis de Regresion Lineal

### Ecuacion de Regresion Lineal

La ecuaci�n de regresi�n lineal entre el uso de datos y el comportamiento del usuario es:
Comportamiento = 0.01 * Uso de Datos + 0.91

### Diagrama de Dispersi�n

![Diagrama de Dispersi�n](diagrama_dispersion.png)

### Coeficiente de Determinacion

El coeficiente de determinaci�n (R�) es: 0.94

### Coeficiente de Correlacion de Pearson

El coeficiente de correlaci�n de Pearson es: 0.97

### Predicciones

Usando la ecuaci�n de regresi�n lineal, las predicciones para el comportamiento del usuario son:

- Para un uso de datos de 30 min/d�a: 1.14
- Para un uso de datos de 60 min/d�a: 1.37
- Para un uso de datos de 90 min/d�a: 1.60

## Conclusiones

- Se observa una relaci�n positiva entre el uso de datos y el comportamiento del usuario.
- El coeficiente de determinaci�n indica que el modelo de regresi�n lineal explica el 0.94% de la variabilidad en el comportamiento del usuario.
- El coeficiente de correlaci�n de Pearson indica una correlaci�n positiva entre el uso de datos y el comportamiento del usuario.
- Se concluyo que el tiempo de uso de aplicaciones y el comportamiento del usuario est�n relacionados, y el an�lisis de regresi�n lineal proporciona informaci�n valiosa sobre esta relaci�n.
- Se entendio que el comportamiento como el de nivel 5 es el mejor y el de nivel 1 es el peor.

## Anexos

- Fuente de los datos: [Kaggle](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)
- Fecha de la base de datos: 18 de octubre del 2024
- Poblaci�n: 700 personas
- Columnas: 11
- Hombres: 364
- Mujeres: 336
- Edad menor: 18 a�os
- Edad mayor: 59 a�os
- Sistema Operativo iOS: 146
- Sistema Operativo Android: 554
- Depuraci�n de datos: S� porque no hay datos nulos en la base de datos.
