from joblib import load

def predict(data):
    '''Function to make predictions
    '''
    # Load Model
    model = load('lasso_fit.joblib')

    # Make predictions
    predictions = model.predict(data)

    return predictions