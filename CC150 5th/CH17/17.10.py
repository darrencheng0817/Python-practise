# Since XML is very verbose, you are given a way of encoding it where each tag gets mapped to a pre-defined integer value. The language/grammar is as follows:
# Element --> Element Attr* END Element END [aka, encode the element tag, then its attributes, then tack on an END character, then encode its children, then another end tag]
# Attr --> Tag Value [assume all values are strings] END --> 01
# Tag --> some predefined mapping to int
# Value --> string value END
# Write code to print the encoded version of an xml element (passed in as string).
# FOLLOW UP
# Is there anything else you could do to (in many cases) compress this even further?


from xml.dom import minidom

hash_map = {"family": 1, "person": 2, "firstname": 3, "lastname": 4, "state": 5}

xmldoc = minidom.parse('17.10.xml')
root = xmldoc.getroot()
print root.find('family')
#for neighbor in root:
  #print neighbor.attrib
  
#itemlist = xmldoc.getElementsByTagName('family')


# print(len(itemlist))
# print(itemlist[0].attributes['name'].value)
#for s in itemlist:
    #print(s.attributes['name'].value)


