# Transcriber

Sistema simples de transcrição de arquivos de áudio com persistência em banco de dados relacional (SQLite).

## 📌 Objetivo

Automatizar a transcrição de arquivos de áudio e armazenar os resultados de forma organizada e persistente.

## ⚙️ Funcionalidades

- Upload e transcrição de arquivos de áudio (WAV, MP3, etc).
- Armazenamento das transcrições no banco de dados SQLite.
- Interface CLI para inserção, edição, remoção e listagem das transcrições.
- Modelo de dados relacional com SQL.
- Estrutura modular e extensível.

## 🧱 Modelo de Dados

A estrutura principal está documentada em [docs/modelo_de_dados.md](docs/modelo_de_dados.md).

### Tabela `transcriptions`

| Campo        | Tipo     | Descrição                         |
|--------------|----------|------------------------------------|
| `id`         | INTEGER  | Identificador único da transcrição |
| `filename`   | TEXT     | Nome do arquivo de áudio original  |
| `transcription` | TEXT  | Texto transcrito do áudio          |
| `created_at` | TIMESTAMP | Data e hora da transcrição         |

## 🗃️ Banco de Dados

O sistema utiliza SQLite. O esquema do banco de dados é criado automaticamente ao iniciar o programa, caso não exista.

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/dirfel/transcriber.git
cd transcriber
