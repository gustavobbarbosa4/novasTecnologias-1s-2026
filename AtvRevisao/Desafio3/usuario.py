class Usuario:
    def __init__(self, id, nome, email):
        self.__id = id
        self.__nome = nome
        self.__email = email

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("E-mail inválido")

    def __str__(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, Email: {self.__email}"