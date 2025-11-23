# Mapping of Static Coil Voltages to Speed Reading

The speedometer uses an analog servo motor to control the needle.
This table shows the required voltages of each terminal to ground for a list of shown velocities.
| Speed [km/h] | Input Frequency [Hz] | COM [mV] | SIN [mV] | COS [mV] |
| ------------ | -------------------- | -------- | -------- | -------- |
| 0            |                      | 4260     |          |          |
| 20           | 18                   | 4260     | 3297     | 5775     |
| 30           | 30                   | 4260     | 2390     | 6162     |
| 40           | 41                   | 4260     | 1969     | 5780     |
| 50           | 52                   | 4260     | 1679     | 5311     |
| 60           | 63                   | 4260     | 1489     | 4792     |
| 70           | 74                   | 4260     | 1407     | 4276     |
| 80           | 84                   | 4260     | 1419     | 3828     |
| 90           | 95                   | 4260     | 1529     | 3330     |
| 100          | 107                  | 4260     | 1755     | 2815     |
| 110          | 120                  | 4260     | 2105     | 2333     |
| 120          | 131                  | 4260     | 2494     | 1971     |
| 130          | 143                  | 4260     | 2975     | 1680     |
| 140          | 154                  | 4260     | 3452     | 1506     |
| 150          | 165                  | 4260     | 3977     | 1418     |
| 160          | 175                  | 4260     | 4447     | 1431     |
| 170          | 186                  | 4260     | 5000     | 1546     |
| 180          | 197                  | 4260     | 5527     | 1793     |
| 190          | 207                  | 4260     | 5933     | 2085     |
| 200          | 217                  | 4260     | 6267     | 2437     |
| 210          | 228                  | 4260     | 6584     | 2922     |
| 220          | 238                  | 4260     | 6744     | 3325     |
| 230          | 249                  | 4260     | 6846     | 3820     |
| 240          | 258                  | 4260     | 6847     | 4228     |
| 250          | 268                  | 4260     | 6816     | 4679     |
| 260          | 278                  | 4260     | 6681     | 5136     |

## Analysis

The measurements appear valid. The relationship between the angle of the voltage vector and the speed is highly linear ($R^2 \approx 0.9998$).

The amplitude of the vector ($A = \sqrt{(V_{sin}-V_{com})^2 + (V_{cos}-V_{com})^2}$) is approximately constant around 2800 mV for speeds above 30 km/h.

### Formulas

Based on the data, the voltages can be approximated by:

$$
V_{com} = 4260 \text{ mV}
$$

$$
V_{sin}(v) = V_{com} + A \cdot \sin(\theta(v))
$$

$$
V_{cos}(v) = V_{com} + A \cdot \cos(\theta(v))
$$

Where:
- $v$ is the speed in km/h.
- $A \approx 2800 \text{ mV}$ (Amplitude).
- $\theta(v)$ is the angle in degrees:
  $$ \theta(v) \approx -1.07 \cdot v - 13.5 $$

(Note: Convert $\theta$ to radians for calculation: $\theta_{rad} = \theta_{deg} \cdot \frac{\pi}{180}$)
