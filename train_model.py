import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    "crime_rate": [10, 20, 30, 70, 80, 90],
    "street_lighting": [9, 8, 7, 3, 2, 1],
    "crowd_density": [8, 7, 6, 3, 2, 1],
    "police_patrol": [9, 8, 7, 3, 2, 1],
    "safe": [1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

X = df[["crime_rate",
        "street_lighting",
        "crowd_density",
        "police_patrol"]]

y = df["safe"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model Created Successfully")