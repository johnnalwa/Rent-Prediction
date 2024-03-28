# preprocessing.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(input_data):
    """
    Preprocesses the input data before making predictions.
    
    Args:
    - input_data: Dictionary containing the input data
    
    Returns:
    - preprocessed_data: Preprocessed data ready for making predictions
    """
    # Load the input data into a DataFrame
    df = pd.DataFrame(input_data, index=[0])
    
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
    
    # Return the preprocessed data
    return df_scaled.to_dict(orient='records')[0]
