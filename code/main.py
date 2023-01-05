import typer
import os

app = typer.Typer()

# --date mm/dd/aaaa

@app.command()
def hello(name: str, idade: int, display_idade: bool = True):
    print(f'É nóis {name}')
    if display_idade:
        print(f'{idade}')

@app.command()
def commit(data: str):
    os.system(f"echo \'{data}\' > foo.txt")
    os.system("git add .")
    os.system(f'git commit -m \"fake commit\" --date \"{data}\"')
    os.system("git push")

if __name__ == "__main__":
    app()