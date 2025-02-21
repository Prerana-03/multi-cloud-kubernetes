from flask import Flask, request, jsonify  # ✅ CORRECT
import pandas as pd


import pandas as pd

app = Flask(__name__)

# Load dataset
# Load dataset
df = pd.read_csv("Greedy_Multi_Cloud_Selection_Dataset.csv")


# Greedy Algorithm for Multi-Cloud Selection
def select_best_cloud_provider(df):
    weights = {
        'Cost ($)': -0.4,  # Minimize
        'Latency (ms)': -0.3,  # Minimize
        'Success Rate (%)': 0.3,  # Maximize
        'Deployment Time (hrs)': -0.2,  # Minimize
        'Resource Utilization (%)': 0.2  # Balance
    }
    
    df_normalized = df.copy()
    for column in weights.keys():
        df_normalized[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    
    df_normalized['Selection Score'] = sum(weights[col] * df_normalized[col] for col in weights)
    best_providers = df_normalized.loc[df_normalized.groupby('Microservice Name')['Selection Score'].idxmax()]
    
    return best_providers[['Microservice Name', 'Cloud Provider', 'Selection Score']]

@app.route('/', methods=['GET'])
def home():
    return "Hello, Multi-Cloud with Docker and Kubernetes!"
    
@app.route('/best-cloud-provider', methods=['GET'])
def get_best_cloud_provider():
    best_providers = select_best_cloud_provider(df)
    return jsonify(best_providers.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
