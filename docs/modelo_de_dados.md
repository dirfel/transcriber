# Modelo de Dados: Transcriber

## Entidade: `transcriptions`

Tabela responsável por armazenar os arquivos transcritos.

| Campo       | Tipo       | Descrição                                |
|-------------|------------|------------------------------------------|
| `id`        | INTEGER    | Identificador único (chave primária)     |
| `filename`  | TEXT       | Nome do arquivo de áudio                 |
| `transcription` | TEXT   | Texto transcrito                         |
| `created_at`| TIMESTAMP  | Data/hora da criação da transcrição      |

## Restrições

- `filename` e `transcription` são obrigatórios (`NOT NULL`)
- `id` é gerado automaticamente (`AUTOINCREMENT`)
- A data de criação é atribuída automaticamente (`DEFAULT CURRENT_TIMESTAMP`)

## Futuras Expansões

- Adicionar campo `language` para suportar multilinguagem
- Relacionar com tabela de usuários (para autenticação)
