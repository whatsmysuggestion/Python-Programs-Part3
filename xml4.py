import xml.etree.ElementTree as xml


def dummy(file_name):
    tt = xml.ElementTree(file=file_name)
    print(tt.getroot())
    root = tt.getroot()
    print("tag=%s, attrib=%s" % (root.tag, root.attrib))
    print("-" * 40)
    users = root.getchildren()
    for user in users:
        user_children =user.getchildren()
        for user_child in user_children:
            print("%s=%s" % (user_child.tag, user_child.text))

dummy("test.xml")
