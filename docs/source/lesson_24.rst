Lesson 24 Touch Switch
========================

**Introduction**

A touch sensor operate with the conductivity of human body. When you
touch the metal on the base electrode of the transistor, the level of
pin SIG will turn over.

.. image:: media/image204.png
   :width: 1.44653in
   :height: 1.2in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* Touch sensor module

- 1 \* Dual-Color LED module

- 2 \* 3-Pin anti-reverse cable

**Experimental Principle**

In this experiment, touch the base electrode of the transistor by
fingers to make it conduct as human body itself is a kind of conductor
and an antenna that can receive electromagnetic waves in the air. These
electromagnetic wave signals collected from the human body are amplified
by the transistor and processed by the comparator on the module to
output steady signals. The schematic diagram:

.. image:: media/image205.png
   :width: 5.02153in
   :height: 3.22361in

**Experimental Procedures**

**Step 1:** Build the circuit.

+-----------------------+----------------------+----------------------+
| **Raspberry Pi**      | **GPIO Extension     | **Touch Sensor       |
|                       | Board**              | Module**             |
+-----------------------+----------------------+----------------------+
| **GPIO0**             | **GPIO17**           | **SIG**              |
+-----------------------+----------------------+----------------------+
| **3.3V**              | **3V3**              | **VCC**              |
+-----------------------+----------------------+----------------------+
| **GND**               | **GND**              | **GND**              |
+-----------------------+----------------------+----------------------+

+-----------------------+----------------------+----------------------+
| **Raspberry Pi**      | **GPIO Extension     | **Dual-Color LED     |
|                       | Board**              | Module**             |
+-----------------------+----------------------+----------------------+
| **GPIO1**             | **GPIO18**           | **R**                |
+-----------------------+----------------------+----------------------+
| **GND**               | **GND**              | **GND**              |
+-----------------------+----------------------+----------------------+
| **GPIO2**             | **GPIO27**           | **G**                |
+-----------------------+----------------------+----------------------+


.. image:: media/image206.png
  :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\24_Touch_Switch_bb.png24_Touch_Switch_bb
  :width: 6.31597in 
  :height: 5.46875in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/24_touch_switch/

**Step 3:** Compile.

.. code-block::

    gcc touch_switch.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 24_touch_switch.py

Now, touch the metal disk, you can see the LED change its colors and
"ON" and "OFF" printed on the screen.

.. image:: media/image207.jpeg