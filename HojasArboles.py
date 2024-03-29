from __future__ import print_function


# Declaramos la clase "Node"
class Node:

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        self.parent = parent

        # Métodos para asignar nodos

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def esHoja(self):
        return not (self.left or self.getRight)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        # Creamos un nuevo nodo
        new_node = Node(label, None)
        # Si el árbol esta vacio
        if self.empty():
            self.root = new_node
        else:
            # Si el árbol no esta vacio
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)

            # Operación de borrado

    def delete(self, label):
        if (not self.empty()):
            node = self.getNode(label)
            if (node is not None):
                if (node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                elif (node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                elif (node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                else:
                    tmpNode = self.getMax(node.getLeft())
                    self.delete(tmpNode.getLabel())
                    node.setLabel(tmpNode.getLabel())

    def getNode(self, label):
        curr_node = None
        if (not self.empty()):
            curr_node = self.getRoot()
            while curr_node is not None and curr_node.getLabel() is not label:
                if label < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
        return curr_node

    def getMax(self, root=None):
        if (root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if (not self.empty()):
            while (curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root=None):
        if (root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if (not self.empty()):
            curr_node = self.getRoot()
            while (curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        contador = 0
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
            if curr_node.getLeft() is None and curr_node.getRight() is None:
                contador +=1
            print(str(contador))
        return nodeList

    def getRoot(self):
        return self.root

    def __isRightChildren(self, node):
        if (node == node.getParent().getRight()):
            return True
        return False

    def __reassignNodes(self, node, newChildren):
        if (newChildren is not None):
            newChildren.setParent(node.getParent())
        if (node.getParent() is not None):
            if (self.__isRightChildren(node)):
                node.getParent().setRight(newChildren)
            else:
                node.getParent().setLeft(newChildren)

    def traversalTree(self, traversalFunction=None, root=None):
        if (traversalFunction is None):
            return self.__InOrderTraversal(self.root)
        else:
            return traversalFunction(self.root)

    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str



def InPreOrder(curr_node):
    nodeList = []
    nodosmayores = []
    numdado = 6
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(curr_node.getLeft())
        if curr_node.getLabel() > numdado:
            nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + InPreOrder(curr_node.getRight())
        #print('este es el getñabel',curr_node.getLabel)

        #for i in range(len(nodeList)):
          #  if nodeList[i] > numdado:
           #     nodosmayores.append(nodeList[i])
        #return nodosmayores



    return nodeList



def contarHojas(curr_node):

    contador = 0
    if curr_node is not None:
        #print('Nodo actual: ', curr_node)

        if curr_node.getRight() == None and curr_node.getLeft() ==  None:
            contador -=- 1
        #print('Evaluando nodo izquierdo: ', curr_node.getLeft())
        contador +=  contarHojas(curr_node.getLeft())
        #print('Evaluando nodo derecho: ', curr_node.getRight())
        contador +=  contarHojas(curr_node.getLeft())


    return contador






#def numHojas(curr_node):
 #   contador = 0
  #  if curr_node.getLeft() is None and curr_node.getRight() is None:
   #     contador +=1
    #contador += 0 if curr_node.getRight is None else curr_node.getRight.numHojas()
    #contador += 0 if curr_node.getLeft is None else curr_node.getLeft.numHojas()

    #return contador

# Función para probar las clases
def testBinarySearchTree():
    '''
    Ejemplo
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
    '''

    '''
    Ejemplo luego del borrado
                  7
                 / \
                1   4
    '''
    # Instancia del árbol binario de búsqueda
    t = BinarySearchTree()
    # Insertamos los elementos
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)


    print(t.__str__())

    if (t.getNode(6) is not None):
        print("El elemento 6 existe")
    else:
        print("El elemento 6 no existe")

    if (t.getNode(-1) is not None):
        print("El elemento -1 existe")
    else:
        print("El elemento -1 no existe")

    if (not t.empty()):
        print(("Valor Max: ", t.getMax().getLabel()))
        print(("Valor Min: ", t.getMin().getLabel()))



    t.delete(13)
    t.delete(10)
    t.delete(8)
    t.delete(3)
    t.delete(6)
    t.delete(14)

    # Obtenemos todos los elementos del árbol en preorden
    list = t.traversalTree(InPreOrder, t.root)
    for x in list:
        print(x)




def main():
    t = BinarySearchTree()
    # Insertamos los elementos
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)
    print(f'El numero de Hojas en el arbol de busqueda es de: {t.traversalTree(contarHojas,t.root)}')
    print(f'Los nodos mallores al numero dado son: {t.traversalTree(InPreOrder,t.root)}')
    #list = t.traversalTree(InPreOrder, t.root)
    #lista = t.traversalTree(contarHojas, t.root)



    #for x in list:
     #   print(x)
    #print('lol',list)

if __name__ == "__main__":
    #testBinarySearchTree()
    main()
