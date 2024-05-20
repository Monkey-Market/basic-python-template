import os
import subprocess


def initialize_git_repo(folder_path, name, email):
    # Inicializar repositorio de Git
    subprocess.run(["git", "init"], cwd=folder_path)

    # Configurar nombre y correo del usuario
    subprocess.run(["git", "config", "user.name", name], cwd=folder_path)
    subprocess.run(["git", "config", "user.email", email], cwd=folder_path)

    # Hacer commit inicial
    subprocess.run(["git", "add", "-A"], cwd=folder_path)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=folder_path)
    subprocess.run(["git", "checkout", "-b", "dev"], cwd=folder_path)


# Ejemplo de uso
folder_path = os.path.realpath(os.path.curdir)
name = "{{cookiecutter.author_name}}"
email = "{{cookiecutter.author_email}}"

initialize_git_repo(folder_path, name, email)
