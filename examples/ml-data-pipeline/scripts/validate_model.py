"""Validazione del modello: verifica che produca output coerenti."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.predict import predict, train_model


def main():
    model = train_model()

    test_input = [[5.1, 3.5, 1.4, 0.2]]
    result = predict(model, test_input)

    if len(result) != 1:
        print(f"ERRORE: atteso 1 risultato, ottenuti {len(result)}")
        sys.exit(1)

    if result[0] not in [0, 1, 2]:
        print(f"ERRORE: classe non valida: {result[0]}")
        sys.exit(1)

    print(f"Validazione OK: predizione={result[0]}")


if __name__ == "__main__":
    main()
