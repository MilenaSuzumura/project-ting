import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, 'r') as f:
                return f.read().split("\n")

        except FileNotFoundError:
            sys.stderr.write("Arquivo {path_file} não encontrado\n".format(
                path_file=path_file))

    else:
        sys.stderr.write("Formato inválido")
