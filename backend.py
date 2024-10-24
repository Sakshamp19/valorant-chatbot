from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.json
    selected_option = data.get('selectedOption', '')

    # Path to the main.py script
    script_path = 'main.py'

    try:
        # Run the script with selected option as argument and capture the output
        result = subprocess.run(['python', script_path, selected_option], capture_output=True, text=True)
        print("Result : ",result)
        # response_lines = result['response'].strip().split('\n')
        # igl_line = next(line for line in response_lines if line.startswith('IGL:'))
        # igl_value = igl_line.split(': ')[1]
        # Parse the JSON output from the script
        output = json.loads(result.stdout)
        print("Output : ",output)
        # Send the result as a response to the frontend
        return jsonify({'status': 'success', 'output': output['response'], 'players': output['players']})
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
