from flask import Flask, render_template, request, redirect, url_for
import boto3
import json

app = Flask(__name__)

# Lambda client
lambda_client = boto3.client('lambda', region_name='us-east-1')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Log incoming request
    print("Received POST request")
    print(f"Request form data: {request.form}")

    name = request.form.get('name')
    email = request.form.get('mail')
    country = request.form.get('country')

    payload = json.dumps({
        "name": name,
        "email": email,
        "country": country
    })

    print(f"Invoking Lambda with payload: {payload}")

    try:
        response = lambda_client.invoke(
            FunctionName='dbconnector',
            InvocationType='RequestResponse',
            Payload=payload
        )

        response_payload = json.loads(response['Payload'].read())
        print(f"Lambda response object: {response}")
        print(f"Lambda response payload: {response_payload}")

        # Access the 'body' of the response and parse it
        body = json.loads(response_payload['body'])  # Parsing the body JSON string

        if response['StatusCode'] == 200 and body.get('status') == 'success':
            return redirect(url_for('success'))
        else:
            error_message = body.get('message', 'Unknown error occurred')
            print(f"Error storing data: {error_message}")
            return redirect(url_for('failure', error=error_message))

    except Exception as e:
        print(f"Error invoking Lambda: {e}")
        return redirect(url_for('failure', error='Error invoking Lambda: ' + str(e)))

@app.route('/success')
def success():
    return "Data successfully stored in the database!"

@app.route('/failure')
def failure():
    error = request.args.get('error', 'No specific error message')
    return f"Failed to store data in the database. Error: {error}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

