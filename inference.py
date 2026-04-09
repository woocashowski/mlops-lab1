import joblib


def load_model():
    return joblib.load("model.joblib")


def predict(model, data: dict) -> str:
    class_names = ["setosa", "versicolor", "virginica"]
    values = list(data.values())
    prediction = model.predict([values])
    return class_names[prediction[0]]
