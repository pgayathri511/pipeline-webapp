from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Azure DevOps Pipeline</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: "Segoe UI", Arial, sans-serif;
                min-height: 100vh;
                color: white;
                background:
                    radial-gradient(circle at 20% 20%, rgba(0, 120, 212, 0.35), transparent 30%),
                    radial-gradient(circle at 80% 80%, rgba(0, 188, 242, 0.25), transparent 30%),
                    linear-gradient(135deg, #07111f, #0b1f36 50%, #06101d);
                overflow-x: hidden;
            }

            /* Background glow */
            .glow {
                position: fixed;
                width: 350px;
                height: 350px;
                background: #0078d4;
                filter: blur(130px);
                opacity: 0.18;
                border-radius: 50%;
                top: 10%;
                left: -100px;
                z-index: 0;
            }

            .glow2 {
                position: fixed;
                width: 300px;
                height: 300px;
                background: #00bcf2;
                filter: blur(120px);
                opacity: 0.15;
                border-radius: 50%;
                bottom: 5%;
                right: -80px;
                z-index: 0;
            }

            /* Navigation */
            nav {
                position: relative;
                z-index: 2;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 25px 8%;
                border-bottom: 1px solid rgba(255,255,255,0.08);
                backdrop-filter: blur(10px);
            }

            .logo {
                font-size: 22px;
                font-weight: 700;
                letter-spacing: 0.5px;
            }

            .logo span {
                color: #00bcf2;
            }

            .status {
                display: flex;
                align-items: center;
                gap: 8px;
                font-size: 14px;
                color: #b9d8ee;
            }

            .status-dot {
                width: 9px;
                height: 9px;
                background: #00d084;
                border-radius: 50%;
                box-shadow: 0 0 12px #00d084;
                animation: pulse 2s infinite;
            }

            /* Hero */
            .hero {
                position: relative;
                z-index: 1;
                min-height: 68vh;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 70px 20px 40px;
            }

            .hero-content {
                max-width: 900px;
            }

            .badge {
                display: inline-block;
                padding: 9px 18px;
                border-radius: 50px;
                background: rgba(0, 120, 212, 0.15);
                border: 1px solid rgba(0, 188, 242, 0.35);
                color: #70d7ff;
                font-size: 14px;
                margin-bottom: 25px;
                animation: fadeDown 0.8s ease;
            }

            h1 {
                font-size: clamp(42px, 7vw, 78px);
                line-height: 1.05;
                font-weight: 800;
                margin-bottom: 25px;
                animation: fadeUp 0.8s ease;
            }

            h1 .highlight {
                background: linear-gradient(90deg, #00bcf2, #0078d4, #5c2d91);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .subtitle {
                max-width: 700px;
                margin: auto;
                color: #b7c8d8;
                font-size: 19px;
                line-height: 1.7;
                animation: fadeUp 1s ease;
            }

            /* Buttons */
            .buttons {
                margin-top: 35px;
                display: flex;
                justify-content: center;
                gap: 15px;
                flex-wrap: wrap;
            }

            .btn {
                text-decoration: none;
                padding: 14px 26px;
                border-radius: 10px;
                font-weight: 600;
                transition: 0.3s ease;
            }

            .btn-primary {
                color: white;
                background: linear-gradient(135deg, #0078d4, #00a8e8);
                box-shadow: 0 10px 30px rgba(0,120,212,0.3);
            }

            .btn-primary:hover {
                transform: translateY(-3px);
                box-shadow: 0 15px 35px rgba(0,188,242,0.4);
            }

            .btn-secondary {
                color: #d9edf9;
                border: 1px solid rgba(255,255,255,0.18);
                background: rgba(255,255,255,0.05);
            }

            .btn-secondary:hover {
                background: rgba(255,255,255,0.1);
                transform: translateY(-3px);
            }

            /* Cards */
            .cards {
                position: relative;
                z-index: 2;
                max-width: 1100px;
                margin: 0 auto;
                padding: 20px 25px 70px;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 22px;
            }

            .card {
                padding: 30px;
                border-radius: 18px;
                background: rgba(255,255,255,0.06);
                border: 1px solid rgba(255,255,255,0.1);
                backdrop-filter: blur(14px);
                transition: 0.35s ease;
            }

            .card:hover {
                transform: translateY(-8px);
                border-color: rgba(0,188,242,0.45);
                background: rgba(255,255,255,0.09);
                box-shadow: 0 20px 45px rgba(0,0,0,0.25);
            }

            .icon {
                width: 52px;
                height: 52px;
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 14px;
                margin-bottom: 20px;
                font-size: 25px;
                background: linear-gradient(
                    135deg,
                    rgba(0,120,212,0.35),
                    rgba(0,188,242,0.15)
                );
            }

            .card h3 {
                font-size: 20px;
                margin-bottom: 10px;
            }

            .card p {
                color: #9eb2c5;
                line-height: 1.6;
                font-size: 15px;
            }

            /* Pipeline */
            .pipeline {
                position: relative;
                z-index: 2;
                max-width: 900px;
                margin: 0 auto;
                padding: 10px 25px 70px;
                text-align: center;
            }

            .pipeline h2 {
                font-size: 30px;
                margin-bottom: 35px;
            }

            .steps {
                display: flex;
                justify-content: space-between;
                position: relative;
            }

            .steps::before {
                content: "";
                position: absolute;
                top: 24px;
                left: 10%;
                right: 10%;
                height: 2px;
                background: linear-gradient(90deg, #0078d4, #00bcf2);
                opacity: 0.5;
            }

            .step {
                position: relative;
                z-index: 1;
                width: 25%;
            }

            .circle {
                width: 48px;
                height: 48px;
                margin: 0 auto 12px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #0b2138;
                border: 2px solid #00bcf2;
                box-shadow: 0 0 20px rgba(0,188,242,0.25);
            }

            .step strong {
                display: block;
                font-size: 14px;
            }

            .step small {
                color: #7f95a9;
                display: block;
                margin-top: 5px;
            }

            /* Footer */
            footer {
                position: relative;
                z-index: 2;
                text-align: center;
                padding: 25px;
                color: #71869a;
                font-size: 13px;
                border-top: 1px solid rgba(255,255,255,0.08);
            }

            /* Animations */
            @keyframes pulse {
                0%, 100% {
                    transform: scale(1);
                    opacity: 1;
                }
                50% {
                    transform: scale(1.3);
                    opacity: 0.6;
                }
            }

            @keyframes fadeUp {
                from {
                    opacity: 0;
                    transform: translateY(25px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes fadeDown {
                from {
                    opacity: 0;
                    transform: translateY(-15px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            /* Mobile */
            @media (max-width: 750px) {
                nav {
                    padding: 20px;
                }

                .cards {
                    grid-template-columns: 1fr;
                }

                .steps {
                    flex-direction: column;
                    gap: 25px;
                }

                .steps::before {
                    display: none;
                }

                .step {
                    width: 100%;
                }

                .hero {
                    min-height: 60vh;
                    padding-top: 50px;
                }

                .subtitle {
                    font-size: 16px;
                }
            }
        </style>
    </head>

    <body>

        <div class="glow"></div>
        <div class="glow2"></div>

        <nav>
            <div class="logo">Azure<span>Pipeline</span></div>

            <div class="status">
                <div class="status-dot"></div>
                Deployment Active
            </div>
        </nav>

        <section class="hero">
            <div class="hero-content">

                <div class="badge">
                    ⚡ CI/CD • Azure DevOps • Flask
                </div>

                <h1>
                    Build. Deploy.<br>
                    <span class="highlight">Scale.</span>
                </h1>

                <p class="subtitle">
                    A modern Python Flask application automatically deployed
                    to Microsoft Azure using a continuous integration and
                    continuous deployment pipeline.
                </p>

                <div class="buttons">
                    <a href="#pipeline" class="btn btn-primary">
                        Explore Pipeline
                    </a>

                    <a href="#features" class="btn btn-secondary">
                        View Features
                    </a>
                </div>

            </div>
        </section>

        <section class="cards" id="features">

            <div class="card">
                <div class="icon">🚀</div>
                <h3>Fast Deployment</h3>
                <p>
                    Push your code and let the automated pipeline handle
                    building and deployment to Azure.
                </p>
            </div>

            <div class="card">
                <div class="icon">☁️</div>
                <h3>Azure Cloud</h3>
                <p>
                    Running in Microsoft Azure with the flexibility and
                    scalability of cloud infrastructure.
                </p>
            </div>

            <div class="card">
                <div class="icon">⚙️</div>
                <h3>CI/CD Automation</h3>
                <p>
                    Automated workflows reduce manual deployment steps and
                    make releasing new versions easier.
                </p>
            </div>

        </section>

        <section class="pipeline" id="pipeline">

            <h2>Deployment Pipeline</h2>

            <div class="steps">

                <div class="step">
                    <div class="circle">💻</div>
                    <strong>Code</strong>
                    <small>Git Repository</small>
                </div>

                <div class="step">
                    <div class="circle">🔨</div>
                    <strong>Build</strong>
                    <small>Azure DevOps</small>
                </div>

                <div class="step">
                    <div class="circle">🚀</div>
                    <strong>Deploy</strong>
                    <small>Azure App Service</small>
                </div>

                <div class="step">
                    <div class="circle">🌐</div>
                    <strong>Live</strong>
                    <small>Production</small>
                </div>

            </div>

        </section>

        <footer>
            Built with Python Flask • Deployed with Azure DevOps • Hosted on Azure
        </footer>

    </body>
    </html>
    """


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
