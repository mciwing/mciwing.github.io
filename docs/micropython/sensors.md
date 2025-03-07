I would recommend that you create a separate folder in which you can save all programmes. All programmes in the Pymakr Project will also be loaded onto the microcontroller. There will be various sensors and test programmes that you can and should use for the project. You will not always need all of them at the same time and you should only load onto the controller what you actually use. Otherwise it will only become cluttered and you could possibly have problems with pin assignments, inputs and outputs or computing power. While working on the project, you can simply copy the required programmes and libraries and load them into your Pymakr workspace. This should make your work a little easier and better structured.

It is best to always give the programmes self-explanatory names so that you still know what the code does later. If you want to use the programme on the controller, simply copy the code into the main.py programme of the microcontroller, the same for boot.py if you need it. For additional libraries, copy the entire programme into the Pymakr folder and make sure you name it correctly.

Some libraries used in the programmes are underlined when you load them into VSCode. This happens if the libraries cannot be found on your computer. Please do NOT download these libraries! These libraries are specially made for microcontrollers and will not run on your computer. Unfortunately, this makes working a little more difficult as you cannot always recognise where errors occur as the code is interpreted on the controller. Use the console, you might find hints there, some possible problems are already covered here. This is a disadvantage when working with Python or Micropython. In C, the code must be compiled beforehand. In most cases, you will receive error messages and can correct the code before it ends up on the controller. With Python, the code is uploaded as it is and than only interpreted and executed on the device. Keep this in mind in case of complications.



https://www.berrybase.at/analoger-kapazitiver-bodenfeuchtesensor


Aufgabe: Wenn Feuchtigkeit unter 30% --> LED an

???+ info "GPIO Insights"
    A **GPIO (General Purpose Input/Output)** is a digital pin on a microcontroller or processor that can be freely configured as an **input** or **output** through programming. By default, GPIOs are unassigned and can be controlled in a binary manner (`HIGH` or `LOW`).  

    GPIOs typically operate at **3.3V** and can supply **2-16 mA** of current, making them suitable for driving components like LEDs. For example, if a GPIO pin is set to **HIGH**, the LED turns **on**; when set to **LOW**, the LED turns **off**. GPIOs are fundamental for interfacing with sensors, actuators, and other peripherals in embedded systems.


To find out which pin is which, you can look at the [pinout](https://cdn.shopify.com/s/files/1/1509/1638/files/ESP-32_NodeMCU_Developmentboard_Pinout.pdf?v=1609851295) chart:

![Pinout](../assets/micropython/pinout.png)



### Pins

A typical microcontroller has between 6 and 60 pins to which power, input and output, or communication connections are connected. Each microcontroller (sometimes different models of the ‘same’ controller) have different configurations. Pins often have multiple functions. This is called **pin multiplexing**.

In addition, each microcontroller has pin names specific to its hardware or architecture. This means that controllers from different manufacturers may use different designations. Common manufacturers of microcontrollers for IoT applications are Espressif, Arduino and Raspberry Pi. The advantage over noname controllers is that there are always data sheets (see ‘ESP32_datasheet’) with exact pin assignment. 
So it's better to spend €10 on a good µC instead of buying one from Alibaba for €2 and then the pins don't match!
The picture above shows the ‘ESP32 NodeMCU Module WLAN WiFi Development Board | Dev Kit C V2’ with its pins.

### GPIO / PWM

A GPIO or General Purpose Input/Output is a general digital pin whose behaviour can be freely determined by logical programming. They are unassigned by default. GPIOs operate from 2-16 mA and 3.3 V and can be read and switched in binary form. For example, a LED can be controlled via a GPIO. The pin is set to ‘HIGH’ and the LED lights up. If the GPIO pin is set back to ‘LOW’, the LED goes out. But what if you want to dim the LED? This requires a PWM signal!

PWM is the so-called pulse width modulation. It is basically a square wave function that oscillates between two different voltage levels. In principle, the signal is switched on and off very quickly. The ratio between switch-on time and switch-off time can vary and forms the duty cycle. A PWM signal is suitable as a control or measurement signal, for data transmission or for driving a load with variable voltage. For our dimmed LED, this means that we have to specify a frequency and a resolution (1 - 16 bits). 8 bits means that the voltage (normally 3.3V) is divided between 0 and 255. In concrete terms, 0 is 0V (LED off) and 255 is 3.3V (LED on). If you cycle through a function from 0 - 255, the LED starts switched off and becomes brighter and brighter until it reaches maximum brightness. The frequency indicates how fast a cycle is.

1. **Power Pins**
    - **VCC / VIN / 5V / 3.3V / 3V3**
        - **What they do:** These pins supply power from the controller to the sensors.
        - **Common names:** VCC (Voltage Common Collector), VIN (Voltage In), 3.3V or 3V3 is the voltage level. Means this Pin provides 3.3 Volt.
        - **Where to connect:** Connect the VCC / VIN Pin on a sensor with the RIGHT! voltage on the controller.
        - **Why it´s important:** This pin powers the setup. It´s important to look into the Datasheet of the sensors before connecting, to insure the right voltage is used. If you use 5V for a 3.3V sensor you could damage it, the other way round the sensor may not work, because it´s undersupplied. Controllers can have different amounts of voltage pins, but in terms of voltage value 3.3V and 5V are standart.  
    
    - **GND (Ground)**
        - **What it does:** Acts as a common reference point for electrical cicuits. Voltage needs a start and endpoint. Going from 0V to 5V is the same as from 10V to 15V. It´s just the difference in the potential. Therefore you need the ground as the reference. 
        - **Common names:** GND, Ground, sometimes represented by a symbol (⏚).
        - **Where to connect:** Always connect ground to ground, normally the controller has more than one GND pin.
        - **Why it´s important:** Completes the circuit by providing a return path for the current, and closes it. Without ground, circuits won´t work.

2. **GPIO Pins**
    - **General-Purpose Input/Output**    
        - **What they do:** They can be programmed as either inputs or outputs, making them very versatile.
        - **Common names:** GPIO1, GPIO2,... or G1, G2,..., sometimes D0, D1 or Digital. GPIOs can do a bit more than normal digital pins and are the most common digital pin, thats why they get a separate category.
        - **Where to connect:** Connect to components that can act as input (buttons) or output (LED)
        - **Why it´s important:** GPIOs are multipurpose pins used for connecting a variety of components, enabling the microcontroller to interact with the external world. They can serve as digital pins, and some even support PWM (discussed below). 

3. **Digital Pins**
    - **Digital I/O Pins**
        - **What they do:** Can read or write digital (on/off) signals. 
        - **Common names:** Labeled D0, D1,... DO for Digital Ouput, DI for Digital Input. 
        - **Where to connect:** Use the digital pins for devices that only need on/off states, like buttons, LED or digital sensors.
        - **Why it´s important:** These help control and read digital components. On most Microcontrollers you will find GPIOs, so use those. 
    
    - **PWM (Pulse Width Modulation) Pins**
        - **What they do:** Provide a  "fake" analog output by rapidly switching between on and off states, creating varying voltages. Where also discussed in the beginning.
        - **Common names:** PWM, sometimes indicated with a ~ symbol.
        - **Where to connect:** Useful for components needing variable control, like dimmable LEDs, motor speed controllers, or servos.
        - **Why it´s important:** Allows for smoother interactions and variing controls, like speed and brightness. With a Digital I/O you have on/off, with PWM you have on/off and everything in between.

4. **Analog Pins**
    - **Analog Input Pins / ADC (Analog to Digital Converter)**
        - **What they do:** Measure varying voltage levels, enabling the microcontroller to read sensor data (e.g., temperature, light, humidity). 
        - **Common names:** A0, A1,... AO for Analog Output, AI for Analog Input, ADC_1, ADC_2.
        - **Where to connect:** Connect sensor with analog pins and varying voltages, such as temperature or potentiometers.
        - **Why it´s important:** These pins let microcontrollers interpret environmental data beyond just on/off values, allowing for more complex sensing capabilities. We will use these for some of the sensors. Normally indicated by the Library: 'import ADC'

5. **Communication Pins**
    - **UART (TX/RX) - Serial Communication**
        - **What they do:** Transmit (TX) and receive (RX) data for serial communication.
        - **Common names:** TX (Transmit), RX (Receive), often located next to each other.
        - **Where to connect:** Connect TX of one device to RX of another and vice versa.
        - **Why it´s important:** Used to communicate with other microcontrollers, computers, or external modules like GPS and Bluetooth. It’s crucial for data exchange between devices. When you connect the Microcontroller to your PC or Laptop, Pymakr will say USB to UART Bridge, because we internally use UART to communicate with the controller. That´s also why we need the driver software, it translates from USB to UART. 

    - **I2C (SDA/SCL) - Internal-Integrated Circuit**
        - **What they do:** Allow communication with multiple sensors or modules using only two pins. 
        - **Common names:** SDA (Serial Data) and SCL (Serial Clock).
        - **Where to connect:** SDA to SDA and SCL to SCL
        - **Why it´s important:** Commonly used for modules like OLED displays, temperature sensors, and accelerometers. Saves space by connecting multiple devices with just two wires, making it simpler to connect sensors and displays.

    - **SPI (MOSI, MISO, SCK, SS) - Serial Peripheral Interface**
        - **What they do:** Fast communication protocol typically for higher-speed components (e.g., SD cards, displays). 
        - **Common names:**  MOSI (Master Out Slave In), MISO (Master In Slave Out), SCK (Serial Clock), SS (Slave Select).
        - **Where to connect:** SPI devices connect to their corresponding pins on the microcontroller.
        - **Why it´s important:** Allows for high-speed communication with components that require a lot of data, like displays and storage.


|**Pin Type**|**Common Labels**|**Purpose**|**Common Use Cases**|
|---|---|---|---|
|Power|VCC, VIN, 3.3V, 5V|Provides power to the board/sensors|Power for sensors/modules|
|Ground|GND (⏚)|Returns current to complete the circuit|Essential for all connections|
|GPIO|GPIO, D0, G0, etc.|General-purpose input/output|Flexible pin for input/output|
|Digital I/O|D0, D1, D2...|Reads/writes digital states|Buttons, LEDs, simple sensors|
|PWM|~ or PWM|Provides variable control (analog output)|Dim LEDs, control motors|
|Analog Input|A0, A1, ADC1|Reads varying voltages|Temperature, light, humidity sensors|
|Serial (UART)|TX/RX|Basic data communication|GPS, Bluetooth modules, PC-µC connection|
|I2C|SDA, SCL|Multi-device communication with 2 wires|OLED displays, accelerometers|
|SPI|MOSI, MISO, SCK, SS|High-speed communication|SD cards, TFT displays|