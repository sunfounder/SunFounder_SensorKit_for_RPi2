Lesson 6 Button Module
======================

**Introduction**

In this lesson, we will use button module to control a dual-color LED
module.

.. image:: media/image119.png
   :alt: C:\Users\sunfounder\Desktop\sensor pisd 抠图\Button.pngButton
   :width: 2.03889in
   :height: 1.52986in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- Several Jumper wires

- 1 \* Button module

- 1 \* Dual-color LED module

- 2 \* 3-Pin anti-reverse cable

**Experimental Principle**

Use a normally open button as an input device of Raspberry Pi. When the
button is pressed, the General Purpose Input/Output (GPIO) connected to
the button will change to low level (0V). You can detect the state of
the GPIO through programming. That is, if the GPIO turns into low level,
it means the button is pressed, so you can run the corresponding code.
In this experiment, we will print a string on the screen and control an
LED.

The schematic diagram of the module is as shown below:

.. image:: media/image120.png
   :width: 3.3375in
   :height: 2.69306in

**Experimental Procedures**

**Step 1:** Build the circuit.

+----------------------+----------------------+------------------------+
| **Raspberry Pi**     | **GPIO Extension     | **Button Module**      |
|                      | Board**              |                        |
+----------------------+----------------------+------------------------+
| **GPIO0**            | **GPIO17**           | **SIG**                |
+----------------------+----------------------+------------------------+
| **3.3V**             | **3V3**              | **VCC**                |
+----------------------+----------------------+------------------------+
| **GND**              | **GND**              | **GND**                |
+----------------------+----------------------+------------------------+

+----------------------+----------------------+------------------------+
| **Raspberry Pi**     | **GPIO Extension     | **Dual-Color LED       |
|                      | Board**              | Module**               |
+----------------------+----------------------+------------------------+
| **GPIO1**            | **GPIO18**           | **R**                  |
+----------------------+----------------------+------------------------+
| **GND**              | **GND**              | **GND**                |
+----------------------+----------------------+------------------------+
| **GPIO2**            | **GPIO27**           | **G**                  |
+----------------------+----------------------+------------------------+

.. image:: media/image121.png
   :alt: 06_Button_bb
   :width: 5.85694in
   :height: 5.60417in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/06_button/

**Step 3:** Compile.

.. code-block::

    gcc button.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 06_button.py

The LED on the module will emit green light. If you press the button,
"Button pressed" will be printed on the screen and the LED will emit red
light. If you release the button, "Button released" will be printed on
the screen and the LED will flash green again.

.. image:: media/6.png