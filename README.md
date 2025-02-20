# Apache Log Viewer

Este é um aplicativo simples em Python para visualizar logs do Apache em tempo real usando uma interface gráfica com Tkinter.

## Funcionalidades

- Seleção de arquivos de log (.log, .txt)
- Exibição em tempo real do conteúdo do log
- Interface gráfica amigável

## Requisitos

- Python 3.x
- Tkinter (geralmente incluído na instalação padrão do Python)

## Como executar

1. Clone o repositório para o seu computador:

    ```sh
    git clone https://github.com/domwal/apache-log-viewer.git
    cd apache-log-viewer
    ```

2. Crie um ambiente virtual:

    - **Windows:**

        ```sh
        python -m venv venv
        venv\Scripts\activate
        ```

    - **Linux:**

        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Instale as dependências necessárias (se houver):

    ```sh
    pip install -r requirements.txt
    ```

4. Execute o aplicativo:

    ```sh
    python logview.py
    ```

5. Na interface do aplicativo, clique no botão "Selecionar Log" para escolher o arquivo de log que deseja visualizar.


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
