Lesson 20 Photoresistor Module
================================

**Introduction**

A photoresistor is a light-controlled variable resistor.
The resistance of a photoresistor decreases with increasing incident
light intensity.

.. image:: media/image189.png
   :width: 1.82847in
   :height: 1.45in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* PCF8591

- 1 \* Photoresistor module

- 1 \* 3-Pin anti-reverse cable

- Several Jumper wires

**Experimental Principle**

With light intensity increasing, the resistance of a photoresistor will
decrease. Thus the output voltage changes. Analog signals collected by
the photoresistor are converted to digital signals through PCF8591. Then
these digital signals are transmitted to Raspberry Pi and printed on the
screen. The schematic diagram:

.. image:: media/image190.png
   :width: 3.34931in
   :height: 3.14306in

**Experimental Procedures**

**Step 1:** Build the circuit.

+-----------------------+----------------------+----------------------+
| **Raspberry Pi**      | **GPIO Extension     | **PCF8591 Module**   |
|                       | Board**              |                      |
+-----------------------+----------------------+----------------------+
| **SDA**               | **SDA1**             | **SDA**              |
+-----------------------+----------------------+----------------------+
| **SCL**               | **SCL1**             | **SCL**              |
+-----------------------+----------------------+----------------------+
| **3.3V**              | **3V3**              | **VCC**              |
+-----------------------+----------------------+----------------------+
| **GND**               | **GND**              | **GND**              |
+-----------------------+----------------------+----------------------+

+-----------------------+----------------------+----------------------+
| **Photoresistor**     | **GPIO Extension     | **PCF8591 Module**   |
|                       | Board**              |                      |
+-----------------------+----------------------+----------------------+
| **SIG**               | **\***               | **AIN0**             |
+-----------------------+----------------------+----------------------+
| **VCC**               | **3V3**              | **VCC**              |
+-----------------------+----------------------+----------------------+
| **GND**               | **GND**              | **GND**              |
+-----------------------+----------------------+----------------------+

.. image:: media/image191.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\20_Photoresistor_bb.png20_Photoresistor_bb
   :width: 6.34444in
   :height: 6.02639in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/20_photoresistor/

**Step 3:** Compile.

.. code-block::

    gcc photoresistor.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 20_photoresistor.py

Now, change light intensity (e.g. cover the module with a pad), and the
value printed on the screen will change accordingly.

.. image:: media/image192.jpeg