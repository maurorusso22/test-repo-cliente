# CI/CD Pipeline Examples

Ready-to-use example projects for common scenarios. Each example includes source code, tests, Dockerfile, a GitHub Actions pipeline (`.github/workflows/ci.yml`), and pre-commit hooks (`.pre-commit-config.yaml`).

## Available Scenarios

| Scenario | Directory | Use Case | Key Tools |
|----------|-----------|----------|-----------|
| Backend Python API | `backend-python/` | REST APIs, Python microservices | black, flake8, isort, mypy, pytest, Docker |
| Frontend React/Next.js | `frontend-react/` | SPA, SSR, frontend apps | Prettier, ESLint, TypeScript, Vitest |
| Fullstack + K8s | `fullstack-k8s/` | Full-stack apps with Kubernetes deployment | All of the above + Helm, Trivy, Hadolint |
| ML/Data Pipeline | `ml-data-pipeline/` | ML serving, data pipelines | black, pytest, nbstripout, model validation, Docker |

## How to Use an Example

1. Copy the desired example directory as the base for a new project
2. Move `.github/workflows/ci.yml` to the root of the new repo
3. Install pre-commit and activate hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```
4. Adjust names, paths, and versions in `ci.yml` and `pyproject.toml`/`package.json`

## Running Pipelines Locally

### Using `act` (full GitHub Actions simulation)

[`act`](https://github.com/nektos/act) runs GitHub Actions workflows locally using Docker.

**Installation:**

```bash
brew install act
```

**Usage (from an example directory):**

```bash
# Run the entire pipeline
cd examples/backend-python
act

# Run a specific job
act -j quality

# Run only on a specific event
act pull_request

# Dry run (show what would execute without running)
act -n
```

**Tips:**

- On first run, `act` will ask which Docker image to use. Choose **Medium** for a good speed/compatibility trade-off.
- Pass secrets with `act -s DOCKER_USERNAME=xxx -s DOCKER_TOKEN=yyy` or create a `.secrets` file.
- Skip registry push jobs by targeting specific jobs: `act -j quality`.

### Running Quality Checks Directly

If you only want to test the quality checks without simulating the full GitHub Actions environment:

**Backend Python:**

```bash
cd examples/backend-python
uv sync --all-extras
uv run black --check .
uv run flake8 src/ tests/
uv run isort --check-only .
uv run mypy src/
uv run pytest --cov=src
```

**Frontend React:**

```bash
cd examples/frontend-react
npm ci
npx prettier --check .
npx eslint . --max-warnings 0
npx tsc --noEmit
npx vitest run
```

**ML/Data Pipeline:**

```bash
cd examples/ml-data-pipeline
uv sync --all-extras
uv run black --check .
uv run flake8 src/ tests/
uv run pytest -m "not slow"
uv run python scripts/validate_model.py
```

### Running Pre-commit Hooks

```bash
# Run all hooks against all files
pre-commit run --all-files

# Run a specific hook
pre-commit run black --all-files
```

## Required Secrets (GitHub)

| Secret | Used In | Description |
|--------|---------|-------------|
| `DOCKER_USERNAME` | All scenarios with Docker | Docker Hub username |
| `DOCKER_TOKEN` | All scenarios with Docker | Docker Hub access token |

## Updating Hooks

Run periodically to update hook versions:

```bash
pre-commit autoupdate
```

## Design Principles

- Pre-commit hooks are a **subset** of CI checks: they catch issues locally before pushing
- CI runs additional checks that require infrastructure (Docker build, Trivy scan, container tests)
- Formatting/linting configurations are aligned between CI and pre-commit to avoid drift
