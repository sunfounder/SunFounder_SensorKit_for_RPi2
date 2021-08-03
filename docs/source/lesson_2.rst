Lesson 2 RGB LED Module
=======================

**Introduction**

RGB LED modules can emit various colors of light. Three LEDs of red,
green, and blue are packaged into a transparent or semitransparent
plastic shell with four pins led out. The three primary colors of red,
green, and blue can be mixed and compose all kinds of colors by
brightness, so you can make an RGB LED emit colorful light by
controlling the circuit.

.. image:: media/image100.png
   :width: 1.74861in
   :height: 1.43889in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- Several Jumper wires

- 1 \* RGB LED module

- 1 \* 4-Pin anti-reverse cable

**Experimental Principle**

In this experiment, we will use PWM technology to control the brightness
of RGB.

Pulse Width Modulation, or PWM, is a technique for getting analog
results with digital means. Digital control is used to create a square
wave, a signal switched between on and off. This on-off pattern can
simulate voltages in between full on (5 Volts) and off (0 Volts) by
changing the portion of the time the signal spends on versus the time
that the signal spends off. The duration of "on time" is called the
pulse width. To get varying analog values, you change, or modulate, that
pulse width. If you repeat this on-off pattern fast enough with an LED
for example, the result is as if the signal is a steady voltage between
0 and 5v controlling the brightness of the LED.

.. image:: media/image101.png
   :width: 3.92083in
   :height: 2.46875in

We can see from the top oscillogram that the amplitude of DC voltage
output is 5V. However, the actual voltage output is only 3.75V through
PWM, for the high level only takes up 75% of the total voltage within a
period.

Here are the three basic parameters of PWM:

.. image:: media/image102.png
   :width: 5.55208in
   :height: 3.12431in

1. The term **duty cycle** describes the proportion of "on" time to the
regular interval or "period" of time

2. **Period** describes the reciprocal of pulses in one second.

3. The voltage amplitude here is 0V-5V.

Here we input any value between 0 and 255 to the three pins of the RGB
LED to make it display different colors.

RGB LEDs can be categorized into common anode LED and common cathode
LED. In this experiment, we use a common cathode RGB LED.

The schematic diagram of the module is as shown below:

.. image:: media/image103.png
   :width: 4.53611in
   :height: 2.33056in

**Experimental Procedures**

**Step 1:** Build the circuit according to the following method.

+-----------------------+----------------------+----------------------+
| **Raspberry Pi**      | **GPIO Extension     | **RGB LED Module**   |
|                       | Board**              |                      |
+-----------------------+----------------------+----------------------+
| **3.3V**              | **3V3**              | **VCC**              |
+-----------------------+----------------------+----------------------+
| **GPIO0**             | **GPIO17**           | **R**                |
+-----------------------+----------------------+----------------------+
| **GPIO1**             | **GPIO18**           | **G**                |
+-----------------------+----------------------+----------------------+
| **GPIO2**             | **GPIO27**           | **B**                |
+-----------------------+----------------------+----------------------+

.. image:: media/image104.png
   :alt: 02_RGB_LED_bb
   :width: 5.31458in
   :height: 5.09722in

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/02_rgb_led/

**Step 3:** Compile.

.. code-block::

    gcc rgb_led.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 02_rgb_led.py

You will see the RGB LED light up, and display different colors in turn.

.. image:: media/image105.jpeg
   :width: 700