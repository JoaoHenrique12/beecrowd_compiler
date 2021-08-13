import sys
import os
from tools.language_support.LanguageFactory import LanguageFactory

class Manager:

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self,value):
        self._path = value

    def __init__(self):
        self.path = os.getcwd()
        self.command = None

    def identify(self,command: list):
        try:
            if command[0].lower() == "create":
                self.create(command[1:])
            else:
                print("Comando invalido")
                sys.exit(1)
        except IndexError:
            print("Sem argumentos recebidos\nVerifique a sessao de ajuda")
            sys.exit(1)

    def create(self,command: list):
        question_number = ""
        language = ""

        for g in range(len(command) - 1):
            if command[g] == "-id":
                question_number = command[g+1]
            elif command[g] == "-language":
                language = command[g+1]

        self.path = os.path.join(self.path,question_number)
        os.mkdir(self.path)
        os.chdir(self.path)
        
        language_obj = LanguageFactory(language)
        language_obj = language_obj.create()
        language_obj.create_file()
        
