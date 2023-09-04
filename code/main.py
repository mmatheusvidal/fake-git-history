import typer
from datetime import datetime
import json
import configparser
from pathlib import Path

app = typer.Typer()

hora_format = "%H:%M:%S"
now = datetime.now()
today = datetime.strftime(now, "%d/%m/%Y")
hour = datetime.strftime(now, hora_format)

with open('tasks.json') as f:
    data = json.load(f)

spot = data['tasks'][-1]

def close():
    with open('tasks.json', 'w') as f:
        json.dump(data, f)

@app.command()
def init():
    projectPath = Path.cwd()
    dbPath = "task.json"
    db = str(projectPath) + "\\" + dbPath

    init_file = {"tasks": []}
    
    if Path(db).exists() == True:
        print('Banco de Dados já existe, inicie seu dia')
    else:
        print('Banco de dados não existe')
        with open (db, 'w') as file:
            json.dump(init_file, file)
        print('Banco de dados criado, inicie seu dia')

@app.command(name= 'list')
def list_tasks():
    with open('tasks.json') as f:
        data = json.load(f)
    d = data['tasks']

    for i in range(len(d)):
        dia = list(d[i].keys())[0]
        tasks = len(d[i][dia]['tasks'])
        print(f'{i}| {dia}: {tasks} tasks')

@app.command(name= 'clean-day')
def clean_day(id: int):
    with open('tasks.json') as f:
        data = json.load(f)
    d = data['tasks']
    d.pop(id)
    with open('tasks.json', 'w') as f:
        json.dump(d, f)

@app.command()
def inicio():
    insert_data = {
        today: {
            "inicio": hour,
            "tasks": []}}
    data['tasks'].append(insert_data)
    close()

@app.command()
def almoco():
    spot[today]["almoco"] = hour
    close()

@app.command()
def almoco_final():
    spot[today]["almoco_final"] = hour
    close()

@app.command()
def final():
    spot[today]["end_hour"] = hour
    close()
    calc()

@app.command()
def task(task: str):
    spot[today]['tasks'].append(task)
    close()

def convert(field):
    field = datetime.strptime(spot[today][field], hora_format)
    return field

def calc():
    inicio = convert('inicio')
    almoco = convert('almoco')
    almoco_final = convert('almoco_final')
    end_hour = convert('end_hour')
    
    horas = str(end_hour - inicio - (almoco_final - almoco))
    spot[today]["total_horas"] = horas
    close()

if __name__ == "__main__":
    app()