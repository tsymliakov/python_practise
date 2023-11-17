import xml.etree.ElementTree as ETree


xml1 = ETree.parse("2_xml/demo.xml")
root = xml1.getroot()


def recursive_node_print(root: ETree.ElementTree, tabs_number: int):
    for element in root:
        print("\t" * tabs_number + element.tag)
        attributes = " ".join([f"{attr} = {element.get(attr)}" for attr in element.attrib])
        if attributes:
            print("\t" * tabs_number + "  " + attributes)
        if element.text != "\n    ":  # Грязный хак
            print("\t" * tabs_number + "  " + str(element.text))
        recursive_node_print(element, tabs_number + 1)


def print_all_xml_nodes(root):
    """
    Задание 3.4.1 нужно вывести в консоль содержимое всех узлов XML,
    название тега, а также список атрибутов- их имена и значения
    """
    recursive_node_print(root, tabs_number=0)


def recursive_get_count(root: ETree.ElementTree, attribute):
    """
    Задание 3.4.2 нужно с помощью рекурсивной функции посчитать количество
    элементов, содержащих конкретный аттрибут
    """
    count = 0

    for element in root:
        if attribute in element.attrib:
            count += 1
        count += recursive_get_count(element, attribute)

    return count
