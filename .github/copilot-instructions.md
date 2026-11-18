# Repository instructions

## Project overview

- This is a small FastAPI learning project using the `src/` layout. The importable package is `fastapi_starter` under `src/fastapi_starter/`.
- The FastAPI application is created in `src/fastapi_starter/main.py`; routers are registered there and endpoint definitions belong in `src/fastapi_starter/router.py`.
- `database.py`, `model.py`, and `schema.py` are currently placeholders. SQLModel is a dependency, but database configuration and models are not yet implemented.
- `app/main.py` is a separate simple script, not the FastAPI application entry point.

## Development

- Use `uv` for dependency and environment management. The project requires Python 3.14 or newer.
- Install/synchronize dependencies with `uv sync`; run the API with `uv run fastapi dev src/fastapi_starter/main.py`.
- Add or change dependencies in `pyproject.toml` through `uv`, and keep `uv.lock` synchronized. Do not edit the lockfile by hand.
- The project currently has no configured test, lint, or type-check command. For behavior changes, add focused tests if a test setup exists or introduce only the minimal setup needed.

## Implementation conventions

- Preserve the `src/` package layout and use package-relative imports within `fastapi_starter`.
- Keep route handlers in the router module and include routers from the application module rather than defining application routes in `app/main.py`.
- Add type annotations to public functions and use FastAPI/Pydantic or SQLModel types appropriate to the feature.
- Keep request/response schemas separate from database models; put database engine and session dependencies in `database.py`, SQLModel table definitions in `model.py`, and API schemas in `schema.py`.
- Follow existing endpoint behavior unless the task explicitly asks to change it: `/` returns `{"message": "FastAPI is running"}` and `/health` returns `{"status": "ok"}`.
- Update `README.md` when setup, run commands, or project structure change. Avoid documenting planned database functionality as if it were already implemented.
