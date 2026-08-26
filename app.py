from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure DevOps Web App</title>

        <style>

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                min-height: 100vh;

                background:
                    linear-gradient(
                        135deg,
                        #0f172a,
                        #1e3a8a,
                        #2563eb
                    );

                display: flex;
                justify-content: center;
                align-items: center;

                color: white;
            }

            .container {
                width: 90%;
                max-width: 900px;
                text-align: center;
            }

            .card {
                background: rgba(255, 255, 255, 0.12);

                backdrop-filter: blur(15px);

                border: 1px solid rgba(255, 255, 255, 0.2);

                border-radius: 25px;

                padding: 60px 40px;

                box-shadow:
                    0 25px 50px rgba(0, 0, 0, 0.3);
            }

            .icon {
                font-size: 70px;
                margin-bottom: 20px;
            }

            h1 {
                font-size: 48px;
                margin-bottom: 20px;
            }

            .subtitle {
                font-size: 20px;
                color: #dbeafe;
                margin-bottom: 35px;
                line-height: 1.6;
            }

            .status {
                display: inline-block;

                background: #22c55e;

                color: white;

                padding: 10px 20px;

                border-radius: 50px;

                font-weight: bold;

                margin-bottom: 35px;
            }

            .status::before {
                content: "●";
                margin-right: 8px;
                color: #bbf7d0;
            }

            .button {
                display: inline-block;

                background: white;

                color: #1d4ed8;

                padding: 15px 30px;

                border-radius: 50px;

                text-decoration: none;

                font-weight: bold;

                transition: 0.3s;
            }

            .button:hover {
                transform: translateY(-3px);

                box-shadow:
                    0 10px 25px rgba(0, 0, 0, 0.25);
            }

            .footer {
                margin-top: 25px;

                color: #bfdbfe;

                font-size: 14px;
            }

            @media (max-width: 600px) {

                h1 {
                    font-size: 34px;
                }

                .subtitle {
                    font-size: 17px;
                }

                .card {
                    padding: 40px 25px;
                }

            }

        </style>
    </head>

    <body>

        <div class="container">

            <div class="card">

                <div class="icon">
                    ☁️
                </div>

                <div class="status">
                    Deployment Successful
                </div>

                <h1>
                    Welcome to My Cloud App
                </h1>

                <p class="subtitle">
                    A Python Flask application deployed to
                    Microsoft Azure using an Azure DevOps CI/CD Pipeline.
                </p>

                <a href="#" class="button">
                    🚀 Explore Application
                </a>

                <p class="footer">
                    Built with Python • Flask • Azure • Azure DevOps
                </p>

            </div>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
