
import pandas as pd
import os

FILE = "alunos.csv"

def load():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    return pd.DataFrame(columns=["matricula", "nome", "curso"])

def save(df):
    df.to_csv(FILE, index=False)

def inserir():
    df = load()
    matricula = input("Matrícula: ")
    nome = input("Nome: ")
    curso = input("Curso: ")
    df.loc[len(df)] = [matricula, nome, curso]
    save(df)
    print("Aluno inserido!")

def pesquisar():
    df = load()
    mat = input("Matrícula para pesquisar: ")
    aluno = df[df["matricula"] == mat]
    if aluno.empty:
        print("Não encontrado.")
    else:
        print(aluno)

def editar():
    df = load()
    mat = input("Matrícula do aluno para editar: ")
    if mat in df["matricula"].values:
        nome = input("Novo nome: ")
        curso = input("Novo curso: ")
        df.loc[df["matricula"] == mat, ["nome", "curso"]] = [nome, curso]
        save(df)
        print("Aluno editado!")
    else:
        print("Aluno não encontrado.")

def remover():
    df = load()
    mat = input("Matrícula do aluno para remover: ")
    df = df[df["matricula"] != mat]
    save(df)
    print("Aluno removido!")

while True:
    print("\n1 - Inserir")
    print("2 - Pesquisar")
    print("3 - Editar")
    print("4 - Remover")
    print("5 - Sair")
    op = input("Escolha: ")

    if op == "1":
        inserir()
    elif op == "2":
        pesquisar()
    elif op == "3":
        editar()
    elif op == "4":
        remover()
    elif op == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
