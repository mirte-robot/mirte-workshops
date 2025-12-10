:orphan:

Wakker worden
#########################

.. article-info::
    :author: :fa:`cog` Doen
    :read-time: 15 min


1
----

Nadat je in de vorige workshop de robot helemaal in elkaar hebt gezet, is het
nu tijd om haar wakker te maken.  In deze workshop leer je hoe je de robot aanzet.


.. _hard_reset:

2
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Als je de robot helemaal goed in elkaar hebt gezet is het nu tijd om de robot 
      aan te zetten. Dit kan je doen door het schuifje op de PCB van ‘off’ naar ‘on’ 
      te zetten. 
   
   .. grid-item::
   
      .. image:: _media/pcb_on.jpg
        :width: 350
        :alt: PCB on


3
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      De lampjes van de robot gaan nu branden. Op de computer gaat er eerst het rode lampje
      aan. Daarna de groene.

      Elke robot heeft haar eigen unieke ID. Als je het ID van je robot nog niet weet, en 
      er meerdere robots in de ruimte zijn zal je nog je ID van de robot moeten oncijferen.
      Dit kan je doen door het knipperen van de ledjes te volgen (zoals te zien in de video).

      Het duurt altijd even voordat de robot wakker is. Je moet even wachten totdat 
      het groene lampje op de computer begint met knipperen en er ook een rood lampje gaat 
      knipperen. Vanaf dat moment kan je naar de volgende stap om te verbinden.

   .. grid-item::

      .. video:: /_static/media/mirte_wifi_blinking.mp4
         :width: 500
         :autoplay:
         :loop:

.. dropdown:: :fa:`question-circle` Help

   - Als je helemaal geen lampjes zie branden:
      - Controleer of de kabel van de powerbank naar de PCB goed zit.
      - Controleer of de PCB goed op de computer zit.
      - Controleer dat je de knop op de PCB echt op aan hebt gezet.
   - Als je wel lampjes ziet branden, maar niet die van de computer: 
      - Controleer of de SD kaart in de computer zit.
      - Weet je zeker dat de goede software op de SD kaart staat?
   - Als het groene lampje wel gaat branden, maar niet gaat knipperen:
      - Weet je zeker dat je ongeveer 2 minuten hebt gewacht?
      - Doe de schakelaar van de PCB uit en daarna nog een keer aan.
   - Als die allemaal niet werkt:
      - Dan zal je je SD kaartje opnieuw moeten 'flashen'.

4
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Zodra het rode lampje knippert is de computer wakker en kunnen we aan de slag. Het 
      eerste wat we moeten doen is met de robot verbinden. De robot heeft een Wifi-netwerkje 
      gestart met de naam: Mirte-XXXXXX (waarbij XXXXXX de cijfers en getallen zijn die je in
      de vorige stap hebt ontcijferd).

      Je kan op een laptop een verbinding maken met jouw robot door het wachtwoord 
      ‘mirte_mirte’ in te vullen en op ‘Next’ te klikken.

   .. grid-item::
      
      .. tab-set::

         .. tab-item:: Windows
            :sync: windows

            .. image:: _media/wifi_windows.png
               :width: 350
               :alt: Windows Wifi

         .. tab-item:: Chromebook
            :sync: chromebook

            .. image:: _media/wifi_chromebook.png
               :width: 350
               :alt: Chromebook Wifi

.. admonition:: LET OP
   :class: warning

   Er zullen meerdere Mirte-XXXXXX netwerken in zichtbaar zijn. Elke robot heeft er 1.
   Zorg dat je zeker weet dat jij verbindt met jouw robot.

.. dropdown:: :fa:`question-circle` Help

   - Als er geen Wifi netwerk Mirte-XXXXXX is:
      - Weet je zeker dat je de lampjes op de computer hebt zien knipperen?
      - Controleer of je misschien met een andere computer (of telefoon) het netwerk
        wel kan vinden.
   - Als er geen XXXXXX op de doos staat en je dus niet weet welke robot je hebt:
      - Je kan door naar de lampjes te kijken zien welke XXXXXX je robot heeft. Dit
        kan je `hier <get_ssid>` doen.

5
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Op de volgende vraag die Windows je stelt maakt het antwoord niet zo veel uit. Je mag hier dus zowel ‘Yes’ als ‘No’ klikken.

   .. grid-item::

      .. image:: _media/windows_discovery.png
        :width: 350
        :alt: Windows discovery



6
----

Het kan even duren voordat de robot verbinding heeft. Op een gegeven moment moet de verbinding zeggen: ‘Verbonden, geen internet’.

.. dropdown:: Help

   - Als er geen verbinding komt:
      - Weet je zeker dat je als wachtwoord 'mirte_mirte' (dus zonder ') hebt gebruikt?
      - Als je lampjes op de computer wel knipperen, en je zeker weet dat je het goede wachtwoord in hebt getypt, kan je 
        helaas als beste toch de robot nog een keer opnieuw aan en uitzetten door de schakelaar weer aan te zetten.
        Dus weer terug naar stap 2.

7
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Zodra je verbinding hebt kan je in een browser (Edge, Firefox, Chrome, etc) naar de volgende webpagina gaan:

      http://192.168.42.1

      Het kan even duren voordat deze pagina laadt. Probeer het dan na een minuut nog een keer door in je browser
      op 'refresh' te drukken.


   .. grid-item::

      .. image:: _media/new_tab.png
        :width: 350
        :alt: New Tab


8
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Je ziet nu het startscherm van Mirte (het is niet erg dat er ‘niet beveiligd’ staat). In dit startscherm
      kunnen we de robot vertellen wat ze moet doen. Dit is vanuit waar we de volgende workshops allemaal gaan
      doen. Het kan even duren voordat dit volledig geladen is. Als je de sensoren aan de linkerkant ziet
      verschijnen is de verbinding goed gemaakt.

   .. grid-item::

      .. image:: _media/mirte_home.png
        :width: 350
        :alt: Mirte Web Interface

.. admonition:: LET OP
   :class: warning

   Soms kan het zijn dat je computer ineens niet meer met de Mirte robot verbonden is, maar weer standaard
   naar een ander netwerk is. Dan kan het zijn dat je het startscherm wel ziet, maar er niets meer mee kan
   doen. Dit kan ook gebeuren als je bezig bent. Zorg er dan voor dat je weer vebindt met de Mirte robot
   en dat je de pagina refresht door op F5 te drukken.


.. dropdown:: Help

   - Als je het startscherm wel ziet, maar de sensoren komen er niet bij:
      - Probeer de pagina opnieuw te laden door op F5 te drukken.
   - Blijft het probleem:
      - Probeer dan opnieuw op te starten door de robot uit te zetten zoals je kan zien in de volgende stap.

.. _shutdown:

9
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Waarschijnlijk ga je nu door met de volgende workshop, maar het is nu wel goed om ook te weten hoe we haar 
      weer kunnen laten slapen (uit zetten). Rechtsboven in je scherm zie je een knop om dit te doen. 

   .. grid-item::

      .. image:: _media/shutdown.png
        :width: 70
        :alt: Shutdown

.. admonition:: LET OP
   :class: warning

   Nadat je op de knop hebt gedrukt moet je nog wel de knop dit je in stap 1 hebt gebruikt weer uit zetten. 
   **Dit moet je pas doen wanneer het lampje op de kleine PC uit is!** Anders kan het zijn dat ze de volgende 
   keer niet goed wakker kan worden. 

   .. image:: _media/shutdown_message.png
      :width: 350
      :alt: Shutdown Message




