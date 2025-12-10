:orphan:

Wat als.....
#########################

.. article-info::
    :author: :fa:`brain` Programmeren
    :read-time: 30 min



1
---

Nu we een van de sensoren van de robot kunnen uitlezen kunnen we die waarde gebruiken 
om de robot iets te laten doen. In deze workshop zal je wat basis programmeren leren 
zodat je je robot iets kan laten doen afhankelijk van wat ze ziet. Je robot zal 
stoppen ze een lijn ziet.

.. video:: /_static/media/mirte_stop_at_line.mp4
   :width: 500
   :autoplay:
   :loop:



2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Het programmeren van de robot gaan we uiteraard op het ‘Programmeren’ tabblad 
      doen. In de vorige workshop heb je de waarde van de sensor 1 keer met een blok 
      uitgelezen.

      Het is natuurlijk handiger om dit een aantal keer achter elkaar te doen. Dit 
      kunnen we doen met ‘Lussen’ (‘loops’ in het Engels). Je kan deze om het tesktblok 
      heen zetten en op ‘play’ drukken.

   .. grid-item::

      .. image:: _media/10_times.png
         :width: 350
         :alt: 10 Times

.. admonition:: TIP
   :class: tip

   Als je nou een foutje hebt gemaakt kan je met de ‘undo’ knop weer terug naar je 
   vorige programma.

   .. image:: _media/undo_button.png
      :width: 70
      :alt: Undo

3
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Je ziet nu dat de waarde 10 keer heel snel achter elkaar rechtsonder neer wordt 
      gezet. Dit is natuurlijk wel heel snel achter elkaar. Om iets beter te zien wat 
      er gebeurt kan je een ‘wachtblok’ toevoegen zodat je beter kan zien wat er gebeurt.

   .. grid-item::

      .. image:: _media/10_times_sleep.png
         :width: 350
         :alt: 10 Times with sleep

4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Maar ook dat is nog niet altijd even handig. Het zou handiger zijn als het programma 
      de hele tijd als het klaar is weer opnieuw begint. Dat kan je bereiken door een een 
      ‘herhalen zolang waar’ (in het Engels staat dit bekend als ‘while true’) blok omheen 
      zet.

   .. grid-item::

      .. image:: _media/while_true.png
         :width: 350
         :alt: While true

.. admonition:: LET OP
   :class: warning

   Als je sensoren uit gaat lezen in een ‘herhalen zolang waar’ blok moet je er ook een 
   ‘wacht’-blok aan toevoegen. Als je dit niet doet probeert de robot zó snel de sensor 
   uit te lezen dat ze het niet meer bij kan houden. Je zal dan zien dat de waardes van 
   je sensor achter gaan lopen en je dus waardes terugkrijgt van vroeger.

5
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Je al nu ook merken dat je programma niet meer stopt. Dit kan je nog steeds doen 
      door op de ‘stop’ knop te drukken.

   .. grid-item::

      .. image:: _media/stop_button.png
         :width: 70
         :alt: Stop button

6
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Om nou een te laten stoppen als ze een zwarte lijn ziet kunnen we een ‘als-dan’ 
      (Engels: if-else) blok gaan gebruiken en herkennen dat ze een lijn zien. Dit blok 
      zorgt er voor dat je robot iets doet wat afhangt van een bepaalde voorwaarde 
      (conditie).

      In het voorbeeld hiernaast zal je robot doorhebben of haar sensor op een zwarte 
      lijn staat of niet. Je kan de robot dus nu op de grond zetten en eens over de 
      lijn laten bewegen.

   .. grid-item::

      .. image:: _media/detect_line.png
         :width: 350
         :alt: Stop button

.. admonition:: LET OP
   :class: warning
   
   De waarde vanaf wanneer de robot dit als zwart ziet moet je zelf nog vinden en
   invullen.

.. admonition:: TIP
   :class: tip

   Als je een foutje hebt gemaakt en je ‘undo’ te onhandig vindt kan je blokken ook 
   weggooien door ze naar de prullenbak te verplaatsen.

   .. image:: _media/bin.png
         :width: 70
         :alt: Bin


7
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Het kan natuurlijk heel goed zijn dat je denkt dat je programma zou moeten werken, 
      maar dat de robot niet helemaal doet wat jij denkt dat ze zou moeten doen.

      In dat geval is het soms handig om je programma even te pauzeren en stap voor stap 
      door de code heen te gaan. Dit heet (uit het Engels) ‘debuggen’. Een programma van 
      Mirte kan je ook debuggen door op de pauzeknop te drukken:

      .. image:: _media/pause_button.png
         :width: 70
         :alt: Pause

      Je programma stopt dan even en in de blokken licht het blok waar die mee straks 
      mee bezig zal gaan op.

      In Python zie je hetzelfde, alleen zie je daar aan het rode stipje welke regel hij 
      straks uit zal voeren. Je kan deze regel/blok uit laten voeren door op ‘step’ te drukken:

      .. image:: _media/step_button.png
         :width: 70
         :alt: Step

      De robot gaat dan die regel uitvoeren en pauzeert meteen weer bij de volgende regel.
      Je kan zo goed zien wat de robot aan het doen is.

   .. grid-item::

      .. tab-set::

         .. tab-item:: Blokken
            :sync: blockly

            .. image:: _media/debug_blockly.png
               :width: 350
               :alt: Blockly debug


         .. tab-item:: Python
            :sync: python

            .. image:: _media/debug_python.png
               :width: 350
               :alt: Python debug


8
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Opdracht**: Nu moeten we de robot nog laten rijden en stoppen als ze een lijn ziet. Dit kunnen 
      we doen door de motorblokken weer te gebruiken.

      Hierin kan je zelf nog even spelen met de waardes voor de motoren, de sleep en de 
      waarde om de lijn te detecteren. Wanneer ziet ze de lijn niet meer? En wanneer
      gaat die echt goed? 

      Lukt het je om dit programmatje nog wat compacter te krijgen?

   .. grid-item::

      .. tab-set::

         .. tab-item:: Blokken
            :sync: blockly

            .. image:: _media/stop_line_blockly.png
               :width: 350
               :alt: Blockly stop at line


         .. tab-item:: Python
            :sync: python

            .. image:: _media/stop_line_python.png
               :width: 350
               :alt: Python stop at line
