Lesson 16 Potentiometer Module
=================================

**Introduction**

A potentiometer is a device which is used to vary the resistance in an
electrical circuit without interrupting the circuit.

.. image:: media/image164.png
   :width: 1.91111in
   :height: 1.63403in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* Potentiometer module

- 1 \* Dual-Color LED module

- 2 \* 3-Pin anti-reverse cable

- Several Jumper wires

**Experimental Principle**

An analog potentiometer is an analog electronic component. What’s the
difference between an analog one and a digital one? Simply put, a
digital potentiometer refers to just two states like on/off, high/low
levels, i.e. either 0 or 1, while a digital one supports analog signals
like a number from 1 to 1000. The signal value changes over time instead
of keeping an exact number. Analog signals include light intensity,
humidity, temperature, and so on.

In this experiment, PCF8591 is used to read the analog value of the
potentiometer and output the value to LED. Connect pin SIG of the
potentiometer to pin AIN0 of PCF8591. Connect pin R or Pin G of the
Dual-Color LED to pin AOUT of PCF8591 to observe the change of LED.

The schematic diagram of the module is as shown below:

.. image:: media/image165.png
   :width: 3.72222in
   :height: 3.30208in

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
| **Potentiometer**     | **GPIO Extension     | **PCF8591 Module**   |
|                       | Board**              |                      |
+-----------------------+----------------------+----------------------+
| **SIG**               | **\***               | **AIN0**             |
+-----------------------+----------------------+----------------------+
| **VCC**               | **3V3**              | **VCC**              |
+-----------------------+----------------------+----------------------+
| **GND**               | **GND**              | **GND**              |
+-----------------------+----------------------+----------------------+

+----------------------+-----------------------+-----------------------+
| **Dual-Color         | **GPIO Extension      | **PCF8591 Module**    |
| Module**             | Board**               |                       |
+----------------------+-----------------------+-----------------------+
| **R**                | **\***                | **AOUT**              |
+----------------------+-----------------------+-----------------------+
| **GND**              | **GND**               | **GND**               |
+----------------------+-----------------------+-----------------------+
| **G**                | **\***                | **\***                |
+----------------------+-----------------------+-----------------------+

.. image:: media/image166.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\16_Potentiometer_bb.png16_Potentiometer_bb
   :width: 5.38819in
   :height: 5.42569in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/16_potentiometer/

**Step 3:** Compile.

.. code-block::

    gcc potentiometer.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 16_potentiometer.py

Turn the knob of the potentiometer, and you can see the value printed on
the screen change from 0 (minimum) to 255 (maximum).

.. image:: media/image167.jpeg
   :alt: \_MG_2288
   :width: 6.62778in
   :height: 4.56181in