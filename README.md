Fala pessoal!

Estou compartilhando um projeto que desenvolvi de uma API bancária. Inicialmente, ele foi proposto em um bootcamp da DIO, mas como todo desafio, resolvi ir além e fazer algumas melhorias.

A proposta original era bem simples: criar contas, listar contas e realizar transações, utilizando banco core. Mas decidi evoluir o projeto utilizando ORM, que na minha visão facilita bastante o manuseio por trabalhar com objetos Python. A partir disso, implementei novas funcionalidades como criação de usuário, login e autenticação com JWT.

A API simula um ambiente bancário básico com controle por usuário. Cada usuário possui suas próprias contas, e cada conta tem suas transações. Todas as rotas sensíveis estão protegidas com autenticação JWT.

O fluxo funciona da seguinte forma: o usuário se registra, realiza o login, recebe um token e passa a utilizá-lo nas rotas protegidas via header.

Sobre a estrutura do projeto:

controllers
services
models
schemas
config
database
security

Usei dois tipos de banco de dados: SQLite para desenvolvimento local e PostgreSQL em produção.

Aqui estão os comandos para executar o projeto localmente:

poetry install
poetry run uvicorn main:app --reload

Lembrando de instalar as dependências corretamente antes de rodar o projeto.

Durante o desenvolvimento, identifiquei alguns pontos em que adquiri uma melhoria, principalmente na organização das camadas do projeto, na relação entre funções e tabelas e também no aprofundamento do uso do JWT.

Esse projeto foi muito importante para consolidar conceitos e evoluir na prática como desenvolvedor backend.

depoloy do projeto (para teste): https://api-bank-system.onrender.com/docs