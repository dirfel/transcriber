# Modelo de Dados

Este documento descreve a estrutura do banco de dados relacional utilizado no sistema Transcriber.

## Entidades

### Transcriptions
Armazena as transcrições de arquivos de áudio.

| Campo        | Tipo     | Restrições                        | Descrição                         |
|--------------|----------|-----------------------------------|------------------------------------|
| `id`         | INTEGER  | PRIMARY KEY, AUTOINCREMENT       | Identificador único da transcrição |
| `filename`   | TEXT     | NOT NULL                         | Nome do arquivo de áudio original  |
| `transcription` | TEXT  | NOT NULL                         | Texto transcrito do áudio          |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP        | Data e hora da transcrição         |

## Relacionamentos
Atualmente, o sistema possui apenas uma tabela. Futuras versões podem incluir:

- Usuários que realizam transcrições
- Logs de atividade
- Histórico de alterações

## Regras e Restrições

- Um `filename` não pode estar vazio.
- A `transcription` deve ser preenchida com o conteúdo resultante da transcrição automática ou manual.
