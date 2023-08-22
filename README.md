# Wisconsin Breast Cancer
## About
<p align='justify'>We are going to use <a href=https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic>Wisconsin's Breast Cancer Diagnosis dataset</a>.The dataset has 569 samples and 32 variables. These variables were obtained through the analysis of the characteristics of the cellular nuclei from digitized images of breast tissue samples acquired through fine needle aspiration [FNA] biopsy techniques. An example of two different images obtained through these techniques can be seen below, a benign case on the left and malign on the right. </p>

<p align="center">
  <img src="imgs/FNA.png" alt="[FNA Images of both Benign and Malign cases">
</p>

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
</ul>

As for <b>id</b> and <b>diagnosis</b> they are just a unique identifier and the target variable [M=malign, B=benign].

## Procedure
<p align='justify'>The objective will be to develop an effective model for breast cancer diagnosis and look into the main features that suggest this diagnosis. The metric for success we are going to use is the f1-scoe. We could conside scenarios where other metrics might be more suitable:
<ul>
<li> Wrongly diagnosing a patient's cell as malign and thus unnecessarily moving them to the proceding treatment carries severe consequences and threatens the patient's life. In that case, we would want to maximize precision so we do not commit any type I error. 
<li> (Most logical one) After diagnosing a patient's cell as malign, further test will be carried out to confirm the diagnosis. In this case we want to reduce the number of false negatives therefore we are going to maximize recall.
</ul>
Recall would be a logical choice too, however, we are going to use f1-score this time and aim for a compromise. The steps will be the standard:
<ol>
<li>EDA
<li>Data Preprocessing
<li>Feature Engineering and Selection
<li>Models development
<li>Model selection and final analysis
</ol></p>

## Conclusions
<p align='justify'>The most promising results have been obtained by the MLP (without PCA preprocessing) and the Logistic Regression once added some fine-tuning and preprocessing. While the MLP achieves the highest F1 score with a centesimal above its contrary, and recall, I would stick with logistic regression for its simplicity and high explainability, however, again if we were to just go for results, MLP would then be the choice. RF found concativity_points_worst to be the most relevant variable in the detection, further analysis could be done with XAI such as SHAP values.
Final results for Logistic:
  
<div align="center"> 

| Model | Precision | Recall | F1 Score |
|----------|----------|----------|----------|
| Log. Reg.    | 1.0  | 0.952381  | 0.975610  |
| MLP    | 1.0  | 0.976190  | 0.987952  |

</div>
</p>
