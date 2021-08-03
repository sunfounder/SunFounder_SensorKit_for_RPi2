Lesson 29 IR Obstacle Avoidance Module
========================================

**Introduction**

An IR obstacle avoidance module (as shown below) is used in this Lesson.

.. image:: media/image224.png
   :width: 2.86319in
   :height: 1.75694in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* IR Obstacle module

- 1 \* 3-Pin anti-reverse cable

**Experimental Principle**

An obstacle avoidance sensor mainly consists of an infrared-transmitter,
an infrared-receiver and a potentiometer. According to the reflecting
feature of an object, if there is no obstacle, emitted infrared ray will
weaken with the propagation distance and finally disappear. If there is
an obstacle, when infrared ray encounters an obstacle, it will be
reflected back to the infrared-receiver. Then the infrared-receiver
detects this signal and confirms an obstacle exists ahead.

.. note:: 
    The detection distance of the infrared sensor is adjustable - you may adjust it by the potentiometer.

The schematic diagram of the module is as shown below:

.. image:: media/image225.png
   :width: 6.40625in
   :height: 4.08819in

**Experimental Procedures**

**Step 1:** Build the circuit.

.. image:: media/image226.png
   :width: 600

**For C Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/30_ir_obstacle/

**Step 3:** Compile.

.. code-block::

    gcc ir_obstacle.c -lwiringPi

**Step 4:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 2:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. code-block::

    sudo python3 30_ir_obstacle.py

Now, if there is an obstacle ahead, a string “Detected Barrier!” will be
printed on the screen.

.. image:: media/image227.jpeg