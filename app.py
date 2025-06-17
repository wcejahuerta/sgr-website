from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    fence_type = request.form.get('fence_type')
    gates = request.form.get('gates')
    feet = request.form.get('feet')
    message = request.form.get('message')

    # Debug/logging purposes
    print("\n--- New Contact Request ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print(f"Fence Type: {fence_type}")
    print(f"# of Gates: {gates}")
    print(f"Feet: {feet}")
    print(f"Message: {message}")
    print("---------------------------\n")

    flash('Thank you for reaching out! We will contact you shortly.')
    return redirect('/')
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store"
    return response

if __name__ == '__main__':
    app.run(debug=True)
