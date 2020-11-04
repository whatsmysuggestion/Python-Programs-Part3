import xml.etree.ElementTree as xml

def createXML(filename):
    root = xml.Element("users")
    children1 = xml.Element("user")
    root.append(children1)

    tree = xml.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)
    fh.close()

createXML("test1.xml")
