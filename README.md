# Subnet Analysis and Visualization Tool

# barq-devops-subnet-task

## Prerequisites

- **Docker** (recommended) **OR**
- **Python 3.9+**

## Installation

### Method 1: Docker (Recommended)

#### Using Pre-built Image

Run the pre-built Docker image, mapping your data folder to the container:

```bash
docker run --rm -v "/path/to/your/data/folder:/app" mahmoudkamalaldeen/subnet_analyzer ip_data.xlsx
```

Example (if `input.xlsx` is in the current folder):

```bash
docker run --rm -v "$(pwd):/app" mahmoudkamalaldeen/subnet_analyzer ip_data.xlsx
```

#### Build Locally

### Clone the Repository

```bash
git clone https://github.com/MahmoudKamal01/barq-devops-subnet-task.git
cd barq-devops-subnet-task
```

Build the Docker image locally and run it:

```bash
docker build -t subnet_analyzer .
docker run --rm -v "$(pwd):/app" subnet_analyzer ip_data.xlsx
```

### Method 2: Local Execution

### Clone the Repository

```bash
git clone https://github.com/MahmoudKamal01/barq-devops-subnet-task.git
cd barq-devops-subnet-task
```

Install dependencies and run the tool locally:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# OR on Windows:
# venv\Scripts\activate

# Now install requirements
pip install -r requirements.txt

python subnet_analyzer.py ip_data.xlsx
python visualize.py

# Deactivate when done
deactivate
```

or you can try python3 if this did not work

```bash
python3 subnet_analyzer.py input.xlsx
python3 visualize.py
```

## Output Files

| File                 | Description                              |
| -------------------- | ---------------------------------------- |
| `subnet_report.json` | Detailed network analysis in JSON format |
| `network_plot.png`   | Visual representation of the network     |
