from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        token = request.form.get('manual_token')
        file = request.files.get('token_file')

        if token:
            result = f"Manual Token Entered: {token[:5]}... (truncated)"
        elif file:
            content = file.read().decode('utf-8')
            result = f"File Uploaded: {len(content.splitlines())} tokens found."
        else:
            result = "No input provided."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
