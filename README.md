# Project TheBus

    Aplicação web de localização e rotas do trasporte público de Teresina-PI

## Demonstração http://thebus.herokuapp.com/ Faça uma visita

## Features
    Localização de ônibus e desenho de rotas

## How to Use
    # Dados de autenticação nas conficurações
    thebus/settings.py
    API_STRANS = "api key"
    EMAIL = ""
    PASS = ""

    # Criar banco de dados
    python manage.py migrate core

    # Semear o autocomplete
    python seeds/lines.py

    # criar tabela de cache
    python manage.py createcachetable

# !!!!!!!!!!!!!!!!!!Atenção!!!!!!!!!!!!!!!!!!!!
    Projeto com layout otimizado para deploy no http://heroku.com/


