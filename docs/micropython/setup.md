# Getting Started

<figure markdown="span">
        <img src="https://i.pinimg.com/564x/c4/7b/dd/c47bdd27449f591145fbd5e925d95b84.jpg" 
             alt="LED Control" style="border-radius: 15px; height: 300px">
    </figure>

## What Do We Want to Do?
In this course, we will explore key principles of the Internet of Things (IoT) by developing an **automated plant monitoring and watering system**. Our goal is to create a smart irrigation solution using a microcontroller as the project’s core. In our system, a sensor will continuously measure soil humidity (and temperature) and send these readings via `MQTT` to a central server. There, the data can be processed and visualized using a browser-based dashboard, allowing you to monitor the plant’s status. Furthermore, you will be able to remotely set parameters - such as the optimal humidity level - and these settings will be transmitted back to the microcontroller to trigger a water pump when necessary.

*And let’s face it: not everyone is blessed with a natural green thumb. With this system, even if you have the gardening skills of a cactus 🌵, your plants will still thrive!*

## :material-hammer-wrench: And Therefore We Use...
While `Python` :fontawesome-brands-python: is typically associated with data analysis and software development on PCs, it can also be used to program microcontrollers. In this course, we leverage Python’s flexibility to develop firmware for embedded systems.

We are now in the realm of embedded systems. Embedded systems are essentially 'computers' :fontawesome-solid-computer: integrated into technical systems that combine electronic and often mechanical components. Unlike a typical PC, a microcontroller usually runs either without an operating system or with a highly specialized one, and always relies on firmware. The firmware is generally structured into three main components:

- **Bootloader:** Loads the operating system and the application software.
- **Operating System** (if present): Manages multitasking, memory, and file systems.
- **Application Software:** This is the code you write - in our case, using MicroPython.

### Software: MicroPython
Although the traditional approach for programming embedded systems is to use `C`, this method requires deep hardware knowledge and specialized expertise. Since our focus is on learning IoT concepts without getting lost in low-level programming, we will use MicroPython. MicroPython is a lean implementation of `Python 3`, written in `C` and optimized for microcontrollers. It compiles Python code to bytecode, which is then interpreted at runtime.

???+ tip "CircuitPython"
    For beginners, there’s also CircuitPython - a variant designed with an even friendlier interface - but for this course, we’ll stick with MicroPython.

### Hardware: ESP32

<figure markdown="span">
        <img src="https://www.az-delivery.de/cdn/shop/products/esp32-nodemcu-module-wlan-wifi-development-board-mit-cp2102-nachfolgermodell-zum-esp8266-kompatibel-mit-arduino-872375.jpg" 
             alt="ESP32" style="border-radius: 15px; height: 200px">
    </figure>


The ESP32 microcontroller is an ideal choice for IoT projects. It comes in various versions and supports wireless communication via Wi-Fi and Bluetooth, as well as wired interfaces like SPI, SDIO, I2C, and UART. Thanks to its power efficiency, robustness, and affordability (basic models are available for around €10), the ESP32 is well suited for a wide range of applications - from simple prototypes to complex systems. While other popular microcontrollers include Arduino, STM32, and Raspberry Pi, the ESP32 strikes a great balance between performance and cost for our smart plant watering project.

???+ question "Get Familiar with ESP32"

    Open the corresponding [ESP32 datasheet](https://cdn.shopify.com/s/files/1/1509/1638/files/ESP_-_32_NodeMCU_Developmentboard_Datenblatt_AZ-Delivery_Vertriebs_GmbH_10f68f6c-a9bb-49c6-a825-07979441739f.pdf?v=1598356497) and answer the following questions:

    - How many cores does the ESP32 have?
    - How much flash memory does the ESP32 have?
    - What kind of Bluetooth does the ESP32 support?
    - What are the electrical characteristics of the ESP32 (voltage, current, etc.)?
    

## Setting up our Project
Before we can start programming our ESP32, we need to prepare some tools and the hardware. 

### Firmware Upload

To be able to write code to the microcontroller, the MicroPython firmware must be loaded onto the ESP32. For this, we will use Thonny IDE - a friendly and intuitive Integrated Development Environment that simplifies the process of programming MicroPython on the ESP32.

Below are the step-by-step instructions:

1. **Download Thonny IDE:**  

    - Head over to [thonny.org](https://thonny.org) and download the IDE software appropriate for your operating system.
    - Install thonny by following the instructions. 

2. **Connect the ESP32:** 

    - Plug your ESP32 into your computer using a USB cable.
    - Note that the ESP32 will be detected as a **COM** port on Windows. To check, if the ESP32 is detected correctly, we look in the **Device Manager** under **Ports**. You should see something like this: 
    ![Device](../assets/micropython/cp210x.png)

    ???+ warning "CP210X Driver"
        If you cannot find the correct port, it might be because your PC or laptop does not have the necessary USB-to-UART driver installed. The chip responsible for the USB-to-UART conversion is usually a large, black, square component located next to the connector. If you shine a light on it, you should be able to read **CP2102** on the second line, indicating that the chip is manufactured by Silicon Labs. Since the driver is specific to the chip’s architecture, you can download the appropriate driver from [Silicon Labs USB-to-UART Bridge VCP Drivers](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads). 

        For Windows users, select the **CP210x VCP Windows** file, unzip the downloaded .zip file, and run the installer for your system architecture (x64 or x86). Once the driver is installed, the correct port should appear in your device manager.

3. **Install or Update the Firmware in Thonny:**  

    - Open Thonny IDE and go to **Tools > Options > Interpreter**. 
    - Select **MicroPython (ESP32)** from the interpreter options 
    - Select the correct **port** (see step before).
    - Click the **Install or update MicroPython (esptool)** button. 

    <div style="display: flex; justify-content: center;">
        <img src="/assets/micropython/thonny1.png" alt="Thonny" style="width: 45%">
    </div>

    A new window will open. Make the following selections:

    - **Target port:** USB to UART  
    - **MicroPython family:** ESP32  
    - **Variant:** Espressif ESP32 / WROOM  
    - **Version:** 1.24.1 (this is the latest version at the time of writing)

    <div style="display: flex; justify-content: center;">
        <img src="/assets/micropython/thonny2.png" alt="Thonny 2" style="width: 45%;">
    </div>

    After clicking on **Install** the firmware will be flashed onto the ESP32. :white_check_mark:

    ???+ info "Verify the Installation"

        - In Thonny, you can select the **Micropython (ESP32)** from the bottom right corner.
        - You should see a connection established in the shell at the bottom.  
        - Type `help()` and press Enter to check that the controller is responding correctly.
        <div style="display: flex; justify-content: center;">
            <img src="/assets/micropython/thonny3.png" alt="Thonny" style="width: 80%">
        </div>



Happy coding and welcome to the world of MicroPython :material-file-code:! 

---

### Prepare Visual Studio Code

Although you can program directly in Thonny, we've already explored Visual Studio Code - which offers advantages such as enhanced code completion and seamless GitHub integration. These features make VS Code a powerful option, especially for larger projects or collaborative work. If you need a refresher on how to set up VS Code, you can check out the [IDE Setup](../python-extensive/ide.md) section.


???+ warning "Install Node.js"
    Before continuing, ensure you have **`Node.js`** installed on your computer. `Node.js` is a cross-platform, open-source JavaScript runtime that lets you execute JavaScript code outside of a web browser.

    If you don't have it installed yet, please [download](https://nodejs.org/en/download) and install `Node.js`. During installation, it's highly recommended to tick the option to install any required additional programs. Once you proceed, a terminal window may open where you might need to confirm a few prompts. The installation process might take a few minutes; the terminal will close automatically when the installation is complete. Afterward, you should see `Node.js` listed among your installed programs.

    Once `Node.js` is successfully installed, you can move on to the next steps.
    <figure markdown="span">
        ![Node.js](../assets/micropython/notejs.png)
    </figure>
    

To run our code on the ESP32, we'll use the **`PyMakr` extension** in Visual Studio Code. This extension allows you to easily upload and execute your MicroPython scripts directly on the ESP32. We already covered how to install [extensions](../python-extensive/ide.md#extensions).

<figure markdown="span">
    ![Node.js](../assets/micropython/pymakr.png)
</figure>

After adding the extension, you should see `PyMakr` as a new button on the left-hand side of the VS Code window.

Now we are all set up and can start programming! :rocket:

---

## Blink :material-lightbulb-multiple-outline: | The Hello World of Embedded Systems

<figure markdown="span">
    ![blink](https://media.licdn.com/dms/image/v2/C5112AQGKuOV9YxRaFw/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1569298696507?e=2147483647&v=beta&t=Oi3Tk_iC7r4PA61xjhWRJvblYeMUcYs03Ta4elCS9eg)
</figure>

make led blink


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Was ist Micropython

Welche Tools verwenden wir?
Installation

Welche Hardware verwenden wir? 

Projekt setup


Take a look at the pinout chart of our `ESP32-WROOM-32` and make yourself familiar with the pins.

![Pinout](../assets/micropython/pinout.png)