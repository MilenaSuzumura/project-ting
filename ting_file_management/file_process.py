from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    for data in instance._data:
        if data["nome_do_arquivo"] == path_file:
            return None

    path = txt_importer(path_file)

    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(path),
        "linhas_do_arquivo": path
    }

    instance.enqueue(info)
    sys.stdout.write(f'{info}')


def remove(instance: Queue):
    if len(instance) != 0:
        name = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f'Arquivo {name} removido com sucesso\n')
    else:
        sys.stdout.write('Não há elementos\n')


def file_metadata(instance: Queue, position):
    try:
        search = instance.search(position)
        sys.stdout.write(f'{search}\n')
    except IndexError:
        sys.stderr.write("Posição inválida")
