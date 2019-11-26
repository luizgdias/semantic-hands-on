from owlready2 import *
import yake

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
    
    class OriginalFile(Entity):
        pass

    class Metadata(Entity):
        pass

    class OilWell(Entity):
        pass

    class Table(Entity):
        pass

    class Chart(Entity):
        pass

    class Image(Entity):
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

text = "Exemplo de Poço de petróleo desativado localizado em são paulo"
language = "pt-br"
max_ngram_size = 1
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 4

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)


agent0 = Agent("pdf-extractor-v2")
activity0 = Activity("extract-data")
activity0.wasAssociatedWith = [agent0]

originalfile1                   = OriginalFile("file1.pdf")
originalfile1.wasAttributedTo   = [agent0]

table1                  = Table("table11.jpg")
table1.wasDerivedFrom   = [originalfile1]

originalfile2                   = OriginalFile("file2.pdf")
originalfile2.wasAttributedTo   = [agent0]

table2                  = Table("table21.jpg")
table2.wasDerivedFrom   = [originalfile2]


originalfile3                   = OriginalFile("file3.pdf")
originalfile3.wasAttributedTo   = [agent0]

table3                  = Table("table31.jpg")
table3.wasDerivedFrom   = [originalfile3]


originalfile4                   = OriginalFile("file4.pdf")
originalfile4.wasAttributedTo   = [agent0]

table4 = Table("table41.jpg")
image1 = Image("img42.jpg")
table4.wasDerivedFrom = [originalfile4]
image1.wasDerivedFrom = [originalfile4]


originalfile5 = OriginalFile("file5.pdf")
originalfile5.wasAttributedTo = [agent0]

table5 = Table("table51.jpg")
image2 = Image("img52.jpg")
chart1 = Chart("chart53.jpg")
table6 = Table("table54.jpg")
table5.wasDerivedFrom = [originalfile5]
image2.wasDerivedFrom = [originalfile5]
chart1.wasDerivedFrom = [originalfile5]
table6.wasDerivedFrom = [originalfile5]

print(len(keywords))
index = 0
while index < len(keywords):
    # metadata1 = Metadata("disable")
    metadata1 = Metadata("disable")
    table6.hasMetadata = [metadata1]
    onto.save(file = "ontologia/ontologia-prov.owl")
    index += 1

# for(i = 0; i<= len(keywords); i++):
#     print(kw)
#     metadata1 = Metadata(kw[1])
#     table6.hasMetadata = [metadata1]
#     onto.save(file = "ontologia/ontologia-prov.owl")



# onto.save(file = "ontologia/ontologia-prov.owl")


# onto.save(file = "prov.owl", format = "rdfxml")

# entity = onto.Entity("entidade1")
# agent = onto.Agent("agentinho1")
# location = onto.Location('location')
# role = onto.Role('role')
# agent = onto.Agent("agente")
# agent.wasAttributedTo = [entity]
