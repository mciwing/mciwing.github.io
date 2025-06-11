# Plant Watering System 🌱

<figure markdown="span">
    <img src="/assets/micropython/dashboard1.png" alt="dashboard" style="width: 80%; border-radius: 15px;">
</figure>

Now that all components are working - the moisture sensor, the pump control, and the MQTT communication and a basic dashboard - it's time to bring everything together into a fully automated plant watering system.

## Final System

???+ question "Task: Plant Watering System"
    It's time to all your knowledge together and build a plant watering system with the following features:

    - Measure the soil moisture and show it in the dashboard with a gauge.
    - The threshold for the pump is controlled by a slider in the dashboard.
    - Automatic mode: Once the moisture is below the threshold, the pump is turned on for 5 seconds. after that wait for 10 seconds to measure again.
    - Manual mode: There is a possibility to manually trigger the pump for 5 seconds.

So far we have build everything we asked for. But you can do more if you want to. The following section includes some optional topics to think about and to extend your system to become a more sophisticated plant watering system.

## Optional: Watering Strategy

Now that your system is able to water plants, the key question becomes: **how much water is needed**, and **what are good threshold values for different types of plants and environments**? Here are some ideas to optimize your system.

### Recommended Moisture Thresholds by Plant Type

| **Plant Type**      | **Moisture Threshold** | **Notes**                                                               |
| ------------------- | -------------------------- | ----------------------------------------------------------------------- |
| Succulents & Cacti  | 10–30%                     | Let soil dry completely between waterings                               |
| Medium-water Plants | 30–50%                     | e.g. pothos, spider plants; let top soil dry                            |
| Tropical Plants     | 50–70%                     | e.g. ferns, peace lilies; maintain consistent moisture, avoid sogginess |
| Herbs & Edibles     | 40–60%                     | Prefer moist, well-drained soil                                         |
| Flowering Plants    | 40–70%                     | e.g. violets, begonias; avoid extreme wet/dry cycles                    |


### Adjusting Thresholds Based on Environment

* **Light:** In bright, sunny spots, increase moisture thresholds by **5–10%** to compensate for faster drying.
* **Humidity:** In high-humidity rooms, decrease thresholds by **5–10%** to avoid overwatering.
* **Soil Type:**

    * **Sandy soil:** drains quickly → use **lower thresholds**
    * **Clay soil:** retains water → use **higher thresholds**


### How Much Water to Dispense?

Here are some recommentations for the amount of water to dispense based on AI:

| **Plant Size**         | **Recommended Water Volume** |
| ---------------------- | ---------------------------- |
| Small pots (<15 cm)    | 100–200 ml                   |
| Medium pots (15–30 cm) | 250–500 ml                   |
| Large pots (>30 cm)    | 500–1000 ml                  |

???+ tip "Tip"
    **Note:** Our pump delivers approximately **30 ml per second**.
    To determine how long to run the pump, adjust the `pump_on_time` based on your desired volume.