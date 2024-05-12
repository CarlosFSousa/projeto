def ordenar_por_insercao(resultados):
    if resultados.head is None:
        return
    
    sorted_list = LinkedList()
    sorted_list.append(resultados.head.data)
    current_node = resultados.head.next

    while current_node:
        insert_before = None
        node_to_insert_after = sorted_list.head
        while node_to_insert_after:
            if current_node.data.cidade < node_to_insert_after.data.cidade:
                break
            insert_before = node_to_insert_after
            node_to_insert_after = node_to_insert_after.next

        new_node = Node(current_node.data)
        if insert_before is None:
            new_node.next = sorted_list.head
            sorted_list.head = new_node
        else:
            new_node.next = insert_before.next
            insert_before.next = new_node

        current_node = current_node.next

    return sorted_list

def ordenar_bubblesort(destinos):
    n = len(destinos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if destinos[j].designacao > destinos[j + 1].designacao:
                destinos[j], destinos[j + 1] = destinos[j + 1], destinos[j]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next