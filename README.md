# ACPC Contest Grading System Simulator

A Python-based simulation of the ACPC (ACM Programming Contest) grading system that models the behavior of multiple computers processing programming submissions in a queue-based environment.

## Overview

This project simulates a contest grading system where:
- Multiple computers process tasks concurrently
- Tasks arrive following an exponential distribution
- Service times are exponentially distributed
- System performance metrics are collected and analyzed

## Features

- Multi-computer simulation using parallel processing
- Queue-based task management
- Real-time progress monitoring
- Statistical analysis of system performance
- Configurable parameters (number of computers, mean service time, etc.)

## Project Structure

- `main.py` - Main simulation controller
- `computer.py` - Task processing logic
- `queue_statistics.py` - Statistical calculations and analysis
- `task_generator.py` - Task generation and management
- `simulation_results.txt` - Output file with simulation results

## Requirements

- Python 3.6+
- multiprocessing
- random
- time
- datetime

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd acpc-grading-simulator
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the simulation:
```bash
python main.py
```

2. The simulation will:
   - Run for the specified duration (default: 1 minute)
   - Show progress updates every 10%
   - Generate a `simulation_results.txt` file with statistics

## Configuration

You can modify the following parameters in `main.py`:
- `NUM_COMPUTERS`: Number of parallel grading computers (default: 3)
- `MEAN_SERVICE_TIME`: Average time to grade a submission
- `MEAN_ARRIVAL_TIME`: Average time between submission arrivals
- `SIMULATION_HOURS`: Duration of the simulation

## Example Output

After running the simulation, `simulation_results.txt` will be generated with results similar to:

```
=== ACPC Grading System Simulation Results ===

Average Queue Length: 267.50
Average Waiting Time: 0.02 minutes
Average Completion Time: 0.15 minutes
```

Note: Actual values will vary with each simulation run.

## License

MIT License

Copyright (c) 2024 Jana Khadragy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
