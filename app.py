from flask import Flask
import os
import time

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv('USER')

    # Get current server time in IST
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5*3600 + 30*60))

    # Get top command output (you can mock this data for testing purposes)
    top_output = "Sample Top Output"

    return f"""
        <html>
            <head><title>System Info</title></head>
            <body>
                <h1>System Info</h1>
                <p>Name: Yezaz Abdul</p>
                <p>Username: {username}</p>
                <p>Server Time (IST): {server_time}</p>
                <h2>Top Output</h2>
                <pre>{top_output}</pre>
            </body>
        </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
