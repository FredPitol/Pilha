# -*- coding: utf-8 -*-

from array_stack import ArrayStack  # array_stack.py eh o nome do arquivo(modulo) e ArrayStack eh a classe
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import ListNode
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator
from array_queue_new import ArrayQueue

class PilhaComLista:


#> Método construtor
    def __init__(self): 
        self._pilha = SinglyLinkedListIterator() 

#> Retorna tamanho da pilha            
    def len(self):
        return self._pilha.size
    
#> Verifica se pilha está vazia, retorno binário
    def is_empty(self):
        return (self._pilha.size == 0)
    
#> Adiciona um novo elemento a pilha, iterador fica em cima do novo elemento devido ao método addNode
    def push(self, e): 
        self._pilha.last_Node()
        self._pilha.addNode(e) 

#> Coloca o iterador no ultimo nó da lista(Topo da lista), retorna lista
    def top(self):  
        if(self._pilha.size == 0):
            print('pilha vazia')
            return None
        else:
            self._pilha.last_Node()
            return self._pilha.iterator.data

#> Retira o elemento do topo da lista, retorna o elemento
    def pop(self):
        if (self._pilha.size == 0):  # pilha Vazia
            print('pilha vazia')
            return None
        else:
            self._pilha.last_Node 
            topo = self._pilha.iterator.data 
            self._pilha.elimNode() 
            self._pilha.lastNode 
            return topo 

#> Printa pilha
    def printPilha(self):
        self._pilha.first_Node()  
        # Enquanto o iterador não enstiver indefinido
        while not self._pilha.isUndefinedIterator():
            print(self._pilha.iterator.data, end=" ")
            self._pilha.nextNode()  # avanca iterador para proximo noh
        print('\n')


if __name__ == "__main__":
    print("\n========== Inicio do programa ==========\n")

    print(" 1) Inverter uma lista utilizando como apoio uma pilha")


    print("\n==============================\n")

    print(" 2) Fazer uma cópia de uma pilha, usando como apoio uma lista. Também é possível usar como apoio uma pilha. A pilha original deve ser restaurada")


    print("\n==============================\n")

    print(" 3) Inverter uma pilha utilizando como apoio uma lista")


    print("\n==============================\n")

    print(" 4) Dizer se duas pilhas são iguais sem destruir seu conteúdo. ")


    print("\n==============================\n")

    print(" 5) Adicionar um elemento no fundo da pilha")


    print("\n==============================\n")

    print(" 6) ")


    print("\n============ Fim do programa ==================\n")