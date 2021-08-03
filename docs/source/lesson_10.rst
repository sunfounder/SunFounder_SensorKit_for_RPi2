Lesson 10 Buzzer Module
=======================

**Introduction**

Buzzers can be categorized as active and passive ones (See the following
picture).

.. image:: media/8.png
  :width: 600

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* Passive buzzer module

- 1 \* Active buzzer module

- 1 \* 3-Pin anti-reverse cable

**Experimental Principle**

Place the pins of two buzzers face up and you can see the one with a
green circuit board is a passive buzzer, while the other with a black
tape, instead of a board, is an active buzzer.

.. image:: media/image136.png
   :alt: E:\Sally's file\Done\Super kit for arduino&rpi\buzzer.png
   :width: 4.77431in
   :height: 1.71389in

**Active buzzer Passive buzzer**

The difference between an active buzzer and a passive buzzer is:

An active buzzer has a built-in oscillating source, so it will make
sounds when electrified. But a passive buzzer does not have such source,
so it will not beep if DC signals are used; instead, you need to use
square waves whose frequency is between 2K and 5K to drive it. The
active buzzer is often more expensive than the passive one because of
multiple built-in oscillating circuits.

The schematic diagram of the module is as shown below:

.. image:: media/image137.png
   :width: 4.19861in
   :height: 2.77708in

**Experimental Procedures**

**Active Buzzer**

.. note::
    The active buzzer has built-in oscillating source, so it will beep as long as it is wired up, but it can only beep with fixed frequency.

**Step 1:** Build the circuit.

.. image:: media/image138.png
   :width: 5.33611in
   :height: 4.45625in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/10_active_buzzer/

**Step 3:** Compile.

.. code-block::

    gcc active_buzzer.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 10_active_buzzer.py

Now you can hear the active buzzer beeping.

.. image:: media/image139.jpeg

**Passive Buzzer**

**Step 1:** Build the circuit.

+-----------------------+----------------------+----------------------+
| **Raspberry Pi**      | **GPIO Extension     | **Passive Buzzer     |
|                       | Board**              | Module**             |
+-----------------------+----------------------+----------------------+
| **GPIO0**             | **GPIO17**           | **SIG**              |
+-----------------------+----------------------+----------------------+
| **3.3V**              | **3V3**              | **VCC**              |
+-----------------------+----------------------+----------------------+
| **GND**               | **GND**              | **GND**              |
+-----------------------+----------------------+----------------------+

.. image:: media/image140.png
   :width: 6.21111in
   :height: 5.09375in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/10_passive_buzzer/

**Step 3:** Compile.

.. code-block::

    gcc passive_buzzer.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 10_passive_buzzer.py

Now you can hear the passive buzzer playing music.

.. image:: media/image139.jpeg
