---

# Catálogo de Filmes

Bem-vindo ao **Catálogo de Filmes**! Este é um projeto desenvolvido em **Django** para exibir uma lista de filmes, com informações como título, descrição, ano de lançamento e imagem.

## 📖 Descrição

O **Catálogo de Filmes** permite aos usuários visualizar um catálogo de filmes com suas informações detalhadas, incluindo imagens. O sistema também permite o cadastro de filmes através do painel administrativo do Django. O projeto utiliza o banco de dados **PostgreSQL** e está estruturado para ser fácil de estender e personalizar.

## 🛠 Tecnologias Usadas

- **Django**: Framework web em Python.
- **PostgreSQL**: Banco de dados relacional.
- **HTML/CSS**: Para o front-end.
- **Bootstrap/Tailwind** (opcional): Para a estilização (pode ser integrado facilmente). Contudo, não utilizado ainda nesse repositório.

## 🚀 Funcionalidades

- Visualização da lista de filmes.
- Cadastro de filmes no painel de administração.
- Filtro por título e ano de lançamento.
- Estilização básica com CSS.

## 📂 Estrutura do Projeto

```
catalogo_filmes/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── filmes/
│   │   │   ├── base.html      <-- Template base
│   │   │   └── lista.html     <-- Página de lista de filmes
│   ├── static/
│   │   └── filmes/
│   │       └── css/estilo.css
├── media/
│   └── filmes/
│       └── imagem1.jpg (etc)
```

## 🏃‍♂️ Como Rodar o Projeto

### 1. Clonar o repositório

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/catalogo-filmes.git
cd catalogo-filmes
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

Se você estiver utilizando um ambiente virtual (virtualenv), crie e ative o ambiente:

```bash
python -m venv venv
# No linux, `use source venv/bin/activate`
# No Windows, use `venv\Scripts\activate`
```

### 3. Instalar as dependências

Instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados PostgreSQL

Se estiver utilizando o PostgreSQL, edite o arquivo `settings.py` para incluir as configurações do seu banco de dados:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Rodar as migrações

Aplique as migrações para criar as tabelas do banco de dados:

```bash
python manage.py migrate
python manage.py make migrations
```

### 6. Criar um superusuário

Crie um superusuário para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

### 7. Rodar o servidor

Agora, inicie o servidor local:

```bash
python manage.py runserver
```

Você pode acessar a aplicação no navegador em:

```
http://127.0.0.1:8000/
```

E acessar o painel administrativo em:

```
http://127.0.0.1:8000/admin/
```

## 💡 Como Contribuir

1. Faça um **fork** deste repositório.
2. Crie uma **branch** para a sua feature ou correção (`git checkout -b feature/nova-feature`).
3. **Commit** suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. **Push** para a branch (`git push origin feature/nova-feature`).
5. Abra um **pull request**.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.

---

**Dúvidas?**  
Entre em contato através de (antonio980felixmedeiros@gmail.com).

---
