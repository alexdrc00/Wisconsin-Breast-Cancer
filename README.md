# Wisconsin Breast Cancer
## About
<p align='justify'>We are going to use <a href=https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic>Wisconsin's Breast Cancer Diagnosis dataset</a>.The dataset has 569 samples and 32 variables. These variables were obtained through the analysis of the characteristics of the cellular nuclei from digitized images of breast tissue samples acquired through fine needle aspiration [FNA] biopsy techniques. An example of two different images obtained through these techniques can be seen below, a benign case on the left and malign on the right. </p>
  
  
<p align='justify'>If we take a look at the variables we can see all but the id and target variable ('diagnosis') are presented divided in three metrics according to their suffix: _mean (average of all samples), _se (standard error) and _worst (average of three worst values). Brief explanation of these variables: </p>
<ul>
<li><b>radius:</b> distancia del centro del núcleo a puntos en el perimetro
<li><b>texture:</b> desviación estandar de los valores de la escala de grises
<li><b>perimeter:</b> perímetros de los núcleos de la imagen
<li><b>area:</b> áreas de los núcleos de la imagen
<li><b>smooothness:</b> variación local en las longitudes de radio. Medida de cuán regulares o irregulares son las fronteras de las celulas
<li><b>compactness:</b> perimetro^2/area - 1.0
<li><b>concavity:</b> severidad de las porciones cóncavas del entorno. Entendiendose por más severas aquellos contornos con muchos 'huecos', puede indicar la irrgularidad de la forma del núcleo
<li><b>concave points:</b> número de porciones concavas del contorno
<li><b>symmetry:</b> simetría del núcleo. No especifica método de cáclculo
<li><b>fractal_dimension:</b> Mide que tan 'irregular' es el contorno de los núcleos
