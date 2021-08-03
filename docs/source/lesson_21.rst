Lesson 21 Flame Sensor
=========================

**Introduction**

A flame sensor (as shown below) performs detection by capturing infrared
rays with specific wavelengths from flame. It can be used to detect and
warn of flames.

.. image:: media/image29.png
  :width: 250

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* Flame sensor module

- 1 \* PCF8591

- 1 \* 4-Pin anti-reverse cable

- Several Jumper wires

**Experimental Principle**

There are several types of flame sensors. In this experiment, we will
use a far-infrared flame sensor. It can detect infrared rays with
wavelength ranging from 700nm to 1000nm. A far-infrared flame probe
converts the strength changes of external infrared light into current
changes. And then it convert analog quantities into digital ones. In
this experiment, connect pin D0 of the Flame Sensor module to a GPIO of
Raspberry Pi to detect by programming whether any flame exists. The
schematic diagram:

.. image:: media/image194.png
   :width: 6.65972in
   :height: 3.43611in

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

+----------------------+-----------------------+-----------------------+
| **Flame Sensor**     | **GPIO Extension      | **PCF8591 Module**    |
|                      | Board**               |                       |
+----------------------+-----------------------+-----------------------+
| **DO**               | **GPIO17**            | **\***                |
+----------------------+-----------------------+-----------------------+
| **AO**               | **\***                | **AIN0**              |
+----------------------+-----------------------+-----------------------+
| **VCC**              | **3V3**               | **VCC**               |
+----------------------+-----------------------+-----------------------+
| **GND**              | **GND**               | **GND**               |
+----------------------+-----------------------+-----------------------+

.. image:: media/image195.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\21_Flame_Sensor_bb.png21_Flame_Sensor_bb
   :width: 5.33889in
   :height: 5.71319in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/21_flame_sensor/

**Step 3:** Compile.

.. code-block::

    gcc flame_sensor.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 21_flame_sensor.py

Now, ignite a lighter near the sensor, within the range of 80cm, and
"Fire!" will be displayed on the screen. If you put out the lighter or
just move the flames away from the flame sensor, "Safe~" will be
displayed then.

.. image:: media/image196.jpeg