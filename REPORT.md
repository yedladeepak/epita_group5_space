# TP2 Report — Group 5: Space & Astronomy

## 1. Project Overview

Our project focuses on retrieving and displaying information about NASA's Astronomy Picture of the Day (APOD). We used Python and `uv` to set up the project environment, manage dependencies, load configuration settings, make HTTP requests, and create a command-line interface.

The project is organized as a Python package named `epita-group5-space`, version `0.1.0`, requiring Python 3.12 or newer.

## 2. Python Environment Inspection

We used `scripts/inspect_env.py` to compare the system Python installation with the project's virtual environment.

### System Python

Command:

```bash
python3 scripts/inspect_env.py
```

The output showed:

- Python version: `3.14.4`
- Python executable: `/Library/Frameworks/Python.framework/Versions/3.14/bin/python3`
- Virtual environment: `False`

This command used the system Python installation rather than the project's virtual environment.

### Project Virtual Environment

Command:

```bash
uv run python scripts/inspect_env.py
```

The output showed:

- Python version: `3.12.7`
- Python executable: the project's `.venv/bin/python`
- Virtual environment: `True`
- Base Python installation: `/opt/anaconda3`

The two commands used different Python interpreters. Using a virtual environment helps keep project dependencies separate from globally installed packages and makes the development setup more consistent across the team.

### Understanding the Environment

- `sys.executable` shows the Python executable currently running.
- `sys.prefix` identifies the active Python environment.
- `sys.base_prefix` identifies the base Python installation.
- `sys.path` lists the locations Python searches when importing modules.
- `PATH` is the shell variable used to locate executable commands.

## 3. Configuration and API Client

We separated configuration settings from the code responsible for making API requests.

### Configuration — `config.py`

The configuration module uses `python-dotenv` to load environment variables from a local `.env` file. It defines a `Settings` dataclass containing:

- `NASA_API_KEY`: the configured API key.
- `APP_ENV`: the application environment, defaulting to `development`.
- `DEBUG`: a Boolean debug setting.

The `validate()` method checks whether the API key is configured before the client makes a request.

We use `.env.template` to document the required configuration. The real `.env` file contains a secret and must not be committed to Git or included in the submission ZIP.

### API Client — `client.py`

The client uses the `requests` library to send HTTP requests, check unsuccessful responses, and handle request errors.

During development, the original NASA APOD endpoint returned an HTTP 500 error. We changed the endpoint to:

`https://science.nasa.gov/wp-json/wp/v2/apod-basic`

This endpoint returns data in a different structure, so the CLI was adjusted to handle a list response. We then ran the updated CLI and obtained the expected output for our implementation.

### Command-Line Interface — `cli.py`

The CLI connects the API client to the terminal interface and displays the retrieved APOD information. The package's command-line entry point is defined in `pyproject.toml`.

## 4. Dependencies and `uv`

We used `uv` to manage the project's Python dependencies.

The main dependencies are:

- `requests` — sends HTTP requests.
- `python-dotenv` — loads environment variables.
- `rich` — supports formatted terminal output.

We also included `pytest` in the development dependency group for testing.

The `pyproject.toml` file contains the package metadata, Python version requirement, dependencies, build configuration, and CLI entry point. The `uv.lock` file records the resolved dependency versions.

Useful commands:

```bash
uv sync
uv tree
uv run python scripts/inspect_env.py
uv build
```

The `uv tree` command displays the dependency hierarchy. Direct dependencies are declared by our project, while transitive dependencies are installed because another package requires them.

## 5. Package Build

We built the package using:

```bash
uv build
```

The build completed successfully and generated distribution files in the `dist/` directory, including a wheel and a source distribution.

A wheel is generally faster to install because it is already packaged for installation. A source distribution contains the source code and build metadata, and installation may require a build step and additional tools.

## 6. TestPyPI Publication

We attempted to publish the package using TestPyPI:

```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token "YOUR_TESTPYPI_TOKEN"
```

The upload failed with `403 Forbidden` because TestPyPI rejected the authentication information.

Therefore, the package build is complete, but successful TestPyPI publication and installation have not yet been verified. We need to check the token, retry the upload, and test installation from TestPyPI.

After successful publication, the package page should be available at:

https://test.pypi.org/project/epita-group5-space/

This link must be checked after publishing before we claim the package is available.

## 7. Debugging Challenge

The original debugging challenge requires us to inspect the supplied starter code, identify the data-type problem, follow the call stack, correct the code, and verify the output.

The final report must include the actual runtime types observed during debugging, the reason for the original error, the code correction, and the verified output.

**Status:** The original debugging procedure and results still need to be verified before this task can be marked complete.

## 8. Running the Project

To set up the project on another machine:

1. Install a compatible Python version and `uv`.
2. Open the project directory.
3. Create a local `.env` file using `.env.template` as a guide.
4. Add a valid API key to the local `.env` file.
5. Install the project dependencies:

   ```bash
   uv sync
   ```

6. Inspect the Python environment:

   ```bash
   uv run python scripts/inspect_env.py
   ```

7. Build the package:

   ```bash
   uv build
   ```

8. Run the CLI using the entry point configured in `pyproject.toml`, after confirming the package is installed in the environment.

Never share the real `.env` file or commit it to the repository.

## 9. Current Project Status

| Task | Status |
|---|---|
| Python environment inspection | Completed |
| Configuration and API client | Implemented and run locally |
| CLI execution | Run successfully with the updated endpoint |
| Package build with `uv build` | Successful |
| TestPyPI publication | Pending authentication fix |
| TestPyPI installation verification | Pending |
| Original debugging challenge | Requires verification and documentation |

## 10. Conclusion

This project helped us work with Python virtual environments, dependency management, environment variables, HTTP requests, command-line tools, and package building. We successfully built the package and ran the updated CLI locally.

The remaining work is to resolve TestPyPI authentication, verify installation from the package index, and complete the original debugging challenge before marking all assignment requirements as finished.