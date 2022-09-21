Libraries
===========

Two important libraries are used in programming with Raspberry Pi, and
they are wiringPi and RPi.GPIO. The Raspberry Pi OS image of Raspberry
Pi installs them by default, so you can use them directly.

RPi.GPIO
------------

If you are a Python user, you can program GPIOs with API provided by
RPi.GPIO.

RPi.GPIO is a module to control Raspberry Pi GPIO channels. This package
provides a class to control the GPIO on a Raspberry Pi. For examples and
documents, visit
http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/

Test whether RPi.GPIO is installed or not, type in python:

.. raw:: html

    <run></run>

.. code-block::

    python

.. image:: media/image89.png
    :align: center
    :width: 800

In Python CLI, input \"import RPi.GPIO\", If no error prompts, it means
RPi.GPIO is installed.

.. raw:: html

    <run></run>

.. code-block::

    import RPi.GPIO

.. image:: media/image90.png
    :align: center
    :width: 800

If you want to quit python CLI, type in:

.. raw:: html

    <run></run>

.. code-block::

    exit()

.. image:: media/image91.png
    :align: center

WiringPi 
------------

``wiringPi`` is a C language GPIO library applied to the Raspberry Pi. It complies with GUN Lv3. The functions in wiringPi are
similar to those in the wiring system of Arduino. They enable the users
familiar with Arduino to use wiringPi more easily.

``wiringPi`` includes lots of GPIO commands which enable you to control all
kinds of interfaces on Raspberry Pi. 

Please run the following command to install ``wiringPi`` library.

.. raw:: html

   <run></run>

.. code-block::

    sudo apt-get update
    git clone https://github.com/WiringPi/WiringPi
    cd WiringPi 
    ./build

You can test whether the wiringPi
library is installed successfully or not by the following instruction.


.. raw:: html

    <run></run>

.. code-block::

    gpio -v

.. image:: media/image92.png


Check the GPIO with the following command:


.. raw:: html

    <run></run>

.. code-block::

    gpio readall

.. image:: media/image93.png
    :align: center
    :alt: 图片2

For more details about wiringPi, you can refer to `WiringPi <https://github.com/WiringPi/WiringPi>`_.


