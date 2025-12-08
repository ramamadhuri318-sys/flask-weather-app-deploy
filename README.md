# Flask Starter – VS Code

Simple Flask project to run in VS Code, with Dockerfile and a basic GitHub Actions workflow.

## How to run in VS Code

1. Open VS Code.
2. Go to **File → Open Folder…** and select this folder.
3. Open an integrated terminal (**Terminal → New Terminal**).
4. Create virtual environment:

   ```bash
   python -m venv venv
   ```

5. Activate it:

   **Windows (PowerShell or CMD):**

   ```bash
   venv\Scripts\activate
   ```

6. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

7. Run the app:

   ```bash
   python app.py
   ```

8. Open a browser and go to: `http://localhost:5000`.

## Run with Docker

```bash
docker build -t flask-vscode-app .
docker run -p 5000:5000 flask-vscode-app
```
