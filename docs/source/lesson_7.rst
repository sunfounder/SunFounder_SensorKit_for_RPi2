Lesson 7 Tilt-Switch Module
===========================

**Introduction**

The tilt-switch module (as shown below) in this kit is a ball
tilt-switch with a metal ball inside. It is used to detect inclinations
of a small angle.

.. image:: media/image123.png
   :width: 1.54931in
   :height: 1.33403in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* Dual-color LED module

- 1 \* Tilt-switch module

- 2 \* 3-Pin anti-reverse cable

**Experimental Principle**

The principle is very simple. The ball in the tilt-switch changes with
different angle of inclination to trigger the circuit. When the ball in
tilt switch runs from one end to the other end due to shaking caused by
external force, the tilt switch will conduct and the LED will emit red
light, otherwise it will break and the LED will emit green light.

The schematic diagram of the module is as shown below:

.. image:: media/image124.png
   :alt: C:\Users\sunfounder\Desktop\123.png
   :width: 3.94028in
   :height: 2.91042in

**Experimental Procedures**

**Step 1:** Build the circuit.

+----------------------+-----------------------+-----------------------+
| **Raspberry Pi**     | **GPIO Extension      | **Tilt Switch         |
|                      | Board**               | Module**              |
+----------------------+-----------------------+-----------------------+
| **GPIO0**            | **GPIO17**            | **SIG**               |
+----------------------+-----------------------+-----------------------+
| **3.3V**             | **3V3**               | **VCC**               |
+----------------------+-----------------------+-----------------------+
| **GND**              | **GND**               | **GND**               |
+----------------------+-----------------------+-----------------------+

+----------------------+-----------------------+-----------------------+
| **Raspberry Pi**     | **GPIO Extension      | **Dual-Color LED      |
|                      | Board**               | Module**              |
+----------------------+-----------------------+-----------------------+
| **GPIO1**            | **GPIO18**            | **R**                 |
+----------------------+-----------------------+-----------------------+
| **GND**              | **GND**               | **GND**               |
+----------------------+-----------------------+-----------------------+
| **GPIO2**            | **GPIO27**            | **G**                 |
+----------------------+-----------------------+-----------------------+

.. image:: media/image125.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\07_Tilt-Switch_bb.png07_Tilt-Switch_bb
   :width: 6.46181in
   :height: 5.90417in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/07_tilt_switch/

**Step 3:** Compile.

.. code-block::

    gcc tilt_switch.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 07_tilt_switch.py

Place the tilt switch module horizontally, and the LED will flash green.
If you tilt it, "Tilt!" will be printed on the screen and the LED will
change to red. Place it horizontally again, and the LED will flash green
again.

.. image:: media/7.png