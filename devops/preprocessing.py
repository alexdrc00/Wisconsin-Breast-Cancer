from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def preprocessing(data):
    '''Preprocessing function of the pipeline 
    '''
    preprocessing = Pipeline(steps=[('scaler',StandardScaler()),
                                    ('pca', PCA(n_components=9, svd_solver='full', random_state=42))])
    

    preprocessed_data = preprocessing.fit_transform(data['concave points_mean' 'radius_se' 'radius_worst' 'texture_worst'
 'area_worst' 'smoothness_worst' 'concave points_worst' 'symmetry_worst'])

    return preprocessed_data