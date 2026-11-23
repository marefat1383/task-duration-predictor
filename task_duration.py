import argparse

import numpy as np
from sklearn.ensemble import RandomForestRegressor

TRAINING_FEATURES = np.array([
    [1, 0, 1], [2, 1, 1], [3, 1, 2], [4, 2, 2],
    [5, 2, 3], [6, 3, 2], [7, 3, 3], [8, 4, 3],
    [9, 5, 4], [10, 6, 4], [3, 0, 1], [8, 2, 4],
], dtype=float)
TRAINING_HOURS = np.array([2, 4, 7, 10, 14, 18, 22, 28, 36, 45, 5, 20], dtype=float)


def build_model() -> RandomForestRegressor:
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(TRAINING_FEATURES, TRAINING_HOURS)
    return model


def predict_hours(complexity: int, dependencies: int, team_size: int) -> float:
    if not 1 <= complexity <= 10 or dependencies < 0 or team_size <= 0:
        raise ValueError("Complexity must be 1-10; dependencies cannot be negative; team size must be positive")
    result = float(build_model().predict([[complexity, dependencies, team_size]])[0])
    return round(max(0.0, result), 2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate task duration in hours.")
    parser.add_argument("--complexity", type=int, required=True)
    parser.add_argument("--dependencies", type=int, required=True)
    parser.add_argument("--team-size", type=int, required=True)
    args = parser.parse_args()
    print(f"Estimated duration: {predict_hours(args.complexity, args.dependencies, args.team_size)} hours")


if __name__ == "__main__":
    main()
