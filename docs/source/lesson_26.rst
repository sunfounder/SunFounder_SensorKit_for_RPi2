Lesson 26 DS18B20 Temperature Sensor
======================================

**Introduction**

Temperature Sensor DS18B20 is a commonly used digital temperature sensor
featured with small size, low-cost hardware, strong anti-interference
capability and high precision. The digital temperature sensor is easy to
wire and can be applied a various occasions after packaging. Different
from conventional AD collection temperature sensors, it uses a 1-wire
bus and can directly output temperature data.

.. image:: media/image34.png
  :width: 250

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* DS18B20 Temperature Sensor module

- 1 \* 3-Pin anti-reverse cable

**Experimental Principle**

With a unique single-wire interface, DS18B20 requires only one pin for a
two-way communication with a microprocessor. It supports multi-point
networking to measure multi-point temperatures. Eight sensors can be
connected at most, because it will consume too much power supply and
cause low voltage thus harming the stability of transmission.

When using the DS18B20, you need to connect a 10KΩ resistor to the
middle pin DQ to pull up the level. The schematic diagram of the module
is as shown below:

.. image:: media/image211.png
   :width: 3.24931in
   :height: 2.99722in

**Experimental Procedures**

**Step 1:** Build the circuit according to the following method.

+----------------------+---------------------+------------------------+
| **Raspberry Pi**     | **GPIO Extension    | **DS18B20 Temperature  |
|                      | Board**             | Sensor**               |
+----------------------+---------------------+------------------------+
| **GPIO7**            | **GPIO4**           | **SIG**                |
+----------------------+---------------------+------------------------+
| **3.3V**             | **3V3**             | **VCC**                |
+----------------------+---------------------+------------------------+
| **GND**              | **GND**             | **GND**                |
+----------------------+---------------------+------------------------+

.. image:: media/image212.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\26_DS18B20_bb.png26_DS18B20_bb
   :width: 5.65139in
   :height: 4.99167in

**Step 2:** Upgrade your kernel.

.. code-block::

    sudo apt-get update
    sudo apt-get upgrade

**Step 3:** You can edit that file with nano.

.. code-block::

    sudo nano /boot/config.txt

Then scroll to the bottom and type.

.. code-block::

    dtoverlay = w1-gpio

Then reboot with

.. code-block::

    sudo reboot

Mount the device drivers and confirm whether the device is effective or
not.

.. code-block::

    sudo modprobe w1-gpio
    sudo modprobe w1-therm
    cd /sys/bus/w1/devices/
    ls

The result is as follows:

.. code-block::

    root@rasberrypi:/sys/bus/w1/devices# ls
    28-00000495db35 w1_bus_master1

28-00000495db35 is an external temperature sensor device, but it may
vary with every client. This is the serial number of your ds18b20.

**Step 4:** Check the current temperature.

.. code-block::

    cd 28-00000495db35
    ls

The result is as follows:

.. code-block::

    root@rasberrypi:/sys/bus/w1/devices/28-00000495db35# ls
    driver  id  name  power  subsystem  uevent  w1_slave
    cat w1_slave

The result is as follows:

.. code-block::

    root@raspberrypi:/sys/bus/w1_slave/28-00000495db35# cat w1_slave
    a3 01 4b 46 7f ff 0d 10 ce : crc=ce YES
    a3 01 4b 46 7f ff 0d 10 ce t=26187

The second line t=26187 is current temperature value. If you want to
convert it to degree Celsius, you can divide by 1000, that is, the
current temperature is 26187/1000=26.187 ℃.

**For C Users:**

**Step 2:** Change directory and edit.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/26_ds18b20/
    nano ds18b20.c

Find the following line, replace "28-00000495db35" with your
sensor address. Save and exit.

.. code-block::

    char* addr = "/sys/bus/w1/devices/28-00000495db35/w1_slave";

**Step 6:** Compile.

.. code-block::

    gcc ds18b20.c -lwiringPi

**Step 7:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 5:** Change directory and edit.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/
    nano 26_ds18b20.py

**Step 6:** Run.

.. code-block::

    sudo python3 26_ds18b20.py

Now, you can see the current temperature value displayed on the screen.

.. image:: media/image213.jpeg