Installing the OS
======================

In this chapter, we firstly learn to start up Raspberry Pi.
If your Raspberry Pi is set up, you can skip the chapter and go into the next chapter.

**Required Components**

* Any Raspberry Pi
* 1 * Mirco SD card
* 1 * Personal Computer	

**Step 1**

Raspberry Pi have developed a graphical SD card writing tool that works on Mac OS, Ubuntu 18.04 and Windows, and is the easiest option for most users as it will download the image and install it automatically to the SD card.
Visit the download page: https://www.raspberrypi.org/software/. Click on the link for the Raspberry Pi Imager that matches your operating system, when the download finishes, click it to launch the installer.

    .. image:: media/install_os1.png
        :align: center

**Step 2**

When you launch the installer, your operating system may try to block you from running it. For example, on Windows I receive the following message:
If this pops up, click on More info and then Run anyway, then follow the instructions to install the Raspberry Pi Imager.

    .. image:: media/install_os2.png
        :align: center

**Step 3**

Insert your SD card into the computer or laptop SD card slot.

**Step 4**

In the Raspberry Pi Imager, select the OS that you want to install and the SD card you would like to install it on.

    .. image:: media/install_os3.png
        :align: center

.. note::
    * You will need to be connected to the internet the first time.
    * That OS will then be stored for future offline use(lastdownload.cache, ``C:/Users/yourname/AppData/Local/Raspberry Pi/Imager/cache``). So the next time you open the software, it will have the display “Released: date, cached on your computer”.

**Step 5**

Select the SD card you are using.

    .. image:: media/install_os4.png
        :align: center

**Step 6**

Press **Ctrl+Shift+X** or click the **setting** icon to open the Advanced options page to enable SSH and set username and password.

.. note::

    * Now that the Raspberry Pi doesn’t have a default password, you will need to set it yourself. Also, the username can be changed.
    * For remote access, you will also need to enable SSH manually.

    .. image:: media/install_os5.png
        :align: center

Then scroll down to complete the wifi configuration and click SAVE.

.. note::
    Wi-Fi country should be set the two-letter ISO/IEC alpha2 code for the country in which you are using your Raspberry Pi, please refer to the following link: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements

    .. image:: media/install_os6.png
        :align: center

**Step 7**

Click the WRITE button.

    .. image:: media/install_os7.png
        :align: center

**Step 8**

If your SD card currently has any files on it, you may wish to back up these files first to prevent you from permanently losing them. If there is no file to be backed up, click Yes.

    .. image:: media/install_os8.png
        :align: center

**Step 9**

After waiting for a period of time, the following window will appear to represent the completion of writing.

    .. image:: media/install_os9.png
        :align: center