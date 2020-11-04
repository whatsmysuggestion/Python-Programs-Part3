import xml.dom.minidom

def main():

    doc = xml.dom.minidom.parse("Output.xml")

    print (doc.firstChild.tagName)
    expertise = doc.getElementsByTagName("student")
    print( expertise.length)
    for skill in expertise:
        print(skill.getAttribute("name"))
    print("----------------------------------------")

    newexpertise = doc.createElement("student")
    newexpertise.setAttribute("name", "BigData")
    doc.firstChild.appendChild(newexpertise)

    expertise = doc.getElementsByTagName("student")
    print(expertise.length)
    for skill in expertise:
        print(skill.getAttribute("name"))


main()