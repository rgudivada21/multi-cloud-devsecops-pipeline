# Flask Application (app.py)

## Why do we need this file?

A computer cannot directly show a web page.

If we write:

```python
print("Hello")
```

it only prints in the terminal.

We need a web framework to receive requests from a browser and send responses back.

For this project, we use **Flask**.

---

## Developer Thinking

Problem:

User opens:

http://localhost:5000

↓

The application should return a response.

To do this, we need:

1. Create a Flask application.
2. Tell Flask which URL to handle.
3. Write the logic for that URL.
4. Start the server.

---

## Code

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Multi-Cloud DevSecOps Pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Explanation

### 1.

```python
from flask import Flask
```

Imports the Flask framework.

Without this, Python cannot create a web application.

---

### 2.

```python
app = Flask(__name__)
```

Creates a Flask application.

Think of this as turning an empty Python file into a web application.

---

### 3.

```python
@app.route("/")
```

Maps the home URL (`/`) to the function below.

When a user visits:

http://localhost:5000/

Flask calls the `home()` function.

---

### 4.

```python
def home():
```

This function contains the logic for the home page.

---

### 5.

```python
return "Hello from Multi-Cloud DevSecOps Pipeline!"
```

Sends the response back to the browser.

---

### 6.

```python
if __name__ == "__main__":
```

Runs the application only when this file is executed directly.

---

### 7.

```python
app.run(host="0.0.0.0", port=5000)
```

Starts the Flask server.

- `host="0.0.0.0"` allows Docker and Kubernetes to access the application.
- `port=5000` runs the application on port 5000.

---

## Request Flow

Browser

↓

localhost:5000

↓

Flask

↓

home()

↓

Return response

↓

Browser displays the message

---

## Real-world Usage

In a real company, this function usually:

- Reads data from a database
- Calls another API
- Processes business logic
- Returns JSON or HTML

---

## Interview Questions

### Why do we use Flask?

To build web applications and REST APIs.

### What does @app.route() do?

It connects a URL to a Python function.

### Why use host="0.0.0.0"?

To allow external access, especially from Docker and Kubernetes.

### What happens when we open localhost:5000?

Flask executes the `home()` function and returns the response.
