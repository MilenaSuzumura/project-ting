import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, 'r') as f:
                return f.read().split("\n")

        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    else:
        sys.stderr.write("Formato inválido")
