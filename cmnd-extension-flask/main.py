# main.py
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from dotenv import load_dotenv

# Import tool collections from different modules
from tools import tools as general_tools
from get_db import tools as get_db_tools
from company_get_db import tools as company_db_tools

# Import the send_sms function
from send_sms import send_sms, tools as sms_tools

load_dotenv()
app = Flask(__name__)
CORS(app)

# Combine tools from all sources into one list
combined_tools = []
combined_tools.extend(general_tools)
combined_tools.extend(get_db_tools)
combined_tools.extend(company_db_tools)
combined_tools.extend(sms_tools)  # Assuming sms_tools is a list similar to other modules

@app.route("/cmnd-tools", methods=['GET'])
def cmnd_tools_endpoint():
    tools_response = [
        {
            "name": tool["name"],
            "description": tool["description"],
            "jsonSchema": tool.get("parameters", {}),
            "isDangerous": tool.get("isDangerous", False),
            "functionType": tool["functionType"],
            "isLongRunningTool": tool.get("isLongRunningTool", False),
            "rerun": tool["rerun"],
            "rerunWithDifferentParameters": tool["rerunWithDifferentParameters"],
        } for tool in combined_tools
    ]
    return jsonify({"tools": tools_response})

@app.route("/run-cmnd-tool", methods=['POST'])
def run_cmnd_tool_endpoint():
    data = request.json
    tool_name = data.get('toolName')
    props = data.get('props', {})
    tool = next((t for t in combined_tools if t['name'] == tool_name), None)
    if not tool:
        abort(404, description="Tool not found")
    try:
        result = tool["runCmd"](**props)
        return jsonify(result)
    except Exception as e:
        abort(500, description=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)



