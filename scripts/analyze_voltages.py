
import math

data = """
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
"""

lines = data.strip().split('\n')
parsed_data = []
for line in lines:
    parts = [p.strip() for p in line.split('|') if p.strip()]
    if len(parts) == 5:
        speed = float(parts[0])
        freq = float(parts[1])
        com = float(parts[2])
        sin_val = float(parts[3])
        cos_val = float(parts[4])
        parsed_data.append({'speed': speed, 'com': com, 'sin': sin_val, 'cos': cos_val})

print(f"Loaded {len(parsed_data)} data points.")

# Analyze Amplitude
amplitudes = []
angles = []
speeds = []

for d in parsed_data:
    sin_diff = d['sin'] - d['com']
    cos_diff = d['cos'] - d['com']
    amplitude = math.sqrt(sin_diff**2 + cos_diff**2)
    angle_rad = math.atan2(sin_diff, cos_diff)
    angle_deg = math.degrees(angle_rad)
    
    amplitudes.append(amplitude)
    angles.append(angle_deg)
    speeds.append(d['speed'])

avg_amp = sum(amplitudes) / len(amplitudes)
min_amp = min(amplitudes)
max_amp = max(amplitudes)
amp_variation = (max_amp - min_amp) / avg_amp * 100

print(f"Average Amplitude: {avg_amp:.2f}")
print(f"Amplitude Variation: {amp_variation:.2f}%")

# Analyze Angle vs Speed
# We expect a linear relationship: angle = m * speed + c
# Let's do a simple linear regression or just check the slope

# Unwrapping angles if necessary (though atan2 handles -pi to pi)
# Let's check if there are jumps.
unwrapped_angles = []
prev_angle = angles[0]
offset = 0
for a in angles:
    diff = a - prev_angle
    if diff > 180:
        offset -= 360
    elif diff < -180:
        offset += 360
    unwrapped_angles.append(a + offset)
    prev_angle = a

# Linear regression for Angle vs Speed
n = len(speeds)
sum_x = sum(speeds)
sum_y = sum(unwrapped_angles)
sum_xy = sum(x*y for x, y in zip(speeds, unwrapped_angles))
sum_xx = sum(x*x for x in speeds)

slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
intercept = (sum_y - slope * sum_x) / n

print(f"Angle vs Speed Linear Fit:")
print(f"Slope: {slope:.4f} degrees/km/h")
print(f"Intercept: {intercept:.4f} degrees")

# Calculate R-squared
y_mean = sum_y / n
ss_tot = sum((y - y_mean)**2 for y in unwrapped_angles)
ss_res = sum((y - (slope * x + intercept))**2 for x, y in zip(speeds, unwrapped_angles))
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared:.6f}")

# Check residuals
max_residual = 0
for x, y in zip(speeds, unwrapped_angles):
    pred = slope * x + intercept
    residual = abs(y - pred)
    if residual > max_residual:
        max_residual = residual

print(f"Max Residual: {max_residual:.4f} degrees")

print("\nAmplitude vs Speed:")
for s, a in zip(speeds, amplitudes):
    print(f"Speed: {s}, Amplitude: {a:.2f}")


