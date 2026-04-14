import pytest

from src.predict import predict, train_model


@pytest.mark.model_validation
def test_model_produces_valid_classes():
    model = train_model()
    samples = [
        [5.1, 3.5, 1.4, 0.2],
        [6.7, 3.0, 5.2, 2.3],
        [5.8, 2.7, 4.1, 1.0],
    ]
    results = predict(model, samples)
    assert len(results) == 3
    for r in results:
        assert r in [0, 1, 2], f"Classe non valida: {r}"


@pytest.mark.model_validation
def test_model_accuracy_above_threshold():
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    iris = load_iris()
    _, X_test, _, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = train_model()
    predictions = predict(model, X_test.tolist())
    accuracy = sum(p == t for p, t in zip(predictions, y_test)) / len(y_test)
    assert accuracy > 0.8, f"Accuracy troppo bassa: {accuracy:.2f}"
