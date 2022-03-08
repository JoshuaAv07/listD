from linked_list import DoublyLinkedList


if __name__ == '__main__':
    t = ""
    my_list = DoublyLinkedList()

    print(f'List Size = {my_list.size()}')
    print(f'If list is empty =  {my_list.empty()}')
    print(t.center(50,'-'))
    my_list.append("Joshua")

    print(f'List Front = {my_list.front()}')
    print(f'List Back = {my_list.back()}')
    print(f'List Size = {my_list.size()}')
    print(f'If list is empty =  {my_list.empty()}')
    print(t.center(50,'-'))

    my_list.append("Gustavo")
    my_list.append("Derek")
    my_list.append("Fabian")
    my_list.append("Fabian")
    my_list.append("David")
    my_list.append("Omar")
    my_list.append("Luis")
    my_list.append("Kevin")
    my_list.append("Jonathan")

    print(f'List Front = {my_list.front()}')
    print(f'List Back = {my_list.back()}')
    print(f'List Size = {my_list.size()}')
    print(f'If list is empty =  {my_list.empty()}')
    print(t.center(50,'-'))

    for name in my_list.iter():
        print(name)

    print(my_list.delete("Fabian"))

    print(t.center(50,'-'))

    for name in my_list.iter():
        print(name)

    print(t.center(50,'-'))
    if my_list.search("Fabian"):
        element = my_list.search("Fabian")
        print(f'{element.data} exist in the list')
    else:
        print(False)

    print(t.center(50,'-'))   

    my_list.insert("Alex", "David")

    for name in my_list.iter():
        print(name)
