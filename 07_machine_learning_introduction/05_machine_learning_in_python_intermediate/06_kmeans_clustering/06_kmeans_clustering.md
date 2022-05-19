# K-means clustering
## 1. Clustering NBA Players.

En la cobertura de los medios de la NBA, los reporteros deportivos generalmente se enfocan en unos pocos jugadores y crean historias sobre la singularidad de las estadísticas de estos jugadores. Como científicos de datos, es probable que seamos escépticos acerca de cuán único es realmente cada jugador. Usaremos la ciencia de datos para explorar esta idea al observar un conjunto de datos de información de jugadores de la temporada 2013-2014.

Estas son las columnas con las que trabajaremos:


- `player` — el nombre del jugador
- `pos` — la posición del jugador
- `g` — el número de juegos jugados
- `pts` — el total de puntos anotados por el jugador
- `fg.` — el porcentaje de tiros de campo
- `ft.` — el porcentaje de tiros libres


Consulte el glosario en <a href="https://www.basketball-reference.com/leagues/NBA_2014_advanced.html" target="_blank">Basketball Reference</a> para obtener una explicación de cada columna.

## 2. Bases.

Los bases juegan uno de los roles más cruciales en un equipo porque su principal responsabilidad es crear oportunidades de anotar. Esta lección se centrará en una técnica de aprendizaje automático llamada agrupación (clustering), que nos permite visualizar los tipos de bases y agrupar bases similares. El uso de dos funciones nos permite visualizar fácilmente a los jugadores y también simplificará la agrupación. Para los bases, la relación entre asistencia y rotación es un buen indicador del rendimiento porque cuantifica la cantidad de oportunidades de gol que creó ese jugador. Usemos también los puntos por partido, ya que los armadores efectivos no solo crean oportunidades de gol, sino que también anotan muchos de esos puntos ellos mismos.

### Ejercicio


- Cree un marco de datos nuevo que contenga solo los bases del conjunto de datos. 
- Los bases aparecen como `PG` en la columna `pos`. 
- Asigne el marco de datos filtrado a `point_guards`.


## 3. Puntos por juego.

Si bien nuestro conjunto de datos no incluye valores de _puntos por juego_, podemos calcularlos fácilmente utilizando los puntos totales de cada jugador (`pts`) y la cantidad de juegos (`g`) jugaron. Usando pandas, podemos multiplicar y dividir columnas para crear la columna _Puntos por juego_ `ppg` dividiendo `pts` y `g</code > columnas.


## 4. Tasa de rotación de asistencia.

Ahora vamos a crear una columna, `atr`, para el índice de rotación de asistencias, que calculamos dividiendo las asistencias totales (`ast`) por las pérdidas de balón totales (`tov` ):

$\text{ATR} \frac{\text{Assists}}{\text{Turnovers}}$

### Ejercicio


- Elimina a los jugadores que tienen 0 pérdidas de balón. 
- Estos jugadores no solo jugaron algunos juegos, lo que dificulta entender sus verdaderas habilidades, sino que tampoco podemos dividir entre 0 cuando calculamos `atr`. 


- Utilice la misma técnica de división que usamos con _Puntos por partido_ para crear la columna _Ratio de rotación de asistencias_ (`atr`) para `point_guards </código>.


## 5. Visualizando a los Bases.
Use `matplotlib` para crear un diagrama de dispersión con _Puntos por juego_ (`ppg`) en el _eje X_ y _ Tasa de rotación asistida_ (`atr`) en el _eje Y_.

## 6. Agrupación de jugadores.

Parece haber cinco áreas generales, o grupos, de bases (con algunas excepciones). Podemos usar una técnica llamada agrupación para segmentar a todos los bases en grupos de jugadores similares. Si bien la regresión y otras técnicas de _aprendizaje automático supervisado_ funcionan bien cuando tenemos una métrica clara que queremos optimizar y una gran cantidad de datos etiquetados previamente, debemos utilizar en su lugar _aprendizaje automático no supervisado_ técnicas para explorar la estructura dentro de un conjunto de datos que no tiene un valor claro para optimizar.

Hay varias formas de agrupar datos, pero en esta lección nos centraremos en la agrupación basada en el centroide. El agrupamiento basado en centroides funciona bien cuando los grupos se asemejan a círculos con centros (o centroides). El centroide representa la media aritmética de todos los puntos de datos en ese grupo.

Usaremos K-means Clustering, un popular algoritmo de agrupamiento basado en el centroide. La K en K-medias se refiere a la cantidad de grupos en los que queremos segmentar nuestros datos. El paso clave con K-means (y la mayoría de las técnicas de aprendizaje automático no supervisadas) es que tenemos que especificar qué es `k`. Esto tiene ventajas y desventajas, pero una ventaja es que podemos elegir el `k` que tenga más sentido para nuestro caso de uso. Estableceremos `k` en cinco, ya que queremos que K-means segmente nuestros datos en cinco grupos.


## 7. El Algoritmo.

Setup K-means es un algoritmo iterativo que cambia entre recalcular el centroide de cada grupo y los jugadores que pertenecen a ese grupo. Para comenzar, seleccione cinco jugadores al azar y asigne sus coordenadas como los centroides iniciales de los grupos recién creados.

**Paso 1 (Asignar puntos a grupos):** Para cada jugador, calcule la distancia euclidiana entre las coordenadas de ese jugador o los valores para `atr` &amp; `ppg`, y cada una de las coordenadas de los centroides. Asigne al jugador al grupo cuyo centroide sea el más cercano o tenga la distancia euclidiana más baja de los valores del jugador.

**Paso 2 (Actualizar nuevos centroides de los grupos):** Para cada grupo, calcule el nuevo centroide calculando la media aritmética de todos los puntos (jugadores) en ese grupo. Calculamos la media aritmética tomando el promedio de todos los valores X (`atr`) y el promedio de todos los valores Y (`ppg`) de los puntos en ese grupo .

**Iterar:** repetir los pasos 1 y 2 hasta que los clústeres ya no se muevan y hayan convergido. 


## 8. Visualice Centroides.

Tracemos los `centroides`, además de los `point_guards`, para que podamos ver dónde comenzaron los centroides elegidos al azar.

## 9. Configuración (continuación).

Si bien el objeto de marco de datos `centroids` funcionó bien para los centroides iniciales, donde los centroides eran solo un subconjunto de jugadores, a medida que iteramos, los valores de los centroides serán coordenadas que pueden no coincidir con las coordenadas de otro jugador. Usemos un objeto de diccionario en su lugar para representar los centroides.

Necesitaremos un identificador único, como `cluster_id`, para hacer referencia al centroide de cada clúster y una representación de lista de las coordenadas del centroide (o valores para `ppg` y `atr</ código>). Vamos a crear un diccionario con el siguiente mapeo:

Para generar los `cluster_id`, iteremos a través de cada centroide y asignemos un número entero de 0 a `k-1`. Por ejemplo, el primer centroide tendrá un `cluster_id` de 0, mientras que el segundo tendrá un `cluster_id` de 1. Escribiremos una función, `centroids_to_dict`, que toma el objeto de marco de datos `centroids`, crea un `cluster_id`, convierte `ppg` y `atr` valores para ese centroide en una lista de coordenadas y agrega tanto el `cluster_id` como la `coordinates_list` al diccionario que se devuelve.


## 10. Paso 1 (Distancia Euclidiana).

Antes de que podamos asignar jugadores a grupos, necesitamos una forma de comparar los valores `ppg` y `atr` de los jugadores con los centroides de cada grupo. La distancia euclidiana es la técnica más común utilizada en la ciencia de datos para medir la distancia entre vectores y funciona muy bien en dos y tres dimensiones. En dimensiones de mayor valor, la distancia euclidiana puede ser engañosa. En dos dimensiones, la distancia euclidiana es esencialmente el teorema de Pitágoras.

Aquí está la fórmula: $\sqrt{(q_1-p_1)^2 + (q_2-p_2)^2 + \cdots + (q_n-p_n)^2}$



`q` y `p` son los dos vectores que estamos comparando. Si `q` es [5, 2] y `p` es [3, 1], la distancia resulta ser la siguiente:

$\sqrt{(5-3)^2 + (2-1)^2} = \sqrt{5} = ~2.23607$

Vamos a crear la función `calculate_distance`, que toma dos listas (los valores del jugador para `ppg` y `atr` y los valores del centroide para `ppg< /código> y <código>atr</código>).


## 11. Paso 1 (Continuación).

Ahora necesitamos una forma de asignar puntos de datos a los clústeres en función de la distancia euclidiana. En lugar de crear una nueva variable o estructura de datos para albergar los clústeres, simplifiquemos las cosas y simplemente agreguemos una columna a los `point_guards` marco de datos que contiene el `cluster_id` del clúster al que pertenece. 

_Nota: aunque no sembramos los números aleatorios para generar los centroides, la respuesta se sembrará y producirá los mismos resultados cada vez._ 

### Ejercicio


- 
<p>Cree una función que pueda aplicarse a cada fila en el conjunto de datos (usando la función `apply` en `pandas`). </p>

- Para cada jugador, queremos calcular las distancias al centroide de cada grupo usando la función `calculate_distance`. 
- Una vez que conocemos las distancias, podemos determinar qué centroide es el más cercano (tiene la distancia más baja) y devolver el `cluster_id` de ese centroide. 


- 
<p>Cree una nueva columna, `cluster`, que contenga los resultados por filas de `assign_to_cluster`.</p>



## 12. Visualización de clústeres.

Escribamos una función, `visualize_clusters`, para visualizar los clústeres fácilmente.

## 13. Paso 2.
¡Qué colorido! Ahora codifiquemos el Paso 2, donde recalculamos los centroides para cada grupo.

### Ejercicio


- Termine la función `recalculate_centroids` para que haga lo siguiente:
- Toma `point_guards` 
- Utiliza cada `cluster_id`(desde `0` hasta `num_clusters - 1`) para extraer todos los jugadores de cada grupo
- Calcula la nueva media aritmética
- Agrega el `cluster_id` y la nueva media aritmética a `new_centroids_dict`, el diccionario final que queremos devolver




## 14. Repita el paso 1.

Ahora que volvimos a calcular los centroides, volvamos a ejecutar el Paso 1 (`assign_to_cluster`) y veamos cómo cambiaron los clústeres.



## 15. Repita los pasos 2 y 1.
Now we need to recalculate the centroids and shift the clusters again.


## 16. Desafíos de K-medias.

A medida que repite los pasos 1 y 2 y ejecuta `visualize_clusters`, notará que algunos de los puntos cambian de clúster entre cada iteración (especialmente en áreas donde dos clústeres casi se superponen), pero por lo demás, parece que los clústeres no se mueven. mucho después de cada iteración. Esto significa dos cosas:

- K-means no provoca cambios significativos en la composición de los clústeres entre iteraciones, lo que significa que siempre convergerá y se estabilizará.
- Debido a que K-means es conservador entre iteraciones, es muy importante dónde seleccionamos los centroides iniciales y cómo asignamos los jugadores a los grupos.

Para contrarrestar estos problemas, la implementación de `sklearn` de K-means hace algunas cosas inteligentes como volver a ejecutar todo el proceso de agrupamiento muchas veces con centroides iniciales aleatorios para que los resultados finales estén un poco menos sesgados en los centroides iniciales de un paso.


## 17. Conclusión.

En esta lección, exploramos cómo segmentar a los jugadores de la NBA en grupos con rasgos similares. Nuestra exploración nos ayudó a comprender los cinco tipos de bases en función de la tasa de rotación de asistencias y los puntos por juego de cada jugador. En lecciones futuras, exploraremos cómo agrupar usando muchas más funciones, así como formas alternativas de agrupar datos sin usar centroides.

También trabajamos con `sklearn` y exploramos la simplicidad de usar modelos sofisticados para lograr lo que necesitamos rápidamente. En solo unas pocas líneas, ejecutamos y visualizamos los resultados de una sólida implementación de agrupamiento de K-means. Cuando use K-means en el mundo real, use la implementación `sklearn`.

