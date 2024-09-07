# TV Leds

## Prerequisites
- Python 3.x
- `pip` (Python package manager)

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/TxFig/TV-Leds.git
    cd your-repo
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the script with elevated permissions**:
    ```bash
    sudo ./venv/bin/python main.py
    ```

    Note: Ensure you are in the root directory where venv and main.py are located when you run this command.


## Deactivation and Cleanup

To deactivate the virtual environment, run:

```bash
deactivate
```

To remove the virtual environment, delete the `venv/` folder:

```bash
rm -rf venv/
```
