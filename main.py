from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if request.method == 'POST':
        message = request.form.get('message', '')

    return render_template_string("""
        <form method="POST">
            <input name="message" type="text">
            <input type="submit" value="Echo">
        </form>
        <p>{{ message }}</p>
    """, message=message)

if __name__ == '__main__':
    app.run(debug=True)
