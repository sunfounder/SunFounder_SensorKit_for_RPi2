Appendix: I2C Configuration
===========================

**Step 1**: Enable the I2C port of your Raspberry Pi (If you have
enabled it, skip this; if you do not know whether you have done that or
not, please continue):

.. code-block::

    sudo raspi-config

**5 Interfacing options**

.. image:: media/image248.png
   :width: 6.03333in
   :height: 3.36806in

**P5 I2C**

.. image:: media/image249.png
   :width: 6.05069in
   :height: 3.51528in

**<Yes>**

.. image:: media/image250.png
   :width: 600

**<Yes>**

.. image:: media/image251.png
   :width: 600

**<Ok>**

.. image:: media/image252.png
   :width: 600

**<Finish>**

.. image:: media/image253.png
   :width: 600

**<Yes>** (If you do not see this page, continue to the next step)

.. image:: media/image254.png
   :width: 600

**Step 2:** Check that the i2c modules are loaded and active:

.. code-block::

    lsmod | grep i2c

Then the following code will appear (the number may be different).

.. code-block::

    i2c_dev                6276   0
    i2c_bcm2708                4121   0

**Step 3**: Install i2c-tools.

.. code-block::

    sudo apt-get install i2c-tools

**Step 4**: Check the address of the I2C device:

.. code-block::

    i2cdetect -y 1   # For Raspberry Pi 2 and higher version
    i2cdetect -y 0   # For Raspberry Pi 1

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

.. code-block::

    sudo apt-get install libi2c-dev

**For Python users:** Install smbus for I2C.

.. code-block::

    sudo apt-get install python3-smbus

**Copyright Notice**

All contents including but not limited to texts, images, and code in
this manual are owned by the SunFounder Company. You should only use it
for personal study, investigation, enjoyment, or other non-commercial or
nonprofit purposes, under the related regulations and copyrights laws,
without infringing the legal rights of the author and relevant right
holders. For any individual or organization that uses these for
commercial profit without permission, the Company reserves the right to
take legal action.

.. |image1| image:: media/image3.png
   :width: 0.34792in
   :height: 0.33472in
.. |image2| image:: media/image4.png
   :width: 0.34236in
   :height: 0.33403in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Dual Color LED.pngDual Color LED| image:: media/image5.png
   :width: 1.5in
   :height: 1.19931in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\RGB LED.pngRGB LED| image:: media/image6.png
   :width: 1.5in
   :height: 1.23403in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Auto Flash LED.pngAuto Flash LED| image:: media/image7.png
   :width: 1.46597in
   :height: 1.20486in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Relay Module.pngRelay Module| image:: media/image8.png
   :width: 2.41597in
   :height: 1.2in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Laser Emitter.pngLaser Emitter| image:: media/image9.png
   :width: 1.78472in
   :height: 1.29722in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Button.pngButton| image:: media/image10.png
   :width: 1.60694in
   :height: 1.19514in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Tilt Swich.pngTilt Swich| image:: media/image11.png
   :width: 1.46458in
   :height: 1.23403in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Vibration Switch.pngVibration Switch| image:: media/image12.png
   :width: 1.52292in
   :height: 1.29444in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\IR Receiver.pngIR Receiver| image:: media/image13.png
   :width: 1.56042in
   :height: 1.29444in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Active Buzzer.pngActive Buzzer| image:: media/image14.png
   :width: 1.70694in
   :height: 1.35139in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Passive Buzzer.pngPassive Buzzer| image:: media/image15.png
   :width: 1.84236in
   :height: 1.44097in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Reed Switch.pngReed Switch| image:: media/image16.png
   :width: 1.48958in
   :height: 1.28611in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Photo-interrupter.pngPhoto-interrupter| image:: media/image17.png
   :width: 1.69306in
   :height: 1.35in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\AD-DA Converter.pngAD-DA Converter| image:: media/image18.png
   :width: 1.56528in
   :height: 1.34514in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Raindrop Sensor.pngRaindrop Sensor| image:: media/image19.png
   :width: 1.34375in
   :height: 0.9125in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Raindrop Sensor - .pngRaindrop Sensor -| image:: media/image20.png
   :width: 1.77847in
   :height: 1.14583in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Joystick PS2.pngJoystick PS2| image:: media/image21.png
   :width: 1.66528in
   :height: 1.03819in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Potentiometer.pngPotentiometer| image:: media/image22.png
   :width: 1.63472in
   :height: 1.39792in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Analog Hall Sensor.pngAnalog Hall Sensor| image:: media/image23.png
   :width: 1.57847in
   :height: 1.3375in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Hall Switch.pngHall Switch| image:: media/image24.png
   :width: 1.60486in
   :height: 1.31597in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Analog Temperature Sensor.pngAnalog Temperature Sensor| image:: media/image25.png
   :width: 1.69444in
   :height: 1.35069in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Thermistor.pngThermistor| image:: media/image26.png
   :width: 1.74306in
   :height: 1.35208in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Sound Sensor.pngSound Sensor| image:: media/image27.png
   :width: 1.68194in
   :height: 1.4625in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Photoresistor.pngPhotoresistor| image:: media/image28.png
   :width: 1.67431in
   :height: 1.34306in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Flame Sensor.pngFlame Sensor| image:: media/image29.png
   :width: 1.88681in
   :height: 1.35903in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Gas Sensor.pngGas Sensor| image:: media/image30.png
   :width: 2.42431in
   :height: 1.25in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Remote Control.pngRemote Control| image:: media/image31.png
   :width: 2.68194in
   :height: 1.35833in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Touch Switch.pngTouch Switch| image:: media/image32.png
   :width: 1.575in
   :height: 1.30625in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Ultrasonic.pngUltrasonic| image:: media/image33.png
   :width: 2.35347in
   :height: 1.39444in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Temperature sensor.pngTemperature sensor| image:: media/image34.png
   :width: 1.75486in
   :height: 1.35069in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\_Rotary Encoder.png_Rotary Encoder| image:: media/image35.png
   :width: 1.73681in
   :height: 1.35625in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Humiture Sensor.pngHumiture Sensor| image:: media/image36.png
   :width: 1.66806in
   :height: 1.3875in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\IR Obstacle Module.pngIR Obstacle Module| image:: media/image37.png
   :width: 2.39097in
   :height: 1.46667in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\LCD 1602.pngLCD 1602| image:: media/image38.png
   :width: 2.97917in
   :height: 1.35347in
.. |IMG_256| image:: media/image39.jpeg
   :width: 1.75069in
   :height: 1.41944in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\MPU6050 Module.pngMPU6050 Module| image:: media/image40.png
   :width: 1.46736in
   :height: 1.52569in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\RTC-DS1302 Module.pngRTC-DS1302 Module| image:: media/image41.png
   :width: 1.91597in
   :height: 1.55208in
.. |C:\Users\sunfounder\Desktop\sensor pisd 抠图\Tracking Sensor.pngTracking Sensor| image:: media/image42.png
   :width: 2.63889in
   :height: 1.02847in
.. |\_MG_7704_副本.jpg| image:: media/image43.jpeg
   :width: 2.82292in
   :height: 1.7625in
.. |D:\Raspberry Pi\图片\_MG_6473.jpg| image:: media/image44.jpeg
   :width: 2.47639in
   :height: 2.11042in
.. |image3| image:: media/image45.png
   :width: 3.07083in
   :height: 0.84375in
.. |F:\SunFounder\Kit\Sensor Kit for Rpi2\图2015-7-3\2015-7-3\小零件 裁剪\_MG_0601.JPG| image:: media/image46.jpeg
   :width: 1.80972in
   :height: 1.64167in
.. |F:\SunFounder\Kit\Sensor Kit for Rpi2\图2015-7-3\2015-7-3\小零件 裁剪\_MG_9999.JPG| image:: media/image47.jpeg
   :width: 2.09167in
   :height: 1.78889in
.. |F:\SunFounder\Kit\Sensor Kit for Rpi2\图2015-7-3\2015-7-3\小零件 裁剪\_MG_9996.JPG| image:: media/image48.jpeg
   :width: 2.45278in
   :height: 1.66181in
.. |F:\SunFounder\Kit\Sensor Kit for Rpi2\图2015-7-3\2015-7-3\小零件 裁剪\_MG_0002.JPG| image:: media/image49.jpeg
   :width: 2.18542in
   :height: 1.81111in
.. |image4| image:: media/image50.jpeg
   :width: 2.61944in
   :height: 1.5875in
.. |C:\Users\Administrator\Desktop\树莓派全部文档 2.18\_MG_7478.png| image:: media/image51.png
   :width: 2.62083in
   :height: 1.65972in
.. |微信截图_20200628104259| image:: media/image64.png
   :width: 7.09375in
   :height: 4.69792in
.. |微信截图_20200628104336| image:: media/image65.png
   :width: 7.11458in
   :height: 4.70833in
.. |\_MG_2263| image:: media/image118.jpeg
   :width: 6.37153in
   :height: 4.55208in
.. |\_MG_2212| image:: media/image122.jpeg
   :width: 5.50556in
   :height: 4.66944in
.. |\_MG_2218| image:: media/image126.jpeg
   :width: 6.175in
   :height: 4.66528in
.. |image5| image:: media/image127.png
   :width: 1.49722in
   :height: 1.27292in
.. |image6| image:: media/image134.png
   :width: 1.77361in
   :height: 1.40417in
.. |image7| image:: media/image135.png
   :width: 1.87917in
   :height: 1.46944in
.. |image8| image:: media/image145.png
   :width: 1.66458in
   :height: 1.34375in
.. |image9| image:: media/image155.png
   :width: 1.59306in
   :height: 1.14236in
.. |image10| image:: media/image156.png
   :width: 1.91111in
   :height: 1.23125in
.. |image11| image:: media/image168.png
   :width: 1.56042in
   :height: 1.34375in
.. |image12| image:: media/image169.png
   :width: 1.71944in
   :height: 1.36528in
.. |image13| image:: media/image177.png
   :width: 1.56875in
   :height: 1.22083in
.. |image14| image:: media/image178.png
   :width: 1.47569in
   :height: 1.07431in
.. |image15| image:: media/image193.png
   :width: 1.84167in
   :height: 1.32639in
.. |C:\Users\Administrator\Desktop\remote.png| image:: media/image201.png
   :width: 2.07431in
   :height: 1.95972in
.. |image16| image:: media/image210.png
   :width: 1.72708in
   :height: 1.36597in
.. |\_MG_2367| image:: media/image234.jpeg
   :width: 5.66181in
   :height: 4.32431in
