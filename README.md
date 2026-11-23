# Task Duration Predictor

A small educational AI project that estimates task duration from complexity, number of dependencies, and team size using Random Forest regression.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python task_duration.py --complexity 7 --dependencies 3 --team-size 2
```

## Test

```bash
python -m unittest test_task_duration.py
```

The training data is synthetic and intended for learning rather than project-management commitments.
