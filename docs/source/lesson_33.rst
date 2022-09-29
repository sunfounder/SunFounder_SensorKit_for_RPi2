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
   :width: 200

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

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/SunFounder_SensorKit_for_RPi2/C/33_ds1302/

**Step 3:** Compile:

.. raw:: html

    <run></run>

.. code-block::

    gcc rtc_ds1302.c -lwiringPi -lwiringPiDev

.. note::

    If it does not work after running, or there is an error prompt ``wiringPi.h: No such file or directory``, please refer to :ref:`install_wiringpi` to install it.

**Step 4:** Set up time by:

.. raw:: html

    <run></run>

.. code-block::

    sudo ./a.out -sdsc

Set year, month, date as YYYYMMDD

Set hour, minute, second as HHMMSS(24-hour clock)

Set weekday (0 as Sunday)

**Step 5:** Run:

.. raw:: html

    <run></run>

.. code-block::

    sudo ./a.out


**Code**

.. code-block:: c

    #include <stdio.h>
    #include <stdlib.h>
    #include <stdint.h>
    #include <string.h>
    #include <time.h>

    #include <wiringPi.h>
    #include <ds1302.h>

    // Register defines

    #define	RTC_SECS	 0
    #define	RTC_MINS	 1
    #define	RTC_HOURS	 2
    #define	RTC_DATE	 3
    #define	RTC_MONTH	 4
    #define	RTC_DAY		 5
    #define	RTC_YEAR	 6
    #define	RTC_WP		 7
    #define	RTC_TC		 8
    #define	RTC_BM		31

    static unsigned int masks [] = { 0x7F, 0x7F, 0x3F, 0x3F, 0x1F, 0x07, 0xFF } ;

    // bcdToD: dToBCD:
    static int bcdToD (unsigned int byte, unsigned int mask)
    {
    unsigned int b1, b2 ;
    byte &= mask ;
    b1 = byte & 0x0F ;
    b2 = ((byte >> 4) & 0x0F) * 10 ;
    return b1 + b2 ;
    }

    static unsigned int dToBcd (unsigned int byte)
    {
    byte = byte % 100;
    return ((byte / 10) << 4) + (byte % 10) ;
    }

    // ramTest:
    static int ramTestValues [] =
    { 0x00, 0xFF, 0xAA, 0x55, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x00, 0xF0, 0x0F, -1 } ;

    static int ramTest (void)
    {
    int addr ;
    int got ;
    int i = 0 ;
    int errors = 0 ;
    int testVal ;

    printf ("DS1302 RAM TEST\n") ;

    testVal = ramTestValues [i] ;

    while (testVal != -1)
    {
        for (addr = 0 ; addr < 31 ; ++addr)
        ds1302ramWrite (addr, testVal) ;

        for (addr = 0 ; addr < 31 ; ++addr)
        if ((got = ds1302ramRead (addr)) != testVal)
        {
        printf ("DS1302 RAM Failure: Address: %2d, Expected: 0x%02X, Got: 0x%02X\n",
            addr, testVal, got) ;
        ++errors ;
        }
        testVal = ramTestValues [++i] ;
    }

    for (addr = 0 ; addr < 31 ; ++addr)
        ds1302ramWrite (addr, addr) ;

    for (addr = 0 ; addr < 31 ; ++addr)
        if ((got = ds1302ramRead (addr)) != addr)
        {
        printf ("DS1302 RAM Failure: Address: %2d, Expected: 0x%02X, Got: 0x%02X\n",
            addr, addr, got) ;
        ++errors ;
        }

    if (errors == 0)
        printf ("-- DS1302 RAM TEST: OK\n") ;
    else
        printf ("-- DS1302 RAM TEST FAILURE. %d errors.\n", errors) ;

    return 0 ;
    }

    // setLinuxClock:
    static int setLinuxClock (void)
    {
    char dateTime [20] ;
    char command [64] ;
    int  clock [8] ;


    printf ("Setting the Linux Clock from the DS1302... ") ; fflush (stdout) ;

    ds1302clockRead (clock) ;

    // [MMDDhhmm[[CC]YY][.ss]]

    sprintf (dateTime, "%02d%02d%02d%02d%02d%02d.%02d",
        bcdToD (clock [RTC_MONTH], masks [RTC_MONTH]),
        bcdToD (clock [RTC_DATE],  masks [RTC_DATE]),
        bcdToD (clock [RTC_HOURS], masks [RTC_HOURS]),
        bcdToD (clock [RTC_MINS],  masks [RTC_MINS]),
        20,
        bcdToD (clock [RTC_YEAR],  masks [RTC_YEAR]),
        bcdToD (clock [RTC_SECS],  masks [RTC_SECS])) ;

    sprintf (command, "/bin/date %s", dateTime) ;
    system (command) ;

    return 0 ;
    }

    // setDSclock:
    static int setDSclock (void)
    {
    struct tm t ;
    time_t now ;
    int clock [8] ;
    int time = 0 ;
    int date = 0 ;
    int weekday = 0 ;

    printf ("Setting the clock in the DS1302 from type in... ") ;

    printf ("\n\nEnter Date(YYYYMMDD): ") ;
    scanf ("%d", &date) ;
    printf ("Enter time(HHMMSS, 24-hour clock): ") ;
    scanf ("%d", &time) ;
    printf ("Enter Weekday(0 as sunday): ") ;
    scanf ("%d", &weekday) ;
    //  printf("\ndate: %d,  time: %d\n\n", date, time) ;

    clock [ 0] = dToBcd (time % 100) ;	// seconds
    clock [ 1] = dToBcd (time / 100 % 100) ;	// mins
    clock [ 2] = dToBcd (time / 100 / 100) ;	// hours
    clock [ 3] = dToBcd (date % 100) ;	// date
    clock [ 4] = dToBcd (date / 100 % 100) ;	// months 0-11 --> 1-12
    clock [ 5] = dToBcd (weekday) ;	// weekdays (sun 0)
    clock [ 6] = dToBcd (date / 100 / 100) ;       // years
    clock [ 7] = 0 ;			// W-Protect off

    ds1302clockWrite (clock) ;

    printf ("OK\n") ;

    return 0 ;
    }

    int main (int argc, char *argv [])
    {
    int i ;
    int clock [8] ;
    int year ;
    int month ;
    int date ;
    int hour ;
    int minute ;
    int second ;
    int weekday ;

    wiringPiSetup () ;
    ds1302setup   (4, 5, 6) ;

    if (argc == 2)
    {
        /**/ if (strcmp (argv [1], "-slc") == 0)
        return setLinuxClock () ;
        else if (strcmp (argv [1], "-sdsc") == 0)
        return setDSclock () ;
        else if (strcmp (argv [1], "-rtest") == 0)
        return ramTest () ;
        else
        {
        printf ("Usage: ds1302 [-slc | -sdsc | -rtest]\n") ;
        return EXIT_FAILURE ;
        }
    }

    for (i = 0 ;; ++i)
    {
        printf ("%5d:  ", i) ;

        ds1302clockRead (clock) ;
        
        hour   = bcdToD (clock [2], masks [2]) ;
        minute = bcdToD (clock [1], masks [1]) ;
        second = bcdToD (clock [0], masks [0]) ;

        date  = bcdToD (clock [3], masks [3]) ;
        month = bcdToD (clock [4], masks [4]) ;
        year  = bcdToD (clock [6], masks [6]) + 2000 ;
        weekday = bcdToD (clock [5], masks [5]) ;

        printf ("  %04d-%02d-%02d", year, month, date) ;
        printf ("  %02d:%02d:%02d", hour, minute, second) ;
        
        switch (weekday){
        case 0: printf ("  SUN") ; break;
        case 1: printf ("  MON") ; break;
        case 2: printf ("  TUE") ; break;
        case 3: printf ("  WED") ; break;
        case 4: printf ("  THU") ; break;
        case 5: printf ("  FRI") ; break;
        case 6: printf ("  SAT") ; break;
        }

        printf ("\n") ;

        delay (200) ;
    }
    return 0 ;
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

    sudo python3 33_ds1302.py

**Code**

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from datetime import datetime
    from ds1302 import DS1302
    from sys import version_info
    import time

    if version_info.major == 2:
        input = raw_input

    rtc = DS1302()

    def setup():
        print ('')
        print ('')
        print (rtc.get_datetime())
        print ('')
        print ('')
        a = input( "Do you want to setup date and time?(y/n) ")
        if a == 'y' or a == 'Y':
            date = input("Input date:(YYYY MM DD) ")
            time = input("Input time:(HH MM SS) ")
            date = list(map(lambda x: int(x), date.split()))
            time = list(map(lambda x: int(x), time.split()))
            print ('')
            print ('')
            rtc.set_datetime(datetime(date[0], date[1], date[2], time[0], time[1], time[2]))
            dt = rtc.get_datetime()
            print ("You set the date and time to:", dt)

    def loop():
        while True:
            a = rtc.get_datetime()
            print (a)
            time.sleep(0.5)

    def destory():
        pass				# Release resource

    if __name__ == '__main__':		# Program start from here
        setup()
        try:
            loop()
        except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            destory()

Now you can see the time on the screen.

.. image:: media/image241.jpeg