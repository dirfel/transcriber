# Transcriber

**Transcriber** é uma aplicação web desenvolvida em Python que permite aos usuários transcrever arquivos de áudio de forma simples e eficiente. Com uma interface amigável, os usuários podem fazer upload de arquivos de áudio e obter a transcrição correspondente.

## Funcionalidades

- Upload de arquivos de áudio para transcrição.
- Interface web intuitiva para interação com o usuário.
- Armazenamento de transcrições em um banco de dados CSV.

## Tecnologias Utilizadas

- Python
- Flask (framework web)
- HTML, CSS e JavaScript para o frontend
- Bibliotecas de processamento de áudio (especificar quais, se aplicável)

## Estrutura do Projeto

```
transcriber/
├── app.py                 # Arquivo principal da aplicação Flask
├── database.csv           # Banco de dados CSV para armazenar transcrições
├── database_manager.py    # Gerenciador de operações no banco de dados
├── utils.py               # Funções utilitárias
├── templates/
│   └── index.html         # Template HTML principal
├── static/
│   ├── style/             # Arquivos CSS
│   └── scripts/           # Arquivos JavaScript
└── README.md              # Documentação do projeto
```

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/dirfel/transcriber.git
   cd transcriber
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Inicie a aplicação:

   ```bash
   python app.py
   ```

2. Acesse a aplicação no navegador:

   ```
   http://localhost:5000
   ```

3. Faça upload de um arquivo de áudio e aguarde a transcrição ser exibida.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

*Nota: Para informações mais detalhadas sobre as bibliotecas de processamento de áudio utilizadas ou outras especificações técnicas, consulte os arquivos do projeto ou entre em contato com o mantenedor.*
