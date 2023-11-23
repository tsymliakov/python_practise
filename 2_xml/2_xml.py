import xml.etree.ElementTree as ETree


def get_parent(node: ETree.Element, xml_tree: ETree.ElementTree) -> ETree.Element | None:
    """
    4.6.1 находит родителя узла и возвращает его.

    Кажется, я посмотрел весь исходный код класса Element, но так и не нашел
    способа найти родителя указанного элемента без доступа к XML-дереву. Поэтому
    я решу задание с условием передачи дерева в качестве аргумента, а затем учту
    свою ошибку во время просмотра эталонного решения.
    """
    parents_map = {child: parent for parent in xml_tree.iter()
                   for child in parent}

    parent = parents_map.get(node)
    return parent


def delete_nodes_via_tag(tag: str, xml_tree: ETree.ElementTree) -> None:
    """
    4.6.1 требуется удалить все узлы, совпадающие по тегу, вместе с их
    поддеревьями.

    Хоть функций и работает, но возникает небольшая проблема с удалением
    корневого элемента. Стандартная библиотека не слишком хочет работать с XML
    деревом, у которого корневой элемент равен None.

    В библиотеке даже есть закомменченный asssert:
        # assert element is None or iselement(element)
    """

    targeted_nodes = [i for i in xml_tree.iter() if i.tag == tag]
    parents_map = {child: parent for parent in xml_tree.iter()
                   for child in parent}

    for node in targeted_nodes:
        parent = parents_map.get(node)

        if not parent:
            xml_tree._setroot(None)
            return

        parent.remove(node)
