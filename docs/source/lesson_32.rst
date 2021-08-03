Lesson 32 MPU6050 Gyro Acceleration Sensor
==========================================

**Introduction**

The MPU-6050 is the world’s first and only 6-axis motion tracking
devices designed for the low power, low cost, and high performance
requirements of smartphones, tablets and wearable sensors.

.. image:: media/image235.png
   :width: 1.79861in
   :height: 1.87014in

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* MPU-6050 module

- Several Jumper wires

**Experimental Principle**

In this experiment, use I2C to obtain the values of the three-axis
acceleration sensor and three-axis gyroscope for MPU6050 and display
them on the screen.

**Experimental Procedures**

**Step 1**: Build the circuit.

+-----------------------+---------------------+------------------------+
| **Raspberry Pi**      | **GPIO Extension    | **MPU-6050 Module**    |
|                       | Board**             |                        |
+-----------------------+---------------------+------------------------+
| **SCL**               | **SCL1**            | **SCL**                |
+-----------------------+---------------------+------------------------+
| **SDA**               | **SDA1**            | **SDA**                |
+-----------------------+---------------------+------------------------+
| **3.3V**              | **3V3**             | **VCC**                |
+-----------------------+---------------------+------------------------+
| **GND**               | **GND**             | **GND**                |
+-----------------------+---------------------+------------------------+

.. image:: media/image236.png
   :alt: C:\Users\Daisy\Desktop\Fritzing(英语)\32_MPU6050_bb.png32_MPU6050_bb
   :width: 6.56667in
   :height: 5.26806in

**Step 2**: Setup I2C (see Appendix. If you have set I2C, skip this
step.)

**For C Users:**

**Step 3:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/32_mpu6050/

**Step 4:** Compile.

.. code-block::

    gcc 32_mpu6050.c -lwiringPi -lm

**Step 5:** Run.

.. code-block::

    sudo ./a.out

**For Python Users:**

**Step 3:** Change directory.

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 4:** Run.

.. code-block::

    sudo python3 32_mpu6050.py

Now you can see the values of the acceleration sensor, gyroscope, and
XY-axis rotation read by MPU6050 printed on the screen constantly.

.. image:: media/image237.jpeg