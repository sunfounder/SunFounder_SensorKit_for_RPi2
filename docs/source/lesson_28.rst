Lesson 28 Humiture Sensor
===========================

**Introduction**

The digital temperature and humidity sensor DHT11 is a composite sensor
that contains a calibrated digital signal output of temperature and
humidity. The technology of a dedicated digital modules collection and
the temperature and humidity sensing technology are applied to ensure
that the product has high reliability and excellent long-term stability.

.. image:: media/image219.png
   :width: 1.76111in
   :height: 1.47431in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* Humiture module

- 1 \* 3-Pin anti-reverse cable

**Experimental Principle**

.. image:: media/image220.png
   :alt: DHT11_Pins
   :width: 2.70694in
   :height: 2.00069in

Only three pins are available for use: VCC, GND, and DATA. The
communication process begins with the DATA line sending start signal to
DHT11, and DHT11 receives the signal and returns an answer signal, then
the host receives the answer signal and begins to receive 40-bit
humiture data (8-bit humidity integer + 8-bit humidity decimal + 8-bit
temperature integer + 8-bit temperature decimal + 8-bit checksum). For
more information, please refer to the datasheet of DHT11.

.. image:: media/image221.png
   :width: 3.93333in
   :height: 2.76597in

**Experimental Procedures**

**Step 1:** Build the circuit.

+-----------------------+---------------------+------------------------+
| **Raspberry Pi**      | **GPIO Extension    | **Humiture Module**    |
|                       | Board**             |                        |
+-----------------------+---------------------+------------------------+
| **GPIO0**             | **GPIO17**          | **SIG**                |
+-----------------------+---------------------+------------------------+
| **3.3V**              | **3V3**             | **VCC**                |
+-----------------------+---------------------+------------------------+
| **GND**               | **GND**             | **GND**                |
+-----------------------+---------------------+------------------------+

.. image:: media/image222.png
   :width: 600

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/28_humiture/

**Step 3:** Compile.

.. code-block::

    gcc humiture.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 28_humiture.py

Now, you can see humidity and temperature value printed on the screen.

.. image:: media/image223.jpeg