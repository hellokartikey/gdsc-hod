from flask import Flask, render_template, request, Response, url_for
from flask_session import Session, sessions
from web3 import Web3
import json
import os

app = Flask(__name__)

# Env variables
CONTRACT_PATH = os.environ.get("CONTRACT_PATH")
RPC_URL = os.environ.get("RPC_URL")
CONTRACT_ADDRESS = os.environ.get("CONTRACT_ADDRESS")

w3 = Web3(Web3.HTTPProvider(RPC_URL))
tf = json.load(open(CONTRACT_PATH))
abi, bytecode = tf['abi'], tf['bytecode']
contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
# Contract instance
contract_instance = w3.eth.contract(abi=abi, address=contract_address)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        res = request.get_json(force=True)
        acc = res["account"]
        # Calling smart contract
        user_type = contract_instance.functions.fetchUser(acc).call()
        # user type
        # 0 = hospital
        # 1 = warehouse
        # 2 = factory
        if user_type == 0:
            return url_for("hospital")
        return Response(status=200)

@app.route("/customer", methods=["GET","POST"])
def hospital():
    if request.method == "GET":
        return render_template("hospital.html")

