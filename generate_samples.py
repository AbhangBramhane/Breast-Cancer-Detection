from sklearn.datasets import load_breast_cancer
import json

# Load dataset
cancer = load_breast_cancer()

X = cancer.data
y = cancer.target

# Find one benign sample (target = 1)
benign = X[y == 1][0]

# Find one malignant sample (target = 0)
malignant = X[y == 0][0]

sample_data = {
    "benign": benign.tolist(),
    "malignant": malignant.tolist()
}

with open("static/samples.json", "w") as f:
    json.dump(sample_data, f, indent=4)

print("samples.json created successfully!")