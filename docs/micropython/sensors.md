# Reading a Sensor

![World](https://media.licdn.com/dms/image/v2/C5612AQHKLg3fNkWLJQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1520091098663?e=2147483647&v=beta&t=2dvFrck3PWzXl1GB9j3borIeDNdTm9eVCmhXFmWOG2U)

Now that we’ve successfully written and run our first blink program, it’s time to dive into the real heart of our project: reading data from a sensor. In this section, you’ll learn how to wire a sensor to your ESP32, read its output with MicroPython, and process the results in code.

## Practical Guideline

### Organizing Your Code

Whenever you sync your PyMakr project, **all** files in that folder are pushed to the ESP32. As we go along in this course, 
you’ll accumulate many scripts - blink tests, sensor readers, utilities, etc. - but you only want to deploy what’s actually in use. To keep things clean:

1. **Maintain a "script library"** on your PC:

    ```hl_lines="1"
    📁 script_collection/
        ├── 📄 blinking_led_main.py
        ├── 📄 sos_blinking_main.py
        ├── 📄 read_sensor_main.py
        └── 📄 ...
    ```

2. **Keep your active project separate**:

    ```hl_lines="1"
    📁 esp_project/
        ├── 📄 main.py
        ├── 📄 boot.py
        └── 📄 pymakr.conf
    ```

3. **Deploy only what you need:** Once you have finished a task and want to start a new one, copy the scripts you’re working on (in the `esp_project` folder) into the `script_collection` folder.

By giving each file a clear, descriptive name and only syncing the files in `esp_project/`, you’ll prevent accidental pin overlaps, minimize memory usage and make it trivial to swap in new routines (just overwrite `main.py`)


### Pin Types

When working with microcontrollers, knowing **which pin to use** and **how** is one of the most important things you need to know. Pins are the connections between the microcontroller and the outside world. Usually the first thing you do is to look at the [pinout](https://cdn.shopify.com/s/files/1/1509/1638/files/AZ281_A_18-10_DE_B08BTWJGFX_e699c448-ffc6-4744-8b93-5c9f102d22b0.pdf?v=1721128839) of the microcontroller and see which pins are available. A typical microcontroller has between 6 and 60 pins. Each microcontroller (sometimes different models of the 'same' controller) have different configurations. Pins often have multiple functions. This is called **pin multiplexing**.

![ESP32 Pinout](../assets/micropython/pinout2.png)


???+ tip "Pinout"
    Each microcontroller has pin names specific to its hardware or architecture. This means that controllers from different manufacturers may use different designations. 
    Common manufacturers of microcontrollers for IoT applications are Espressif, Arduino and Raspberry Pi. The advantage over noname controllers is that there are always data sheets (see 'ESP32_datasheet') with exact pin assignment. 
    So it's better to spend 10€ on a good µC instead of buying one from an unknown manufacturer for 2€ and then the pins don't match!


There are different types of pins which can use to interface with the outside world. The most common ones are:

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

---

By following these practical organization guidelines so far and using the pinout diagram above, you’ll wire up sensors and actuators correctly, write clear code, and keep your ESP32 project’s filesystem neat and efficient.
Happy tinkering!

## Reading a Sensor

Now it's time to move forward with our project to keep our plant alive. The first step is to measure the soil moisture: is it too dry or too wet? 

### How can we measure soil moisture?
#### Theory

There are two common types of sensors used to measure soil moisture: **resistive** and **capacitive** sensors. Both are generally referred to as **hygrometers**.

**Resistive moisture sensors** work by placing a hygroscopic (water-attracting) material between two conductive electrodes. This material is typically a non-conductive polymer that becomes increasingly conductive as it absorbs water. The change in conductivity alters the voltage between the electrodes, which can then be measured.
These sensors offer a large surface area, making them effective for detecting small moisture variations—even in already damp environments. However, their performance drops at very low moisture levels.
A major drawback for our use case is **durability**. Since resistive sensors require direct contact with moisture in the soil, they are prone to corrosion. In particular, cheap resistive sensors can suffer from **electrolysis**, where the sensor material begins to degrade and potentially release **toxic substances** into the soil — harmful for plants and unsuitable for long-term use.

**Capacitive moisture sensors**, on the other hand, rely on a capacitor-like structure whose electrical field is affected by the moisture content of the surrounding soil. As soil moisture increases, so does the soil's dielectric constant, which alters the sensor’s capacitance.
These sensors do not require direct water contact — hence the black protective coating — and are much more **durable** and **maintenance-free**, as corrosion is not an issue. Capacitive sensors are typically more **accurate**, **reliable**, and **resistant to wear and temperature fluctuations**. For these reasons, they are often used in professional applications like agriculture, despite being slightly more expensive.

#### Hardware

For our project we’ll be using the **HW-390 capacitive moisture sensor**, a widely available and cost-effective sensor with a simple 3-wire interface. While different manufacturers may offer this model, its functionality and wiring remain consistent across versions.

<figure markdown="span">
![HW-390](https://cdn-reichelt.de/bilder/web/artikel_ws/A300%2FDEBO_CAP_SENS_1.jpg)
</figure>


#### Wiring
The HW-390 sensor has three pins:

- VCC – Connect to 5V on the ESP32
- GND – Connect to GND
- AOUT – Connect to any analog-capable GPIO

For our project we will use GPIO27 as input pin for the sensor value. The wiring diagram is shown below. Connect all components as shown. 

<figure markdown="span">
    ![Blink](../assets/micropython/sensor_Steckplatine.png)
</figure>

Now we are all set up and we can start coding!

### Coding

As with our first program, we only need to edit the `main.py` file. We begin by importing the required libraries:

```python
from machine import ADC
from time import sleep
```

This time, instead of importing only the `Pin` class, we're also using the `ADC` class from the `machine` module to enable analog-to-digital conversion. You can find the official MicroPython documentation for the ESP32 [here](https://docs.micropython.org/en/latest/esp32/quickref.html#adc-analog-to-digital-conversion).


Next, we initialize the `ADC` class:

```python
adc_pin = Pin(27)
adc = ADC(adc_pin)
```
We can now read values from the sensor using the `read_u16()` method. The `u16` refers to an unsigned 16-bit integer, meaning the returned value will be in the range 0–65535.


```python
val16 = adc.read_u16()
print('ADC Value: ', val16)
```

If you run this code while the sensor is on your desk, you’ll get a value roughly like this:

```
ADC Value:  48139
```















xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


This pin must be initialised, here as a 12-bit ADC. This means that the values we get from the sensor will be between 0-4095. We then set the input voltage range of the ADC between 0-3.6V, which should be sufficient for the sensor. Now we have to be careful here! With a capacitive humidity sensor, a low value (=low voltage) means more humidity. This means 0V -> value = 0 -> 100% humidity and conversely the value 4095 = 0% humidity. Therefore, when calculating the percentage, it must me computed by 1 minus the value. **IMPORTANT: Always consider what the value of an ADC means and what appears to make sense. You often have to read out the ADC values of sensors indirectly!**

---








```python linenums="1" title="main.py"
from machine import ADC
from time import sleep

# Set GPIO 27 as ADC pin
adc_pin = Pin(27)
adc = ADC(adc_pin)

# Function to read moisture level
def read_moisture():

    # Read the analog value from the sensor
    # The ADC value is 16-bit, the range is 0-65535
    val16 = adc.read_u16()
    
    # Map it to a percentage value (0-100%)
    moisture_percentage = 100 - ((val16 / 65535) * 100)
    
    # Return both the percentage and the raw value
    return moisture_percentage, val16

while True:

    # Read the moisture level
    percentage, val16 = read_moisture()

    # Print the results to the console
    print("************** READING MOISTURE LEVEL ************** ")
    print("Percentage: \t \t{:.2f}%".format(percentage))
    print("Value in 16-bit: \t{}".format(val16))    

    # Delay for 1 second before reading again
    sleep(1)
```

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

https://docs.micropython.org/en/latest/esp32/quickref.html#adc-analog-to-digital-conversion



sensor lesen einmal

kalibrieren mit min max






Some libraries used in the programmes are underlined when you load them into VSCode. This happens if the libraries cannot be found on your computer. Please do NOT download these libraries! These libraries are specially made for microcontrollers and will not run on your computer. Unfortunately, this makes working a little more difficult as you cannot always recognise where errors occur as the code is interpreted on the controller. Use the console, you might find hints there, some possible problems are already covered here. This is a disadvantage when working with Python or Micropython. In C, the code must be compiled beforehand. In most cases, you will receive error messages and can correct the code before it ends up on the controller. With Python, the code is uploaded as it is and than only interpreted and executed on the device. Keep this in mind in case of complications.



https://www.berrybase.at/analoger-kapazitiver-bodenfeuchtesensor


Aufgabe: Wenn Feuchtigkeit unter 30% --> LED an










This is code to read the moisture sensor:

from machine import ADC, Pin
import time

# Set up ADC (Analog to Digital Converter)
# Connect the sensor to GPIO 34 (ADC1 channel 6)
sensor_pin = 27
adc = ADC(Pin(sensor_pin))

# Configure the ADC resolution (12-bit)
adc.width(ADC.WIDTH_12BIT)  # ADC width (0-4095)

# Set ADC attenuation (optional depending on voltage range)
# Use ADC.ATTN_11DB for input voltage range 0 to 3.6V
adc.atten(ADC.ATTN_11DB)

def read_moisture():
    # Read the analog value from the sensor
    moisture_value = adc.read()
    
    # Optionally, map it to a percentage value (0-100%)
    moisture_percentage = 100 - ((moisture_value / 4095.0) * 100)
    
    return moisture_value, moisture_percentage

while True:
    value, percentage = read_moisture()
    print("Moisture Value: ", value)
    print("Moisture Percentage: {:.2f}%".format(percentage))
    
    # Delay for 1 second before reading again
    time.sleep(1)

The sensor has 3 pins: GND, VCC and AUOT. These are Ground, Voltage Input and Analogue Output. Ground should be connected to Ground on the controller, VCC to 5V and for the output you can use any ADC, I used pin G27. This pin must be initialised, here as a 12-bit ADC. This means that the values we get from the sensor will be between 0-4095. We then set the input voltage range of the ADC between 0-3.6V, which should be sufficient for the sensor. Now we have to be careful here! With a capacitive humidity sensor, a low value (=low voltage) means more humidity. This means 0V -> value = 0 -> 100% humidity and conversely the value 4095 = 0% humidity. Therefore, when calculating the percentage, it must me computed by 1 minus the value. **IMPORTANT: Always consider what the value of an ADC means and what appears to make sense. You often have to read out the ADC values of sensors indirectly!**

Weiterer Sensor

To get a feel for the different sensors, you can also plug them in and try them out. There is also a BME280, a sensor for temperature, air pressure and humidity and a rain sensor module that can be used to measure the amount of precipitation, including snow. The code for the rain sensor looks relatively similar to that of the humidity sensor. This is because most sensors are based on similar principles. Either an ADC is read out or, as with the BME, communication takes place via I2C. I2C is a serial data bus, i.e. a data connection that allows the controller to interact with the sensor. This means that several data can be sent and read out at the same time without having to be interpreted. The data is therefore only assigned variables in the code and does not have to be calculated depending on the bit resolution, as is the case with the ADC.

As explained above, the BME280 works with I2C, which requires a library that must be loaded onto the controller with the actual programme:
(For all libraries that you need, the name that is used in the other programmes is stored in the first line of the programme. This is the name with which you should save the programme. You can also use other names. However, you must then also change these in the other parts of the code in which the libraries are called).


The Code for reading out the sensor is quite compact and looks lilke this:


The rain sensor has an analogue and a digital output. Depending on which signal you want, the respective pin must be connected. This also changes the code slightly. The AO (analogue output) outputs an analogue signal between 0V and 5V, similar to the humidity sensor. The code would be almost identical. With DO (Digital Output), the signal is converted by the hardware and output directly, similar to the BME280, but without using I2C.

