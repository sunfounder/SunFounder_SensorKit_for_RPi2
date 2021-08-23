Lesson 3 7-Color Auto-flash LED
===============================

**Introduction**

On the 7-Color Auto-flash LED module, the LED can automatically flash
built-in colors after power on. It can be used to make quite fascinating
light effects.

.. image:: media/image106.png
   :width: 1.65556in
   :height: 1.35972in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* 7-color auto-flash LED module

- 1 \* 3-Pin anti-reverse cable

**Experimental Principle**

When it is power on, the 7-color auto-flash LED will flash built-in
colors.

The schematic diagram of the module is as shown below:

.. image:: media/image107.png
   :width: 2.28056in
   :height: 1.85208in

**Experimental Procedures**

Build the circuit.

+-----------------------+----------------------+----------------------+
| **Raspberry Pi**      | **GPIO Extension     | **Auto-flash LED     |
|                       | Board**              | Module**             |
+-----------------------+----------------------+----------------------+
| **GND**               | **GND**              | **GND**              |
+-----------------------+----------------------+----------------------+
| **3.3V**              | **3V3**              | **VCC**              |
+-----------------------+----------------------+----------------------+

.. image:: media/image108.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\03_AutoFlashLED_bb.png03_AutoFlashLED_bb
   :width: 5.17639in
   :height: 4.40833in

.. note::

    There are two \"GND\" pins on the module. You only need to connect one of them.

Now, you will see 7-color auto-flash LED flashing seven colors.

.. image:: media/image109.jpeg