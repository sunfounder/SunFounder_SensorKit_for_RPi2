Lesson 33 RTC DS1302
====================

**Introduction**

DS1302 is a trickle charging clock chip, launched by DALLAS in America.
With a built-in real-time clock/calendar and a 31-byte static RAM, it
can communicate with MCU through simple serial interfaces. The real-time
clock/calendar circuit provides information about second, minute, hour,
day, week, month, and year. DS1302 can automatically adjust the number
of days per month and days in leap year. You can determine to use a
24-hour or 12-hour system by AM/PM selection.

.. image:: media/image238.png
   :width: 2.78194in
   :height: 2.35417in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* DS1302 RTC module

- 1 \* 5-Pin anti-reverse cable

**Experimental Principle**

Interfacing the DS1302 with a microprocessor is simplified by using
synchronous serial communication. Only three wires are required to
communicate with the clock/RAM: RST, serial data (SDA) and serial clock
(SCL). SDA can be transferred to and from the clock/RAM one byte at a
time or in a burst of up to 31 bytes.

After the time of the DS1302 is set manually, the MCU starts to read the
accurate time and date returned by DS1302.

The schematic diagram of the module is as shown below:

.. image:: media/image239.png
   :width: 6.81458in
   :height: 4.96389in

**Experimental Procedures**

**Step 1:** Build the circuit.

+-----------------------+---------------------+------------------------+
| **Raspberry Pi**      | **GPIO Extension    | **RTC DS1302 Module**  |
|                       | Board**             |                        |
+-----------------------+---------------------+------------------------+
| **GPIO4**             | **GPIO23**          | **SCL**                |
+-----------------------+---------------------+------------------------+
| **GPIO5**             | **GPIO24**          | **I/O or SDA**         |
+-----------------------+---------------------+------------------------+
| **GPIO6**             | **GPIO25**          | **RST**                |
+-----------------------+---------------------+------------------------+
| **3.3V**              | **3V3**             | **VCC**                |
+-----------------------+---------------------+------------------------+
| **GND**               | **GND**             | **GND**                |
+-----------------------+---------------------+------------------------+

.. image:: media/image240.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\33_DS1302_bb.png33_DS1302_bb
   :width: 5.825in
   :height: 5.64306in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/33_ds1302/

**Step 3:** Compile:

.. code-block::

    gcc rtc_ds1302.c -lwiringPi -lwiringPiDev

**Step 4:** Set up time by:

.. code-block::

    sudo ./a.out -sdsc

Set year, month, date as YYYYMMDD

Set hour, minute, second as HHMMSS(24-hour clock)

Set weekday (0 as Sunday)

**Step 5:** Run:

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 33_ds1302.py

Now you can see the time on the screen.

.. image:: media/image241.jpeg