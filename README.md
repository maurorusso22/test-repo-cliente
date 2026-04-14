# test-repo-cliente

Repository di riferimento per pipeline CI/CD e documentazione interna di team.

## docs-team

`docs-team/` is a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) pointing to [test-repo-cliente-docs](https://github.com/maurorusso22/test-repo-cliente-docs). It contains shared internal documentation such as meeting notes and team references.

To clone this repo with the submodule:

```bash
git clone --recurse-submodules https://github.com/maurorusso22/test-repo-cliente.git
```

To update the submodule to the latest commit:

```bash
git submodule update --remote docs-team
```

## Pipelines

The `examples/` directory contains four ready-to-use mini-projects, each with its own GitHub Actions CI/CD pipeline (`.github/workflows/ci.yml`) and pre-commit hooks (`.pre-commit-config.yaml`).

| Example | Stack | CI Jobs |
|---------|-------|---------|
| [`backend-python`](examples/backend-python/) | FastAPI, uv, pytest | Code quality, Docker build, registry push |
| [`frontend-react`](examples/frontend-react/) | React 19, Vite, TypeScript, Vitest | Code quality, production build |
| [`fullstack-k8s`](examples/fullstack-k8s/) | FastAPI + React + Helm | Backend & frontend quality, Helm validation, Dockerfile security, Trivy scan, Docker build, container test, registry push |
| [`ml-data-pipeline`](examples/ml-data-pipeline/) | scikit-learn, Jupyter, nbstripout | Code quality, model validation, notebook execution, Docker build, Trivy scan, registry push |

Each example can be run locally with [`act`](https://github.com/nektos/act). Jobs that contact external services (Docker Hub, GitHub artifacts, security scanners) are automatically skipped during local execution.

See [`examples/README.md`](examples/README.md) for detailed usage instructions.
