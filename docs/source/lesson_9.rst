Lesson 9 IR Receiver Module
===========================

**Introduction**

An infrared-receiver (as shown below) is a component which receives
infrared signals and can independently receive infrared rays and output
signals compatible with TTL level. It is similar with a normal
plastic-packaged transistor in size and is suitable for all kinds of
infrared remote control and infrared transmission.

.. image:: media/image13.png
   :width: 200

**Required Components**

- 1 \* Raspberry Pi

- 1 \* Breadboard

- 1 \* IR receiver module

- 1 \* IR Remote Controller

- 1 \* 3-Pin anti-reverse cable

**Experimental Principle**

In this experiment, send signals to IR receiver by pressing buttons on
the IR remote controller. The counter will add 1 every time it receives
signals; in other words, the increased number indicates IR signals are
received.

The schematic diagram of the module is as shown below:

.. image:: media/image131.png
   :width: 500

**Experimental Procedures**

**Step 1:** Build the circuit.

+-----------------------+----------------------+----------------------+
| **Raspberry Pi**      | **GPIO Extension     | **IR Receiver        |
|                       | Board**              | Module**             |
+-----------------------+----------------------+----------------------+
| **GPIO0**             | **GPIO17**           | **SIG**              |
+-----------------------+----------------------+----------------------+
| **3.3V**              | **3V3**              | **VCC**              |
+-----------------------+----------------------+----------------------+
| **GND**               | **GND**              | **GND**              |
+-----------------------+----------------------+----------------------+

.. image:: media/image132.png
   :width: 5.67292in
   :height: 5.01042in

**For C Users:**

**Step 2:** Change directory.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/09_ir_receiver/

**Step 3:** Compile.

.. raw:: html

    <run></run>

.. code-block::

    gcc ir_receiver.c -lwiringPi

**Step 4:** Run.

.. raw:: html

    <run></run>

.. code-block::

    sudo ./a.out

.. note::

   If it does not work after running, or there is an error prompt: \"wiringPi.h: No such file or directory\", please refer to :ref:`C code is not working?`.

**Code**

.. code-block:: c

    #include <wiringPi.h>
    #include <stdio.h>

    #define    IR    0

    int cnt = 0;

    void myISR(void)
    {
        printf("Received infrared. cnt = %d\n", ++cnt);	
    }

    int main(void)
    {
        if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
            printf("setup wiringPi failed !");
            return 1; 
        }
        
        if(wiringPiISR(IR, INT_EDGE_FALLING, &myISR) == -1){
            printf("setup ISR failed !");
            return 1;
        }

        //pinMode(IR, INPUT);

        while(1);
        
        return 0;
    }

**For Python Users:**

**Step 2:** Change directory.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/Python/

**Step 3:** Run.

.. raw:: html

    <run></run>

.. code-block::

    sudo python3 09_ir_receiver.py

**Code**

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    import RPi.GPIO as GPIO

    IrPin  = 11
    count = 0

    def setup():
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        GPIO.setup(IrPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def cnt(ev=None):
        global count
        count += 1
        print ('Received infrared. cnt = ', count)

    def loop():
        GPIO.add_event_detect(IrPin, GPIO.FALLING, callback=cnt) # wait for falling
        while True:
            pass   # Don't do anything

    def destroy():
        GPIO.cleanup()                     # Release resource

    if __name__ == '__main__':     # Program start from here
        setup()
        try:
            loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            destroy()

Press any key of the remote. Then you can see the LED on the module
blinking, and \"Received infrared. cnt = xxx\" printed on the screen.
\"xxx\" means the time you pressed the key(s).

.. image:: media/image133.jpeg
   :alt: \_MG_2421
   :width: 6.72569in
   :height: 5.05347in
