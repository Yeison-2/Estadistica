# Presentación de la Actividad Final de Estadística

## Introducción
Este proyecto presenta un análisis detallado del uso de aplicaciones móviles y el comportamiento del usuario en un grupo de 700 personas. El objetivo principal es comprender los patrones de uso de aplicaciones y el comportamiento del usuario, y extraer conclusiones significativas basadas en los datos proporcionados.

## Objetivos
1. Analizar la distribución del tiempo de uso de aplicaciones entre los participantes.
2. Identificar las medidas estadísticas clave como la media, mediana, moda, varianza, y desviación estándar para el tiempo de uso de aplicaciones y el comportamiento del usuario.
3. Evaluar la asimetría y curtosis de la distribución de datos.
4. Generar visualizaciones que representen claramente los patrones de uso de aplicaciones y el comportamiento del usuario.
5. Proporcionar conclusiones basadas en el análisis de los datos.

## Metodología
- **Recolección de Datos**: Se utilizó un conjunto de datos de Kaggle que incluye información sobre el uso de aplicaciones móviles y el comportamiento del usuario.
- **Análisis Estadístico**: Se calcularon medidas estadísticas clave y se realizó un análisis de regresión lineal para entender la relación entre el uso de aplicaciones y el comportamiento del usuario.
- **Visualización de Datos**: Se generaron gráficos y diagramas para representar los patrones de uso de aplicaciones y el comportamiento del usuario.

## Resultados
### Medidas Estadísticas de Tiempo de Uso de la App (min/día)
- **Media**: 271.13
- **Mediana**: 227.5
- **Moda**: 64
- **Varianza**: 31399.66
- **Desviación Estándar**: 177.20
- **Coeficiente de Variación**: 0.65
- **Asimetría**: 0.37
- **Curtosis**: -1.26

### Medidas Estadísticas de Comportamiento del Usuario
- **Media**: 2.99
- **Mediana**: 3.0
- **Moda**: 2
- **Varianza**: 1.96
- **Desviación Estándar**: 1.40
- **Coeficiente de Variación**: 0.47
- **Asimetría**: 0.02
- **Curtosis**: -1.28

### Análisis de Regresión Lineal
- **Ecuación de Regresión Lineal**: Comportamiento = 0.01 * Uso de Datos + 0.91
- **Coeficiente de Determinación (R²)**: 0.94
- **Coeficiente de Correlación de Pearson**: 0.97

## Conclusiones
- Existe una relación positiva entre el uso de datos y el comportamiento del usuario.
- El modelo de regresión lineal explica el 94% de la variabilidad en el comportamiento del usuario.
- A medida que aumenta el tiempo de uso de la aplicación, el comportamiento del usuario tiende a empeorar.

## Anexos
- **Fuente de los Datos**: [Kaggle](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)
- **Fecha de la Base de Datos**: 18 de octubre del 2024
- **Población**: 700 personas
- **Columnas**: 11
- **Hombres**: 364
- **Mujeres**: 336
- **Edad menor**: 18 años
- **Edad mayor**: 59 años
- **Sistema Operativo iOS**: 146
- **Sistema Operativo Android**: 554
