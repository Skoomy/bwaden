# BWADEN 🚀


```sh
docker compose exec backend bash
```

## Running the Project with Docker

1. **Build the Docker image**:

```bash
   docker-compose build
```

2. **Run container**

```bash
docker-compose up
```
3. **Stop container

```sh
docker-compose down
```


## Pre-requisites

### Setting Up Pre-Commit Hooks

Pre-commit hooks are used to enforce code quality and consistency before each commit. Follow these steps to set it up:

1. **Install pre-commit**:
   ```bash
   pip install pre-commit
   ```

2. Install the hook

```sh
pre-commit install
```

3. Run precommit on each file

```sh
pre-commit run --all-files
```

## Teckstack

- Django
