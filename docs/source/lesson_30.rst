Lesson 30 I2C LCD1602
=======================

**Introduction**

LCD1602 is a character type liquid crystal display, which can display 32
(16*2) characters at the same time. It has 16 pins, of which at least 7
would be used each time. You can use a PCF8574 I2C chip to expand I/O
ports so only two GPIO ports would be occupied.

.. image:: media/image228.png
   :width: 3.29167in
   :height: 1.49514in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* I2C LCD1602

- Several jumper wires

**Experimental Principle**

In this experiment, I2C is used to configure LCD so that you can control
the LCD1602 to display characters. The I2C slave address of I2C LCD1602
here is 0x27.

**Experimental Procedures**

**Step 1:** Build the circuit.

+----------------------+----------------------+------------------------+
| **Raspberry Pi**     | **GPIO Extension     | **I2C LCD1602 Module** |
|                      | Board**              |                        |
+----------------------+----------------------+------------------------+
| **SCL**              | **SCL1**             | **SCL**                |
+----------------------+----------------------+------------------------+
| **SDA**              | **SDA1**             | **SDA**                |
+----------------------+----------------------+------------------------+
| **5V**               | **5V0**              | **VCC**                |
+----------------------+----------------------+------------------------+
| **GND**              | **GND**              | **GND**                |
+----------------------+----------------------+------------------------+

.. image:: media/image229.png
   :width: 5.28611in
   :height: 5.03542in

**Step 2:** Setup I2C(see Appendix. If you have set I2C, skip
this step.)

**For C Users:**

**Step 3:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/30_i2c_lcd1602/

**Step 4:** Compile.

.. code-block::

    gcc i2c_lcd1602.c -lwiringPi

**Step 5:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 3:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 4:** Run.

.. code-block::

    sudo python3 30_i2c_lcd1602.py

Now you can see “Greetings! From SunFounder” displayed on the LCD.

.. image:: media/image230.jpeg
