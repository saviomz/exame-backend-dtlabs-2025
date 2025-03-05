🚀 Como Iniciar o Projeto
Para executar este projeto, siga os passos abaixo:

📌 Pré-requisitos
Certifique-se de ter o Docker e o Visual Studio Code instalados em seu ambiente.

⚙️ Inicializando o Sistema
Abra o projeto no VS Code
No terminal, navegue até o diretório do projeto e execute o seguinte comando para iniciar os containers Docker:

    docker compose up -d --build
    
Inicie a aplicação FastAPI
Após a inicialização do Docker, execute o comando abaixo para rodar o servidor:

    uvicorn main:app --reload


Acesse a documentação da API
O sistema estará disponível em: http://127.0.0.1:8000/docs#/

Nesta página, você encontrará os três endpoints implementados, conforme especificado na documentação.

A aplicação em questão recebe as informações de cadastro do usuário, após efetuar o login, gera um token. 
Logo acima, os dados retornam as informações dos servidores cadastrados via banco.

