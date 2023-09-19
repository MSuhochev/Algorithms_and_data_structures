""" 
- подсчёт количества элементов
- вывод всего дерева на экран
- удаление элементов
"""

class Node:
    """Класс Node который определяет вершины бинарного дерева"""

    # инициализатор класса в который передаются данные о вершинах
    def __init__(self, data):
        self.data = data
        # в каждой вершине есть указатели на левого и правого ребенка, по умолчанию принимают значение None
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        res = f'(значение нашего узла: {self.data})'
        if self.leftChild:
            res += f' (значение левого: {self.leftChild.data})'
        if self.rightChild:
            res += f' (значение правого: {self.rightChild.data})'
        return res


class BinaryTree:
    """класс BynaryTree - для работы с бинарным деревом"""

    # инициализатор класса
    def __init__(self):
        # по умолчанию корень дерева пустой
        self.root = None

    # метод поиска вершин для добавления новых значений в бинарное дерево
    def __find__(self, node, parent, value):
        # если узел имеет значение None
        if node is None:
            # возвращаем None, родительское значение, и флаг означающий, что вершину нужно добавить
            return None, parent, False
        # если добавляемое value равно значению хранящемуся в текущем узле добавлять нам его не нужно
        if value == node.data:
            # возвращаем этот узел, его родителя и флаг того - стоит ли добавлять вершину
            return node, parent, True
        # если добавляемое value меньше значения хранящегося в текущем узле мы идём по левой ветви
        if value < node.data:
            # если существует левый ребенок
            if node.leftChild:
                # продолжаем рекурсию вызываем метод find и передаём ему левого ребёнка, его родителя, и значение value
                return self.__find__(node.leftChild, node, value)
        # если добавляемое value больше значения хранящегося в текущем узле мы идём по правой ветви
        if value > node.data:
            # если существует правый ребенок
            if node.rightChild:
                # продолжаем рекурсию вызываем метод find и передаём ему правого ребёнка, его родителя, и значение value
                return self.__find__(node.rightChild, node, value)
        # при выполнении возвращаем узел для добавления value, родителя и флаг (False - означает что вершину нужно добавить)
        return node, parent, False

    # метод добавляющий новые вершины в бинарное дерево
    def add_value(self, value):
        # если корень None - значит в бинарном дереве нет ни одного объекта
        if self.root is None:
            # тогда наш корневой элемент становится добавляемым value
            self.root = value
            return value
        # метод который ищет возможный узел для добавления нового и возвращает узел к которому
        # можно добавить новый узел
        # его родителя
        # и флаг  False - такого узла не существует и его можно добавить и True - добавлять не нужно
        currNode, parentNode, flag_find = self.__find__(self.root, None, value.data)
        # если flag_find принимает значение False и currNode существует - тогда мы добавляем новую вершину
        if not flag_find and currNode:
            # если добавляемое значение меньше значения узла к которому мы добавляем
            if value.data < currNode.data:
                # тогда добавляемое значение становится левым ребенком
                currNode.leftChild = value
            else:
                # иначе добавляемое значение становится правым ребенком
                currNode.rightChild = value
        # возвращаем добавляемое значение
        return value
    
    # метод подсчёта количества элементов бинарного дерева
    def count_tree(self, node):
        # если передаваемый node пуст
        if node is None:
            # возвращаем 0 - дерево пустое
            return 0
        # иначе рекурсивно подсчитываем количество элементов
        return self.count_tree(node.leftChild) + 1 + self.count_tree(node.rightChild)

    # метод отображающий бинарное дерево (обход в глубину)
    def show_tree(self, node):
        # если узел принимаемый на вход имеет значение None - отображать нечего и мы выходим из функции
        if node is None:
            return
        # рекурсивно вызываем метод и проходим по левой его части
        self.show_tree(node.leftChild)
        # отображаем текущую вершину
        print(node.data)
        # идём по правой части (отображаться будет по возрастанию, если первым поставим обход с правой части
        # отображаться будет по убыванию)
        self.show_tree(node.rightChild)

    # метод отображающий бинарное дерево (обход в ширину)
    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.leftChild:
                    vn += [x.leftChild]
                if x.rightChild:
                    vn += [x.rightChild]
            print()
            v = vn

    # метод удаления листа (узел без детей)
    def __del_leaf(self, delNode, parentNode):
        # если удаляемый узел является левым ребёнком родительского узла
        if parentNode.leftChild == delNode:
            # разрываем связь с ним передавая значению левого ребёнка родительского узла значение None
            parentNode.leftChild = None
        # либо удаляемый узел является правым ребёнком родительского узла
        elif parentNode.rightChild == delNode:
            # разрываем связь с ним передавая значению правого ребёнка родительского узла значение None
            parentNode.rightChild = None

    # метод удаления узла с одним ребенком
    def __del_one_child(self, delNode, parentNode):
        # если удаляемый узел является левым ребенком родительского узла
        if parentNode.leftChild == delNode:
            # если у удаляемого узла отсутствует левый ребёнок
            if delNode.leftChild is None:
                # правый ребёнок удаляемого узла становится левым ребёнком родительского
                parentNode.leftChild = delNode.rightChild
            # если же у удаляемого узла отсутствует правый ребёнок
            elif delNode.rightChild is None:
                #  левый ребёнок удаляемого узла становится левым ребёнком родительского
                parentNode.leftChild = delNode.leftChild
        # если удаляемый узел является правым ребенком родительского узла        
        elif parentNode.rightChild == delNode:
            # если у удаляемого узла отсутствует левый ребёнок
            if delNode.leftChild is None:
                # правый ребёнок удаляемого узла становится правым ребёнком родительского
                parentNode.rightChild = delNode.rightChild
            # если же у удаляемого узла отсутствует правый ребёнок   
            elif delNode.rightChild is None:
                # левый ребёнок удаляемого узла становится правым ребёнком родительского
                parentNode.rightChild = delNode.leftChild

    # метод поиска минимального значения в поддереве
    def __find_min(self, node, parent):
        # если существует левый ребенок
        if node.leftChild:
            # рекурсивно вызываем поиск наименьшего значения
            return self.__find_min(node.left, node)
        # если нет то возвращаем узел и его родителя
        return node, parent

    # метод для удаления элементов бинарного дерева (передаем в него удаляемое значение - key)
    def del_node(self, key):
        # метод который ищет узел для удаления и возвращает узел к которому
        # можно добавить новый узел
        # его родителя
        # и флаг  False - такого узла не существует и удалять нечего и True - можем удалить искомый узел
        delNode, parentNode, flag_find = self.__find__(self.root, None, key)
        # если узел не найден (flag_find = False)
        if not flag_find:
            # возвращаем None
            return None
        # если у удаляемого узла отсутствуют левый и правый ребенок
        if delNode.leftChild is None and delNode.rightChild is None:
            # вызываем метод удаления листа
            self.__del_leaf(delNode, parentNode)
        # либо у удаляемого узла есть левый или правый ребенок
        elif delNode.leftChild is None or delNode.rightChild is None:
            # вызываем метод удаления узла с одним ребенком
            self.__del_one_child(delNode, parentNode)
        # если узел имеет двух детей
        else:
            # находим минимальное значение поддерева
            minCurrNode, parentMinNode = self.__find_min(delNode.rightChild, delNode)
            # удаляемому узлу присваиваем значение минимального
            delNode.data = minCurrNode.data
            # и удаляем узел
            self.__del_one_child(minCurrNode, parentMinNode)

val = [12, 8, 9, 17, 7, 4, 22]

bt = BinaryTree()
for i in val:
    bt.add_value(Node(i))

bt.del_node(7)
print(bt.root)
bt.show_tree(bt.root)
print("-------------------")
bt.show_wide_tree(bt.root)
print(bt.count_tree(bt.root))


