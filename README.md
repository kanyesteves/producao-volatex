# Produção Volatex - Documentação

## Introdução

#### Descrição Geral:
Este sistema foi desenvolvido para efetuar o controle e a gestão de produção para malharias.

#### Objetivo da documentação:
Está documentação foi pensada naquele programador que já contém alguns conhecimentos e experiências em desenvolvimento de sistemas no geral.

## Requisitos prévios

#### Dependências:
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/docs/getting_started/index.html)
- [Plotly](https://plotly.com/python/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [SQLite3](https://www.sqlite.org/docs.html)


## Docker
Build iamgem e subir os containers:
```
docker compose up -d
```
Após iniciado é necessário copiar o JSON esperado do projeto Firebase:
```
docker cp <PATH>/db-firestore-volatex-firebase-adminsdk.json web:/app/
```
