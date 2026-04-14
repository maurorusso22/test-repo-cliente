from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_model():
    """Addestra un classificatore sul dataset Iris."""
    iris = load_iris()
    X_train, _, y_train, _ = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    return model


def predict(model, data: list[list[float]]) -> list[int]:
    """Esegue predizioni con il modello fornito."""
    return model.predict(data).tolist()
