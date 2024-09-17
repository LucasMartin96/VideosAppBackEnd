# YouTube Video API

This project is an API built with FastAPI that allows for creating, reading, updating, and deleting (CRUD) YouTube videos. It provides endpoints for managing a list of YouTube videos and their metadata.

## Requirements

- Python 3.x
- `pip` (Python package installer)
- `uvicorn` (ASGI server)

## Setup and Installation

Follow these steps to set up and run the project on your local machine (Windows).

### 1. Set up a Virtual Environment (Optional)

It is recommended to create a virtual environment to avoid conflicts with other projects. Run the following commands in your terminal (Command Prompt or PowerShell):

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

Once the virtual environment is activated (or if you're not using one), install the required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Run the API

After installing the dependencies, you can run the API using `uvicorn`. Execute the following command:

```bash
uvicorn app.main:app --reload
```

This will start the development server with live reloading.

You can interact with the API using any API client or by visiting the auto-generated documentation at:

```
http://localhost:8000/docs
```