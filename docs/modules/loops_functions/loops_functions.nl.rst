:orphan:

Code hergebruiken
################################

.. article-info::
    :author: :fa:`brain` Programmeren
    :read-time: 15 min


1
---

We weten nu van een aantal sensoren hoe ze werken en je kan ook de robot hier 
op laten reageren door de motoren aan te sturen. Je zal echter snel merken 
dat de programma’s die je maakt steeds groter en complexer worden. Ook zal je 
zien dat je soms dezelfde blokjes achter elkaar gebruikt. In deze workshop zal 
je leren hoe je die weer kan hergebruiken.

2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      In de workshop ‘rijden maar’ heb je je robot een vierkantje laten rijden. 
      Waarschijnlijk zag je code er ongeveer zo uit als hiernaast.

      Je ziet al dat er een heleboel dezelfde dingen gebeuren. Deze kan je allemaal 
      gaan hergebruiken door er bijvoorbeeld een lus omheen te zetten.

   .. grid-item::

      .. image:: _media/drive_square.png
        :width: 350
        :alt: Drive square

3
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Een lus (Engels: loop) zorgt er voor dat de code een aantal keer doorgelopen 
      wordt. We kunnen de vorige code nu vervangen door hiernaast.

      Dat ziet er al een stuk overzichtelijker uit. Zou zal de robot die stukje dus 
      4 keer doorlopen zodat er een vierkant gemaakt wordt. Wil je dat ze het 
      vierkant 2 keer doet, dan moet ze dat dus 8 keer herhalen.

   .. grid-item::

      .. image:: _media/drive_square_loop.png
        :width: 350
        :alt: Drive square

4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Maar eigenlijk gebruiken we nu nog steeds 3 blokken om 1 stap rechtdoor te maken, 
      en ook 3 blokken om een bocht te maken. Dat zijn misschien wel stappen die je vaker 
      zou willen gebruiken. Als je zulke stukjes code vaker wil gebruiken kunnen we dat 
      doen door er een functie van te maken.

      Door een functieblok te maken kunnen we dit soort stukjes makkelijker hergebruiken. 
      We hebben nu 1 functie gemaakt die zorgt dat de robot rechtdoor gaat en 1 functie 
      die zorgt dat de robot gaat draaien.

   .. grid-item::

      .. image:: _media/drive_square_function.png
        :width: 350
        :alt: Drive square

5
---

Maak nu zelf nog meer functies zodat de robot kan draaien naar links, draaien naar rechts, 
vooruit en achteruit kan en stuur de robot langs een moeilijker parcour.




