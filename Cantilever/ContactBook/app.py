from flask import Flask, render_template, request, redirect

app = Flask(__name__)
FILE = "contacts.txt"

def read_contacts():
    contacts = []
    try:
        with open(FILE, "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
    except:
        pass
    return contacts

@app.route("/")
def index():
    return render_template("index.html", contacts=read_contacts())

@app.route("/add", methods=["POST"])
def add():
    with open(FILE, "a") as f:
        f.write(f"{request.form['name']},{request.form['phone']},{request.form['email']}\n")
    return redirect("/")

@app.route("/delete/<name>")
def delete(name):
    contacts = read_contacts()
    with open(FILE, "w") as f:
        for c in contacts:
            if c["name"] != name:
                f.write(f"{c['name']},{c['phone']},{c['email']}\n")
    return redirect("/")

@app.route("/edit", methods=["POST"])
def edit():
    old_name = request.form["old_name"]
    contacts = read_contacts()

    with open(FILE, "w") as f:
        for c in contacts:
            if c["name"] == old_name:
                f.write(f"{request.form['name']},{request.form['phone']},{request.form['email']}\n")
            else:
                f.write(f"{c['name']},{c['phone']},{c['email']}\n")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
