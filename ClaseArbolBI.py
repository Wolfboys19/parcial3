#Definimos la clase para arboles binarios
#Adair Vargas
from ClaseNodoArbol import Node
class BinarySearchTree:
    def __init__(self):
        self.root=None

    def empty(self):
        if self.root is None:
            return True
        return False

#Definimos el metodos para insertar nodos
    def insert(self,label):
        new_node=Node(label,None)
        if self.empty():
            self.root=new_node
        else:
            curr_node=self.root
            while curr_node is not None:
                parent_node=curr_node
                if new_node.getLabel()<curr_node.getLabel():
                    curr_node=curr_node.getLeft()
                else:
                    curr_node=curr_node.getRight()
            if new_node.getLabel()<parent_node.getLabel():
                parent_node.setLeft(new_node)
            else: parent_node.setRight(new_node)
            new_node.setParent(parent_node)

#Definimos un recorrido para imprimir mi arbol
    def __InOrderTraversal(self,curr_node):
        nodeList=[]
        if curr_node is not None:
            nodeList.insert(0,curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

#Imprimir el arbol
    def __str__(self):
        list=self.__InOrderTraversal(self.root)
        str=""
        for x in list:
            str=str +" "+ x.getLabel().__str__()
        return str
