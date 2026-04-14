from src.predict import predict, train_model


def test_train_model():
    model = train_model()
    assert model is not None


def test_predict():
    model = train_model()
    result = predict(model, [[5.1, 3.5, 1.4, 0.2]])
    assert len(result) == 1
    assert result[0] in [0, 1, 2]
