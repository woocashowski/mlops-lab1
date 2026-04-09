from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib


def load_data():
    return load_iris()


def train_model(data):
    model = DecisionTreeClassifier()
    model.fit(data.data, data.target)
    return model


def save_model(model):
    joblib.dump(model, "model.joblib")


if __name__ == "__main__":
    data = load_data()
    model = train_model(data)
    save_model(model)
