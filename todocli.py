import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()

@app.command(short_help="adds an item")
def add(task: str, category: str):
    typer.echo(f"Adding {task}, to {category}")

@app.command(short_help="deletes an item")
def delete(position: int):
    typer.echo(f"Deleting {position}")

@app.command(short_help="updates an item")
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"Updating {position}")

@app.command(short_help="mark a task as in progress")
def mark_in_progress(task_id: int):
    typer.echo(f"Marking {task_id} as in progress")

@app.command(short_help="mark task as done")
def mark_done(task_id: int):
    typer.echo(f"Marking {task_id} as done")

@app.command(short_help="list tasks that are not done")
def list_todo():
    typer.echo(f"Listing all tasks that are not done")

@app.command(short_help="list tasks that in progress")
def list_in_progress():
    typer.echo(f"Listing all tasks that are in progress")

@app.command(short_help="list tasks that are done")
def list_done():
    typer.echo(f"Listing all tasks that are done")

@app.command(short_help="list all tasks")
def list_all():
    typer.echo("Listing all tasks")



if __name__ == "__main__":
    app()