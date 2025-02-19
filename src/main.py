from flask import Flask, render_template

app = Flask(__name__)

@app.route("/ecommerce_test")
def ecommerce_test():
    return render_template("ecommerce.html")

@app.route("/account_test")
def account_test():
    return render_template("account.html")

if __name__ == "__main__":
    app.run(debug=True)