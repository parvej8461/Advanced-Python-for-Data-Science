'''
Hyperparameter Tuning
Optimize models with grid search.
'''

from sklearn.model_selection import GridSearchCV

param_grid = {'clf__C': [0.1, 1, 10]}
grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)

