
import requests

from epita_group5_space.config import config

APOD_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"


def get_apod(date=None):
    """Fetch NASA's Astronomy Picture of the Day."""
    config.validate()

    params = {"api_key": config.api_key}

    if date:
        params["date"] = date

    try:
        response = requests.get(
            APOD_URL,
            params=params,
            timeout=15,
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as exc:
        raise RuntimeError(
            f"Could not retrieve NASA APOD data: {exc}"
        ) from exc
