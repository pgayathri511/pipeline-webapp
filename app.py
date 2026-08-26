from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Pipeline Web App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                text-align: center;
                padding: 50px;
            }

            h1 {
                color: #0078d4;
            }

            p {
                font-size: 20px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Pipeline Web App!</h1>
        <p>This Flask application is deployed using Azure DevOps Pipeline.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
