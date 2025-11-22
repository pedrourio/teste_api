# DOCKER
1. Construa as imagens Docker:
	`docker-compose build`
	
2. Suba os contêineres:"
	`docker compose up -d`
	
3. Execute as migrações do Django (crie o banco de dados e tabelas):" 
	`docker compose exec web python manage.py migrate`
    
4. (Opcional) Crie um superusuário:"
	`docker compose exec web python manage.py createsuperuser`
	ou
    `docker compose exec web python manage.py createsuperuser --username admin --email admin@example.com`
                                                                                   
Sua aplicação estará disponível em http://localhost:8000" 

## Caso seja necessário resetar o docker
* Derruba os containers e apaga os volumes (o banco antigo)
    `sudo docker compose down -v`

* Sobe tudo de novo com a versão nova
    `sudo docker compose up -d --build`

* Tenta rodar a migração novamente
    `sudo docker compose exec web python manage.py migrate`
    
## Caso eu acho que misturei docker-compose e docker compose
* 1. Derruba tudo feito pelo comando antigo
    `sudo docker compose-down`

* 2. Derruba tudo feito pelo comando novo
    `sudo docker compose down`

* 3. Sobe limpo usando APENAS o novo
    `sudo docker compose up -d --build`
    
    
## Comandos do Python no docker
* Rodar migrações	
    * `sudo docker compose exec web python manage.py migrate`
* Criar superusuário
    * `sudo docker compose exec web python manage.py createsuperuser`
* Abrir o shell	
    * `sudo docker compose exec web python manage.py shell`
* Rodar testes	
    * `sudo docker compose exec web python manage.py test`

# SERIALIZER
* Dentro do teste_livon_api/serializer.py vou criar simplificações entre o back e o front
* Criado serializer para os usuários com: "url", "username", "email", "password" "groups"
* criado serializer para os grupos com: "url", "name"
__Lembrar de criar serializers para os posts__ 

# VIEWS
* O arquivo de views.py recebeu ViewSets referentes aos usuários e aos grupos
* Aqui declararei meus endpoints para serem chamados no front

# AUTENTICAÇÃO
## permissions.py
```
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        // Qualquer um pode ver
        if request.method in permissions.SAFE_METHODS:
            return True

        // Somente o dono ou o admin podem editar.
        return obj.owner == request.user or request.user.is_staff
```

# PARA CRIAR USUÁRIO ADMIN
1. Abra o shell do Django:
    `sudo docker compose exec web python manage.py shell`
2. Cole este código:
```
from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@teste.com', '123123')


exit()
```

3. Utilize os usuários
    1. ADMINISTRADOR: 
        * username: admin
        * senha: 123123
    2. USUÁRIO SEM CADASTRO:
        * _não faça login_
