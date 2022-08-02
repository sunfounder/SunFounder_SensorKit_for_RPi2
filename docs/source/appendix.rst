Appendix: I2C Configuration
===========================

**Step 1**: Enable the I2C port of your Raspberry Pi (If you have
enabled it, skip this; if you do not know whether you have done that or
not, please continue):

.. raw:: html

    <run></run>

.. code-block::

    sudo raspi-config

**5 Interfacing options**

.. image:: media/image248.png

**P5 I2C**

.. image:: media/image249.png

**<Yes>**

.. image:: media/image250.png


**<Yes>**

.. image:: media/image251.png


**<Ok>**

.. image:: media/image252.png


**<Finish>**

.. image:: media/image253.png


**<Yes>** (If you do not see this page, continue to the next step)

.. image:: media/image254.png


**Step 2:** Check that the i2c modules are loaded and active:

.. raw:: html

    <run></run>

.. code-block::

    lsmod | grep i2c

Then the following code will appear (the number may be different).

.. code-block::

    i2c_dev                6276   0
    i2c_bcm2708                4121   0

**Step 3**: Install i2c-tools.

.. raw:: html

    <run></run>

.. code-block::

    sudo apt-get install i2c-tools

**Step 4**: Check the address of the I2C device:

.. raw:: html

    <run></run>

.. code-block::

    i2cdetect -y 1   # For Raspberry Pi 2 and higher version
    i2cdetect -y 0   # For Raspberry Pi 1

.. code-block::

    pi@raspberrypi ~ $ i2cdetect -y 1

         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f

    00:            -- -- -- -- -- -- -- -- -- -- -- -- --

    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

    40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- --

    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

    70: -- -- -- -- -- -- -- --

If there's an I2C device connected, the results will be similar as shown
above – since the address of the device is 0x48, 48 is printed.

**Step 5**:

**For C language users:** Install libi2c-dev.

.. raw:: html

    <run></run>

.. code-block::

    sudo apt-get install libi2c-dev

**For Python users:** Install smbus2 for I2C.

.. raw:: html

    <run></run>

.. code-block::

    sudo pip3 install smbus2

**Copyright Notice**

All contents including but not limited to texts, images, and code in
this manual are owned by the SunFounder Company. You should only use it
for personal study, investigation, enjoyment, or other non-commercial or
nonprofit purposes, under the related regulations and copyrights laws,
without infringing the legal rights of the author and relevant right
holders. For any individual or organization that uses these for
commercial profit without permission, the Company reserves the right to
take legal action.