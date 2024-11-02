class Usuario:
    def __init__(self,id, nome, senha):
        self.id= id
        self.nome = nome
        self.senha = senha

lista_usuarios=[]
user= Usuario(2, "igor", "1234")
admin= Usuario(1, "admin", "admin")
lista_usuarios.append(user)
lista_usuarios.append(admin)
