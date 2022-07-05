# Indexación Booleana

## 1. Lectura de archivos CSV con NumPy

<div><p>NumPy facilita la selección de datos e incluye una serie de funciones que simplifican el cálculo de estadísticas en los diferentes ejes (o dimensiones). </p>
<p>Por ejemplo, digamos que queremos saber cuántos <a href="https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page" target="_blank ">viajes en taxi</a> que los pasajeros hicieron cada mes? ¿O qué aeropuerto es el más concurrido? Para ello, aprenderemos una nueva técnica: <strong>Indización booleana</strong>. Antes de comenzar con la indexación booleana, veamos nuestros datos. </p>
<p>Estas son las primeras cinco filas de nuestros datos con etiquetas de columna:</p>

<table class="dataframe">
<thead>
<tr>
<th>pickup_year</th>
<th>pickup_month</th>
<th>pickup_day</th>
<th>pickup_dayofweek</th>
<th>pickup_time</th>
<th>pickup_location_code</th>
<th>dropoff_location_code</th>
<th>trip_distance</th>
<th>trip_length</th>
<th>fare_amount</th>
<th>fees_amount</th>
<th>tolls_amount</th>
<th>tip_amount</th>
<th>total_amount</th>
<th>payment_type</th>
</tr>
</thead>
<tbody>
<tr>
<td>2016</td>
<td>1</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>21.00</td>
<td>2037</td>
<td>52.0</td>
<td>0.8</td>
<td>5.54</td>
<td>11.65</td>
<td>69.99</td>
<td>1</td>
</tr>
<tr>
<td>2016</td>
<td>1</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>16.29</td>
<td>1520</td>
<td>45.0</td>
<td>1.3</td>
<td>0.00</td>
<td>8.00</td>
<td>54.30</td>
<td>1</td>
</tr>
<tr>
<td>2016</td>
<td>1</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>6</td>
<td>12.70</td>
<td>1462</td>
<td>36.5</td>
<td>1.3</td>
<td>0.00</td>
<td>0.00</td>
<td>37.80</td>
<td>2</td>
</tr>
<tr>
<td>2016</td>
<td>1</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>6</td>
<td>8.70</td>
<td>1210</td>
<td>26.0</td>
<td>1.3</td>
<td>0.00</td>
<td>5.46</td>
<td>32.76</td>
<td>1</td>
</tr>
<tr>
<td>2016</td>
<td>1</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>6</td>
<td>5.56</td>
<td>759</td>
<td>17.5</td>
<td>1.3</td>
<td>0.00</td>
<td>0.00</td>
<td>18.80</td>
<td>2</td>
</tr>
</tbody>
</table>

<p>A continuación se muestra información sobre las columnas seleccionadas del conjunto de datos:</p>
<ul>
<li><code>pickup_year</code>: el año del viaje</li>
<li><code>pickup_month</code>: el mes del viaje (enero es <code>1</code>, diciembre es <code>12</code>)</li>
<li><code>pickup_day</code>: el día del mes del viaje</li>
<li><code>pickup_location_code</code>: el aeropuerto o <a href="https://en.wikipedia.org/wiki/Boroughs_of_New_York_City" target="_blank">distrito</a> donde comenzó el viaje </li>
<li><code>dropoff_location_code</code>: el aeropuerto o distrito donde finalizó el viaje</li>
<li><code>trip_distance</code>: la distancia del viaje en millas</li>
<li><code>trip_length</code>: la duración del viaje en segundos</li>
<li><code>fare_amount</code>: la tarifa base del viaje, en dólares</li>
<li><code>total_amount</code>: el monto total cobrado al pasajero, incluidas todas las tarifas, peajes y propinas</li>
</ul>
<p>Puede encontrar información sobre todas las columnas en el <a href="https://s3.amazonaws.com/dq-content/290/nyc_taxi_data_dictionary.md" target="_blank">diccionario de datos</a>. </p>
<p>Ahora, aprendamos a usar el <a href="https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html" target= Función "_blank"><code>numpy.genfromtxt()</code></a> para leer archivos en NumPy ndarrays. Esta es la sintaxis simplificada de la función y una explicación de los dos parámetros:</p>
</div>

```python
np.genfromtxt(filename, delimiter=None)
```

<div>
<ul>
<li><code>filename</code>: un argumento posicional, generalmente una cadena que representa la ruta al archivo de texto para leer</li>
<li><code>delimiter</code>: un argumento con nombre, que especifica la cadena utilizada para separar cada valor</li>
</ul>
<p>En este caso, debido a que tenemos un archivo CSV, el delimitador es una coma. Así es como lo leeríamos en un archivo llamado <code>data.csv</code>:</p>
</div>

```python
data = np.genfromtxt('data.csv', delimiter=',')
```

<div>
<p>Vamos a leer nuestro archivo <code>nyc_taxis.csv</code> en NumPy a continuación.</p></div>

### Ejercicio

<ol>
<li>Importe la biblioteca NumPy y asígnele el alias <code>np</code>.</li>
<li>Utilice la función <code>numpy.genfromtxt()</code> para leer el archivo <code>nyc_taxis.csv</code> en NumPy. Asigne el resultado a <code>taxi</code>.</li>
<li>Utilice el atributo <a href="https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape" target="_blank "><code>ndarray.shape</code> </a> para asignar la dimensión de <code>taxi</code> a <code>taxi_shape</code>.</li>
<li>Imprima las variables para ver el ndarray <code>taxi</code> y su dimensión después de ejecutar su código.</li>
</ol>

<h2>2. Lectura de archivos CSV con NumPy Continuación </h2>

## 2. Lectura de archivos CSV con NumPy Continuación

```python
# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)
```

## Matrices booleanas
## Indexación booleana con ndarrays 1D
## Indexación booleana con ndarrays 2D
## Asignación de valores en ndarrays
## Asignación utilizando matrices booleanas
## Asignación utilizando matrices booleanas, continuación
## Desafío: ¿Cuál es el aeropuerto más popular?
## Desafío: Cálculo de estadísticas de viajes con datos limpios
## Próximos pasos
