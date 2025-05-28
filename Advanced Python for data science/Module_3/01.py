# Advanced Machine Learning with Scikit-Learn
'''
Custom Transformers and Pipelines
Custom transformers ensure reusable preprocessing steps.

'''
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

class LogTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return np.log1p(X)
    
'''
BaseEstimator: Provides get_params() and set_params() methods for parameter handling
TransformerMixin: Automatically provides fit_transform() method by combining fit() and transform()
fit(): Usually learns parameters from training data, but here it's stateless (no parameters to learn)
transform(): Applies log transformation using np.log1p(X) which computes log(1 + X)

Why log1p? It's numerically stable for small values and handles zeros (since log(0) is undefined, but log(1 + 0) = 0).

'''

# Pipeline
pipeline = Pipeline([
    ('log', LogTransformer()),
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression())
])
'''
The pipeline processes data sequentially:

Log transformation: Reduces skewness in data distribution
Standardization: Scales features to have zero mean and unit variance
Classification: Fits logistic regression model

'''
# Fit and predict
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)

'''
When dealing with right-skewed financial data 
(like income, sales), 
the log transformation makes the distribution 
more normal, improving model performance.

'''