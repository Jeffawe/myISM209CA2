from flask import Flask

app = Flask(__name__)  # create a flask app named app


@app.route("/")
def home():
    return '''My name is Ozoekwe-Awagu Jeffery. This is my CA2 work.
 My GitHub URL is https://github.com/Jeffawe/myISM209CA2'''
    # In the return statement above, Use your own name and GitHub URL


if __name__ == "__main__":
    app.run(port=5005)
