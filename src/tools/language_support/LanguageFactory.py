from tools.language_support.Cpp import Cpp11, Cpp17
from tools.language_support.Paitom import Paitom
from tools.language_support.C import C

class LanguageFactory:
    def __init__(self, st: str):
        self.st = st.lower()

    def create(self):
        if self.st == "cpp11":
            return  Cpp11()
        elif self.st == "cpp17":
            return  Cpp17()
        elif self.st == "py":
            return Paitom()
        elif self.st == "c":
            return C()
        else:
            return None
