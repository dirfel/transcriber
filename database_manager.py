import csv
import os

class DatabaseCSV:
    def __init__(self, filename='database.csv'):
        self.filename = filename
        self.fieldnames = ['data-hora', 'transcrição', 'caminho_audio']
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()

    def read_all(self):
        with open(self.filename, newline='', encoding='utf-8') as file:
            return list(csv.DictReader(file))

    def add_entry(self, data_hora, transcricao, caminho_audio):
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow({
                'data-hora': data_hora,
                'transcrição': transcricao,
                'caminho_audio': caminho_audio
            })

    def update_entry(self, index, data_hora=None, transcricao=None, caminho_audio=None):
        registros = self.read_all()
        if 0 <= index < len(registros):
            if data_hora is not None:
                registros[index]['data-hora'] = data_hora
            if transcricao is not None:
                registros[index]['transcrição'] = transcricao
            if caminho_audio is not None:
                registros[index]['caminho_audio'] = caminho_audio
            self._write_all(registros)
            return True
        return False

    def delete_entry(self, index):
        registros = self.read_all()
        if 0 <= index < len(registros):
            registros.pop(index)
            self._write_all(registros)
            return True
        return False

    def _write_all(self, registros):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(registros)
