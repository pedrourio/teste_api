# Teste técnico Livon - BACKEND 

API RESTful para um sistema de gerenciamento de conteúdo, permitindo operações de CRUD (Criar, Ler, Atualizar, Deletar) para posts, além de um sistema de favoritos.

## Stack Tecnológica

- **Backend:** Python, Django, Django REST Framework
- **Banco de Dados:** PostgreSQL
- **Containerização:** Docker, Docker Compose

## Instalação e Execução

Será feita utilizando Docker.

1.  **Build e Run dos Contêineres:**
    O comando a seguir irá construir as imagens Docker, iniciar os serviços (API e banco de dados) e executar as migrações iniciais.

    ```bash
    docker compose up --build
    ```

2.  **Acesso à Aplicação:**
    Após a execução, a API estará disponível em [http://localhost:8000](http://localhost:8000).

-   **Backend (API):** `http://127.0.0.1:8000`
-   **Banco de Dados (PostgreSQL):** A API se conecta automaticamente ao banco de dados `postgres` no container de serviço `db`.

## Endpoints Principais

-   `/api/token/`: Autenticação de usuários para obtenção de token.
-   `/api/posts/`: CRUD de Posts.
-   `/api/posts/{id}`: Requisição de um post específico.
-   `/api/posts/{id}/favorite/`: Adicionar/Remover um post dos favoritos.
-   `/api/users/`: Listagem e criação de usuários.

## Permissões

O sistema de permissões é baseado no tipo de usuário:

-   **Leitor (Usuário não autenticado ou sem permissão de escrita):**
    -   Pode visualizar todos os posts (Leitura).
-   **Autor (Usuário autenticado, dono do post):**
    -   Pode criar, ler, atualizar e deletar seus próprios posts (CRUD completo).
-   **Admin (Superusuário):**
    -   Possui acesso total a todos os posts e funcionalidades administrativas.

A lógica de permissão está implementada em `teste_api/permissions.py` na classe `IsOwnerOrReadOnly`, garantindo que apenas o dono de um post ou um administrador possa modificá-lo.

## Como Testar as Funcionalidades

### Testes Manuais (Admin)

 **Django Admin:**
    Acesse a interface administrativa em [http://127.0.0.1:8000/](http://127.0.0.1:8000/) e utilize as credenciais de um superusuário para gerenciar os dados diretamente.

## Credenciais para Teste

Você pode criar um superusuário para testes com o comando:

```bash
docker compose exec web python manage.py createsuperuser
```

Ou para um usuário comum:
1. Abra o shell do Django:
    `sudo docker compose exec web python manage.py shell`
2. Cole este código:
    ```
    from django.contrib.auth.models import User

    if not User.objects.filter(username='user').exists():
        User.objects.create_superuser('user', 'user@teste.com', 'user123@')


    exit()

    ```

3. Acesse com o usuário "user" e a senha "user123@"