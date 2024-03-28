import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, make_scorer

# Load the dataset into a DataFrame
df = pd.read_csv('House_Rent_Datasettest.csv')

# Drop 'Posted On' and 'Point of Contact' columns
df.drop(['Posted On', 'Point of Contact'], axis=1, inplace=True)

# Extract numerical information from 'Floor' column
df['Floor'] = df['Floor'].str.extract(r'(\d+)').astype(float)

# Handle missing values (if any)
# For example, drop rows with missing values:
df.dropna(inplace=True)

# Perform one-hot encoding for categorical variables
# Update the column names based on the actual column names in your dataset
columns_to_encode = ['Area Type', 'Area Locality', 'City', 'Furnishing Status', 'Tenant Preferred']
df_encoded = pd.get_dummies(df, columns=columns_to_encode)

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Scale numerical features
numerical_features = ['BHK', 'Size', 'Bathroom', 'Floor']
df_scaled = df_encoded.copy()
df_scaled[numerical_features] = scaler.fit_transform(df_encoded[numerical_features])

# Split the dataset into features (X) and target variable (y)
X = df_scaled.drop('Rent', axis=1)  # Features
y = df_scaled['Rent']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Selecting Random Forest Regressor:
model = RandomForestRegressor(random_state=42)

# 2. Hyperparameter Tuning:
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(model, param_grid, cv=2, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_

# 3. Cross-Validation:
cv_scores = cross_val_score(model, X_train, y_train, cv=2, scoring='neg_mean_squared_error')
mean_cv_score = cv_scores.mean()

# 4. Final Evaluation:
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Best Model Hyperparameters:", best_params)
print("Mean Cross-Validation Score:", mean_cv_score)
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared Score:", r2)
