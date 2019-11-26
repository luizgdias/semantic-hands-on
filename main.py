from owlready2 import *

# Para o correto funcionamento deste script, deve existir um arquivo ontologia-prov.owl vazio no diretório /ontologia


onto = get_ontology('ontologia/ontologia-prov.owl').load()

with onto:
    class Entity(Thing):
        namespace = onto

    class Agent(Thing):
        namespace = onto

    class Activity(Thing):
        namespace = onto
    
    onto.save(file = "ontologia/ontologia-prov.owl")
    
    class Metadata(Entity):
        pass
    
    class wasDerivedFrom(ObjectProperty):
        domain   = [Entity]
        range    = [Entity]

    class wasGeneratedBy(ObjectProperty):
        domain   = [Entity]
        range    = [Activity]
    
    class used(ObjectProperty):
        domain   = [Activity]
        range    = [Entity]
    
    class wasAttributedTo(ObjectProperty):
        domain   = [Entity]
        range    = [Agent]
    
    class wasAssociatedWith(ObjectProperty):
        domain   = [Activity]
        range    = [Agent]
    
    class hasMetadata(ObjectProperty):
        domain   = [Entity]
        range    = [Metadata]



agent0 = Agent("pdf-extractor-v2")
activity0 = Activity("extract-data")
activity0.wasAssociatedWith = [agent0]

entity1 = Entity("file1.pdf")
entity1.wasAttributedTo = [agent0]

entity11 = Entity("table11.jpg")
entity11.wasDerivedFrom = [entity1]



entity2 = Entity("file2.pdf")
entity2.wasAttributedTo = [agent0]

entity21 = Entity("table21.jpg")
entity21.wasDerivedFrom = [entity2]


entity3 = Entity("file3.pdf")
entity3.wasAttributedTo = [agent0]

entity31 = Entity("table31.jpg")
entity31.wasDerivedFrom = [entity3]


entity4 = Entity("file4.pdf")
entity4.wasAttributedTo = [agent0]

entity41 = Entity("table41.jpg")
entity42 = Entity("img42.jpg")
entity41.wasDerivedFrom = [entity4]
entity42.wasDerivedFrom = [entity4]


entity5 = Entity("file5.pdf")
entity5.wasAttributedTo = [agent0]

entity51 = Entity("table51.jpg")
entity52 = Entity("img52.jpg")
entity53 = Entity("chart53.jpg")
entity54 = Entity("table54.jpg")
entity51.wasDerivedFrom = [entity5]
entity52.wasDerivedFrom = [entity5]
entity53.wasDerivedFrom = [entity5]
entity54.wasDerivedFrom = [entity5]

metadata1 = Metadata("disable")
entity54.hasMetadata = [metadata1]



onto.save(file = "ontologia/ontologia-prov.owl")
# onto.save(file = "prov.owl", format = "rdfxml")

# entity = onto.Entity("entidade1")
# agent = onto.Agent("agentinho1")
# location = onto.Location('location')
# role = onto.Role('role')
# agent = onto.Agent("agente")
# agent.wasAttributedTo = [entity]
