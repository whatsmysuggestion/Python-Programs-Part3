import xml.etree.ElementTree as xml

def updateXML(filename):
    tree = xml.ElementTree(file=filename)
    root = tree.getroot()
    for salary in root.iter("id"):
        salary.text = '1000'

    tree = xml.ElementTree(root)
    with open("updated_test.xml", "wb") as fh:
        tree.write(fh)
    fh.close()
updateXML("test.xml")
