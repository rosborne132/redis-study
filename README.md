# Redis Study

## Prerequisites
- Python 3.6 or higher (https://www.python.org/downloads/)
- Git (https://git-scm.com/downloads)

## Getting Started
Follow these steps to set up and run the project on your local machine:

1. Clone the repository
Clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/rosborne132/redis-study.git
cd redis-study
```

2. Set up the virtual environment
Create and activate a virtual environment:

For Windows:
```bash
python3 -m venv venv
venv\Scripts\activate
```

For macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
pip install --upgrade pip
```

4. Run the application
Execute the main.py script to start the application:

```bash
redis-server
python3 main.py

# Install redis
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

5. Deactivate the virtual environment
When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```

## Running curl commands

```bash
curl -X POST -H "Content-Type: application/json" -d '{"player": "Rob", "score": 1500}' http://localhost:5000/update_score

```

```bash
curl http://localhost:5000/player/Rob
```
