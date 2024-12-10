# Randomized Multithreading Dashboard
A Python-based multithreaded dashboard using Tkinter that displays dynamically updating random numbers. Each label operates within its own number range and refresh interval, demonstrating the power of Python's threading module to handle asynchronous updates without freezing the user interface.

## Key Features
~ Asynchronous Updates: Utilizes multithreading to ensure smooth updates for all labels concurrently.

~ Customizable Display: Each label has a unique color, range, and refresh rate for random number generation.

~ User-Friendly Design: Intuitive layout with visually distinct labels to highlight individual settings.

## Installation Guide
Clone the repository:
```bash
    git clone https://github.com/your-username/randomized-multithreading-dashboard.git
```
Navigate to the project directory:
```bash
   cd randomized-multithreading-dashboard
```
Run the Python script:
```bash
   python dashboard.py
```
## How It Works
This application uses the Tkinter library for creating a graphical user interface and the threading module for parallel updates. Each label in the dashboard:

- Displays a random number that updates dynamically.
- Operates on its own thread, ensuring seamless updates without GUI freezing.
- Has configurable properties like range, refresh interval, and background color.
  
### Dashboard Overview
The dashboard includes six labels with unique configurations:

|Range            | Refresh Time (s) | Background Color |
|-----------------|------------------|------------------|
| 1 to 50         | 20               | aquamarine       |
| -20 to 20       | 17               | coral            |
| -200 to -50     | 6                | khaki            |
| 10 to 30        | 28               | skyblue          |
| -70 to 70       | 10               | plum             |
| 50 to 300       | 9                | lightgreen       |

## Customization
You can modify the label configurations by editing the configurations list inside the setup_dashboard function in dashboard.py:
```python
configurations = [
    (1, 50, 20, "aquamarine"),
    (-20, 20, 17, "coral"),
    (-200, -50, 6, "khaki"),
    (10, 30, 28, "skyblue"),
    (-70, 70, 10, "plum"),
    (50, 300, 9, "lightgreen")
]
```

# Output Example
Below is an example screenshot of the application in action:
![image](https://github.com/user-attachments/assets/022c5b70-cc70-4449-92cb-3e47453cbc72)

Each label updates independently, ensuring that the dashboard remains responsive and visually appealing.
