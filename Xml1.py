import xml.etree.ElementTree as xml

def createXML(filename):
    root = xml.Element("users")
    children1 = xml.Element("user")
    root.append(children1)

    userId1 = xml.SubElement(children1, "id")
    userId1.text = "123"
    userName1 = xml.SubElement(children1, "name")
    userName1.text = "Shubham"

    tree = xml.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)
    fh.close()


createXML("test.xml")
