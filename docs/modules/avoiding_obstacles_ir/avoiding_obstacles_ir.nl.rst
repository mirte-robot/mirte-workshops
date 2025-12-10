:orphan:

.. _obstacles_ir:

Obstakels ontwijken met IR sensoren
###################################

.. article-info::
    :author: :fa:`brain` Programmeren
    :read-time: 45 min

1
---

In deze workshop leer je hoe je MIRTE obstakels kunt laten ontwijken met behulp van IR (infrarood) sensoren. Controleer eerst of er 2 IR sensoren aangesloten zijn aan de robot. Zo niet, sluit deze sensoren dan eerst aan. De foto's hieronder geven aan hoe de IR sensor eruit ziet, waar deze op de robot hoort te zitten en hoe je deze kunt aansluiten.


2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Om de robot zelfstandig een obstakel te laten herkennen en erop te laten reageren, moet er een programma (ook wel algortime) worden geschreven. Dit kun je op meerdere manieren doen.
      
      Met een IR sensor kan de robot objecten in de omgeving vinden. De IR sensor zendt namelijk (infrarood) licht uit en objecten kaatsen dat licht weer terug. Als dat licht weer terug komt bij de robot, weet de robot in welke richting en hoever een obstakel is. 

      Voor het lijnvolgen gebruikt de robot ook sensoren die werken met infrarood licht. Het verschil met deze sensoren is dat het infrarood licht voor obstakels naar voren gestuurd wordt en objecten het licht weer terugkaatsen. Bij het lijnvolgen wijst de sensor naar beneden en wordt het licht teruggekaast door oppervlakten die licht zijn van kleur. 


   .. grid-item::

      .. image:: _media/situatie-1-sensor.png
         :width: 500
         :alt: Bang Bang method explained in drawing with one sensor


.. dropdown:: :octicon:`dependabot` Obstakelsensor

   Een obstakelsensor stuurt infrarood licht recht vooruit om obstakels te kunnen vinden. 

   - Als er iets in de weg staat, kaatst het licht terug naar de sensor.

   - Als er niks is, komt er geen licht terug.

   Op deze manier weet de robot waar de obstakels zijn.


3
---
Probeer nu een programma te schrijven waarmee de robot een lijn kan volgen. Ga via een nieuw tabblad op internet naar: **mirte.local** en gebruik de blokken om een programma te schrijven.

Kom je er niet helemaal uit? Gebruik dan de tips in het 'Help'-menu hieronder. Op de volgende pagina staat een voorbeeld programma, maar probeer het eerst zelf! Er zijn namelijk meerdere manieren om dit op te lossen.

.. dropdown:: :fa:`question-circle` Help

   - Ik snap niet wat ik moet doen?
      - Je wilt de robot de zwarte lijn laten volgen door de robot naar wit te laten draaien als de sensor de zwarte lijn herkent en je wilt de robot naar de zwarte lijn laten draaien wanneer de sensor wit herkent. Met welke onderdelen kun je de robot laten rijden en draaien?
      - Pas toe wat je hebt geleerd tijdens de workshop '**Wat als...**' en '**Licht meten**'.
   - Welke waarde voor de IR-sensor (lichtwaarde) moet ik invullen?
      - Tijdens de workshop '**Licht meten**' heb je geleerd hoe je de waardes kunt meten voor zowel wit als zwart. In het programma wil je aangeven dat de robot naar wit moet rijden als de waarde van de IR sensor boven/onder een bepaald getal zit en dat deze naar zwart moet rijden als de waarde van de IR sensor boven/onder een bepaald getal zit. Dit getal ligt precies in het midden van de waarde die je hebt gemeten op de zwarte lijn en het witte oppervlak. De waarde die de IR sensor meet, blijft altijd een beetje veranderen. Door precies het midden van de twee waardes te gebruiken, voorkom je dat de twee opdrachten die je de robot geeft met elkaar overlappen.
   - De robot werkte net nog goed, maar nu niet meer en ik heb niks aangepast?
      - De IR sensoren meten licht. Wanneer je de robot in een andere ruimte gebruikt, er zonlicht door de ramen schijnt of je een lamp aan hebt gezet, kan de robot andere waardes meten. Zorg er daarom voor dat je de robot gebruikt in een ruimte waar het licht niet te veel veranderd en meet zo nodig de waardes voor het rijden op zwart en wit opnieuw. 


4
---
Hieronder staat een voorbeeld programma afgebeeld. Deze klopt alleen nog niet helemaal. Kun jij het programma afmaken?

.. image:: _media/voorbeeld_code_lijnvolgen.png
         :width: 500
         :alt: Blockly code for line following with 1 sensor