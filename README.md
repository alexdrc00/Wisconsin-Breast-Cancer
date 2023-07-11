# Wisconsin Breast Cancer
## About
<p align='justify'>We are going to use <a href=https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic>Wisconsin's Breast Cancer Diagnosis dataset</a>.The dataset has 569 samples and 32 variables. These variables were obtained through the analysis of the characteristics of the cellular nuclei from digitized images of breast tissue samples acquired through fine needle aspiration [FNA] biopsy techniques. An example of two different images obtained through these techniques can be seen below, a benign case on the left and malign on the right. </p>

![FNA Images of both Benign and Malign diagnosis](imgs/FNA.png)
  
<p align='justify'>If we take a look at the variables we can see all but the id and target variable ('diagnosis') are presented divided in three metrics according to their suffix: _mean (average of all samples), _se (standard error) and _worst (average of three worst values). Brief explanation of these variables: </p>
<ul>
<li><b>radius:</b> distance from the center of the nuclei to points in the perimeter
<li><b>texture:</b> standard deviation of values in the grayscale
<li><b>perimeter:</b> perimeters of the nuclei in the image
<li><b>area:</b> areas of the nuclei in the images
<li><b>smooothness:</b> local variations of the radius elongation. Measure of cells's border irregularities
<li><b>compactness:</b> perimeter^2/area - 1.0
<li><b>concavity:</b> severity of the concave portions in the contour. Understanding as more severe or higher concavity, those contours with many "gaps" or depressions. In a broader sense, it can indicate how irregular the shape of the nucleus is.
<li><b>symmetry:</b> symmetry of the nuclei. Calculation method unspecified
<li><b>fractal_dimension:</b> measures how 'irregular' the nuclei's contour is

As for <b>id</b> and <b>diagnosis</b> they are just a unique identifier and the target variable [M=malign, B=benign].
