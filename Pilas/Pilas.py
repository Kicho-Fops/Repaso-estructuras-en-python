import Listas_Ligadas as ll



from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Pilas(Generic[T]):
    
    def __init__(self):
        self.lista = ll.ListaLigada()
        self.sais = 0 #Size/Tamaño pero debo de hacer mis pendejadas
    
    def empty(self) -> bool:
        return self.lista.get_first_node() is None
    
    def pop(self) -> Optional[T]:
        if self.empty():
            return None
        last_node = self.lista.get_last_node()
        if self.sais > 0:
            self.lista.removeAt(self.sais - 1)
            self.sais -= 1
        return last_node.get_info() if last_node else None

    def push(self, data: T) -> None:
        self.lista.insertar(data)
        self.sais += 1
        
    def stacktop(self) -> Optional[T]:
        if self.lista.get_first_node() is None:
            return None
        return self.lista.get_last_node().get_info()
    
    
def is_palindrome(word: str) -> bool: #No es la solucion optima

    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    

    stack = Pilas[str]()
    
    for char in cleaned_word:
        stack.push(char)
    

    reversed_word = ''
    while not stack.empty():
        reversed_word += stack.pop()
    

    return cleaned_word == reversed_word

# Example usage
words = ["Racecar", "Python", "Madam", "Hello", "A man, a plan, a canal, Panama"]

is_palindromes = [is_palindrome(word) for word in words]
print(is_palindromes)  # Output: [True, False, True, False, True]