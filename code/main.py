import typer
import os

app = typer.Typer()

@app.command()
def hello(name: str, idade: int, display_idade: bool = True):
    print(f'É nóis {name}')
    if display_idade:
        print(f'{idade}')

@app.command()
def goodbye():
    os.system("git add .")
    
    os.system("git commit -m teste")
    os.system("git push")

if __name__ == "__main__":
    app()