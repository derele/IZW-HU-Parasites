# Timetable

|Woche|       |                             |done?|weiteres:
|-----|-------|-----------------------------|-----|---------
|Oktober
|1    | 2.- 6.|build random tree + tag it   | x | 
|2    | 9.-13.|implement wagner-parsimony   | x |
|3    |16.-20.|parsimony + Zahlen           | x | change distribution for random trees to beta-dist
|4    |23.-27.|binary -> not binary         | x | parasite examples searched, first introduction written
|November
|5    |30.- 3.|not binary with changing distribution| x | Book: Inferring Phylogenies - Joseph Felsenstein
|6    | 6.-10.|Metadata collection from big phylogenetic tree | |
|7    |13.-17.|wagner vs fitch vs others??  |   |
|8    |20.-24.|implement these for not binary|   |
|Dezember
|9    |27. -1.|count origins, compare trees|   |
|10   | 4.- 8.|add empty leaf nodes |   |
|11   |||   |
|Jannuar
|Februar
|März

# ToDos:
* Origins Zählen
* verschiedene parsimony algorithmen (Wagner, Fitch, ...) auschecken
    * implementieren?
    * für nicht binär implementieren
* Distanzen zwischen Bäumen
    * Anzahl Origins
    * Anzahl Veränderungen...
    * Distanz nötig? Origins lokalisieren??? Sinnvoll möglich?
        * Emanuel
* Leere Blätter einführen
    * Umgang mit vergessenen Informationen
        * wie vergessen
        * wieviel vergessen
        * wie damit umgehen
* Daten Sammeln
    * von ges Baum und Subbäumen
    * über:
        * #P, #FL, #untagged
* Parameter für beta-Verteilung -> stability analysis