
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from epita_group5_space.client import get_apod

console = Console()


def main():
    try:
        data = get_apod()

        # The new endpoint may return a list of records.
        if isinstance(data, list):
            if not data:
                raise ValueError("NASA returned an empty list.")
            data = data[0]

        if not isinstance(data, dict):
            raise ValueError("Unexpected response format from NASA.")

        def get_value(key, default="N/A"):
            value = data.get(key, default)

            # WordPress APIs sometimes wrap text in {"rendered": "..."}.
            if isinstance(value, dict):
                value = value.get("rendered", default)

            return str(value) if value else default

        table = Table(title="NASA Astronomy Picture of the Day")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="magenta")

        table.add_row("Title", get_value("title"))
        table.add_row("Date", get_value("date"))
        table.add_row("Media Type", get_value("media_type"))
        table.add_row("Explanation", get_value("explanation"))
        table.add_row("Image URL", get_value("url", get_value("link")))

        console.print(
            Panel(
                table,
                title="EPITA Group 5 — Space & Astronomy",
                expand=False,
            )
        )

    except (RuntimeError, ValueError) as error:
        console.print(f"[bold red]Error:[/bold red] {error}")


if __name__ == "__main__":
    main()
