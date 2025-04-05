import xml.etree.ElementTree as ET

def write_hhc_node(node, f, indent=4):
    spacer = ' ' * indent
    title = node.attrib.get("title", "Unbenannt")
    link = node.attrib.get("link", "")

    f.write(spacer + "<LI> <OBJECT type='text/sitemap'>\n")
    f.write(spacer + "  <param name='Name' value='"  + title + "'>\n")
    f.write(spacer + "  <param name='Local' value='" + link  + "'>\n")
    f.write(spacer + "</OBJECT>\n")

    children = list(node)
    if children:
        f.write(spacer + "<UL>\n")
        for child in children:
            write_hhc_node(child, f, indent + 2)
        f.write(spacer + "</UL>\n")

    f.write(spacer + "</LI>\n")

def generate_hhc_from_xml(xml_file, hhc_output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(hhc_output_file, 'w') as f:
        f.write('<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">\n')
        f.write('<HTML>\n<HEAD>\n')
        f.write('<meta name="GENERATOR" content="Python XML TOC Generator">\n')
        f.write('</HEAD>\n<BODY>\n')
        f.write('<OBJECT type="text/site properties">\n')
        f.write('  <param name="ImageType" value="Folder">\n')
        f.write('</OBJECT>\n\n')
        f.write('<UL>\n')

        for topic in root.findall("topic"):
            write_hhc_node(topic, f, indent=2)

        f.write('</UL>\n</BODY>\n</HTML>\n')

# --- Hauptprogramm ---

xml_input = 'toc.xml'
hhc_output = 'toc.hhc'

generate_hhc_from_xml(xml_input, hhc_output)

print(hhc_output + " wurde erfolgreich aus: " + xml_input + " erstellt.")
