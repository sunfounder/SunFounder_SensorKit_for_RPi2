Lesson 25 Ultrasonic Ranging Module
=====================================

**Introduction**

The ultrasonic sensor uses sound to accurately detect objects and
measure distances. It sends out ultrasonic waves and converts them into
electronic signals.

.. image:: media/image33.png
   :width: 2.35347in
   :height: 1.50903in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* Ultrasonic ranging module

- 1 \* 4-Pin anti-reverse cable

**Experimental Principle**

This sensor works by sending a sound wave out and calculating the time
it takes for the sound wave to get back to the ultrasonic sensor. By
doing this, it can tell us how far away objects are relative to the
ultrasonic sensor.

Test distance = (high level time \* velocity of sound (340M/S)) / 2 (in
meters)

**Experimental Procedures**

**Step 1**: Build the circuit.

+-----------------------+---------------------+------------------------+
| **Raspberry Pi**      | **GPIO Extension    | **Ultrasonic Ranging   |
|                       | Board**             | Module**               |
+-----------------------+---------------------+------------------------+
| **3.3V**              | **3V3**             | **VCC**                |
+-----------------------+---------------------+------------------------+
| **GPIO0**             | **GPIO17**          | **Trig**               |
+-----------------------+---------------------+------------------------+
| **GPIO1**             | **GPIO18**          | **Echo**               |
+-----------------------+---------------------+------------------------+
| **GND**               | **GND**             | **GND**                |
+-----------------------+---------------------+------------------------+

.. image:: media/image208.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\25_Ultrasonic_Ranging_bb.png25_Ultrasonic_Ranging_bb
   :width: 6.09861in
   :height: 5.53472in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

   cd /home/pi/SunFounder_SensorKit_for_RPi2/C/25_ultrasonic_ranging/

**Step 3:** Compile.

.. code-block::

    gcc ultrasonic_ranging.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 25_ultrasonic_ranging.py

Now you can see the distance between the ultrasonic ranging module and
the obstacle (like your palm) in front on the screen. Sway your hand
over the ultrasonic ranging module slowly and observe the distance
printed on the screen.

.. image:: media/image209.jpeg