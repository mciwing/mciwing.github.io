### MQTT

MQTT is an open network protocol for machine-to-machine communication that enables the transmission of messages between devices. MQTT works according to the publisher / subscriber principle, via a central broker. This can either be a local host or a cloud server. You can think of it like Instagram. The data sources report their data via a so-called ‘topic’ and everyone who is a subscriber to this ‘topic’ receives the data. The whole thing is not ‘real-time capable’, but is specialised for low bandwidth and high latency. The message itself is called ‘payload’ in MQTT and is not bound to a specific structure; JSON is often used (or converted into JSON). JSON (JavaScript Object Notation) is a compact data format in an easily readable text form for data exchange between applications and independent of programming languages. Don't worry, JSON is so widely used that there are online tools to properly convert all kinds of data and libraries to manage and convert JSON files.  

If you've never heard of MQTT before, it may sound a little confusing, but it's easier than you think and offers many advantages. This protocol is so common that you can create and run an MQTT server for free from providers such as HiveMQ (with certain restrictions on data volumes and number of subscribers). If you want to host locally, you can use Eclipse Mosquitto and use a microcontroller as a host, for example. Sometimes smaller data can also be saved and plotted via the brokers, which can be quite convenient. A database is of course recommended for large quantities of data. MQTT has the advantage that it has a star-shaped structure. This means that a central distributor in the centre can communicate with several actors and data can be written and read ‘at will’. Of course, it is possible to restrict how many and which rights a device that exchanges data has. Messages can also be encrypted using TLS (the standard security protocol for Internet communication).   


#### Connection to the MQTT-Broker


This link can be used as a guideline: https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

If you want to use your own MQTT server, you are welcome to do so. For example, you can use *HiveMQ*. This website allows you to run MQTT servers on their cloud via Amazon Web Service and is free of charge. You can register there and create a so-called cluster. It is best to follow the instructions on the website. At the end you will need credentials and then you can get started. This is already made available to you in the class. It is possible to run an MQTT server locally on a second microcontroller. You can use the Mosquitto Broker for this.

Of course, you also need an internet connection. Unfortunately, the Eduroam wifi is protected and cannot be connected to the controller. At the class, a router is used via which you can connect. At home, simply use your normal access data for the WLAN or create a hotspot. You will need a relatively large amount of code for the connection compared to what you have seen so far. A wifi and MQTT connection is a lot more complicated than just controlling a GPIO pin. Especially because the HiveMQ server is encrypted via TLS and it needs constant polling to make sure that data is sent and received in time. Please don't be alarmed, you don't need to understand everything. I will explain the most important sections, otherwise you can also copy the code into ChatGPT, the AI will be able to give you information about the programmes. The link above also explains a lot.      

This code sample should be copied into the *boot.py*:

xxxxx boot.py


At the top, as usual, are the libraries, including all but one standard library, more on this later. This is followed by all the access data for the WLAN and the MQTT server. Normally you should receive this information from your professor. If you create an MQTT server yourself, you will find information about the IP or URL on the website and you have to create a user with a password. Below you can see screenshots from the HiveMQ website for this data. In my configuration, the cluster URL is the server IP, ‘8883’ is the secure port, ‘hive_iot_server’ is the user I created and the corresponding password. It is important that my user has ‘PUBLISH-SUBSCRIBE’ as permission. With ‘PUBLISH-ONLY’ or ‘SUBSCRIBE-ONLY’ you can either only write to the server or read from the server. 

A unique ‘client_id’ is created in the programme, so that problems won`t occur if several users would try to use the same ID. Also 2 topics are created. One to which we publish and one to which we subscribe. Then some variables are initialised and a message is generated if the connection to the WLAN was successful. 

**VERY IMPORTANT!**: *boot.py* works in such a way that this code is automatically executed on a reboot (hard reboot). This means that as soon as the microcontroller is plugged in and receives power, this programme is executed and an attempt is made to establish a connection. If you want to see if the code is running, you have to unplug the controller and plug it in again or use the reboot button on the board! Even if you change something in the code of the ‘boot.py’ programme, you must perform a hard reboot so that the new code is loaded.  


This code sample should be copied into the *main.py*:


xxxxx main.py


Here we define some functions that are necessary for establishing the connection to the MQTT server and we check whether messages have arrived to which we are subscribed and which messages should be published. Some of you may have already noticed that we have the same non-standard library *robust* in both *boot.py* and *main.py*, from which we call a function. This library is explained below: (create a new file and name it *robust.py*)

xxxxx robust.py

This library processes MQTT connections and ensures that the interaction takes place smoothly. However, the programme uses another library called *simple.py*:

xxxxx simple.py

This is the most important library in Micropython for communicating with MQTT servers. It covers all the steps that occur when interacting with these servers and defines all the functions that are used. In line 68 (*import ussl*), a library is included if we want to connect with ssl. SSL is the standard technology for securing Internet connections by encrypting the data transmitted between a website and a browser (or between two servers). HiveMQ mainly operates via this network protocol. This is a standard library in Python, but not in Micropython. If you receive an error message in the console when executing the code that looks like this: *AttributeError: ‘bool’ object has no attribute ‘wrap_socket’*, the reason is that something is wrong with the SSL/TLS configuration. It is best to check all the user data again, that the port *8883* is being used (TLS port) and that this library is integrated somewhere. If an error message like this appears: *ImportError: no module named ‘ussl’*, then simply swap *import ussl* with *import ssl* and do the same with the function, i.e. ssl.wrap_socket instead of ussl.wrap_socket.  

Once you have placed all 4 programmes in your project folder and loaded everything onto the controller, you can reboot, but you will probably have to reconnect to Pymakr afterwards. You than may be able to see messages or status updates in your console. If not, reboot the console again with *‘ctrl’ + ‘d’*. If you want to check whether anything is arriving on the MQTT server, you can use *MQTT Explorer*: https://www.heise.de/download/product/mqtt-explorer/download. Simply log in there with the MQTT server data, then you can see what is happening on the server and whether your message is arriving. The message would be: ‘**hello** = Hello #3’, which is incremented by one every 5 seconds. You should then see the same line in your console. (Gif)


Of course, we want to be able to specify a humidity value at which irrigation is carried out. This means we would like to have a dashboard on which we can get information about the plant and set values. There are a few tools that offer this, one of which is MQTT-Tiles. We can connect the MQTT server there and thus have access to the data. We can also integrate a slider and retrieve its value using the *subscribe* function. The next programme you see below is again *main.py*, but this time rewritten so that the humidity sensor sends data to the MQTT server and the values from the slider are read out in MQTT tiles. Before that, a brief explanation of how to use and set up MQTT tiles:  


MQTT tiles (https://mqtttiles.flespi.io/#/) has a red *Connect* field at the top right. Click on it and then on the plus. (Image below as a reference for the following lines) You can enter a name at the top of the window and you can simply leave the *Client ID* as it is. For *Host* write *wss://* and then NOT!!!!! the normal TLS MQTT URL, but the TLS Websocket URL. I think this has to do with the fact that you are using a website here. But don't worry, the websocket URL is almost identical to the ‘normal’ URL. The MQTT URL normally ends with *.eu.provider.cloud:8883*, where 8883 is the port on which the data is transmitted. The websocket URL ends with *.eu.provider.cloud.8884/mqtt*. The provider's website normally contains all this information. If you do not create the server yourself, the data should be provided to you. You then only need to fill in *username* and *password*. 

Then click on *Update* and after a short load the name of the client should now appear in green at the top right and *online* below it. If this is the case, you can create a new board. Give the board a descriptive name such as *Test_board* or any other name. You can leave the *Sync alias* as it is. You do not necessarily need variables. You can simply enter a topic under *Init messages*. It is best to enter a meaningful name here, because the topic is the variable that is then used in the code to read the data. Therefore, you should still know in a fortnight what the value is that you get here. You can leave *Payload* blank. Then click on *Update & Open*. Now you can add a new widget. Let's start with a slider. Go to Slider under *Type*, give it a name and, most importantly, enter the correct one that you have previously created under *Topic*. You can enter a default value at which the slider will start during initialisation. You can also define the value range at the bottom. Simply click on *Save* and that should be it. You can check whether it has worked by looking at the server with MQTT Explorer. The slider value should now appear there and also change when you move the slider.  

Now you just have to change the variable *topic_sub* in your *boot.py* to the topic you have just created. If you now connect the humidity sensor and execute the code, you should see the humidity value in the console, the slider value and the humidity value has been published to the topic that is in the *boot.py*. If the slider value is changed, this should be updated both in the console and in the Explorer. Please note the following section before connecting the sensor:


If we now want to combine different programms and code parts, we have to keep certain things in mind, that could complicate out life or cause problems: 

The ESP32 has 2 types of ADC pins, ADC1 and ADC2. You will notice the difference as soon as you try to connect to the WiFi. This is because ADC2 pins are connected internally in the chip to the WiFi driver. This means that when using WiFi, the ADC2 pins will be overwritten and will not work. If this happens, you should receive an error message stating that you are initialising the pin incorrectly or that something went wrong with the ‘attenuation’, for example. Please take another look at the overview of pins at the very beginning and check that you are using one of the ADC1 pins. Also, please do not delete the *adc.atten* line from the code. The sensor needs 5V input voltage, which means the output signal will be between 0-5V. An ADC can only manage 0-3.6V and if you don't write anything, the default value is 1.1V, so it can happen that the values are read out incorrectly or not at all. With *adc.atten* you can throttle the voltage, otherwise you would have to use additional resistors to reduce the voltage manually. *ADC.ATTN_11DB* allows the ADC to use the entire range from 0-3.6V. You could use other value ranges with other specifications (0DB, 2_5DB or 6DB), depending on the sensor and the application. 

xxxxx py file

