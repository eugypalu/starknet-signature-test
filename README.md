To set up the environment, follow these steps:

1. Copy the `.env.example` file to a new `.env` file by running the command `cp .env.example .env` in your terminal.
2. Open the newly created `.env` file and set the following values:
   - `STARKNET_PRIVATE_KEY`: your StarkNet private key
   - `STARKNET_ACCOUNT_ADDRESS`: your StarkNet account address
   - `NETHERMIND_API_KEY`: your Nethermind API key for rpc.nethermind.io/sepolia-juno

To run the Python script:
1. cd starknet_py_sign
2. python -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. python starknet_transfer.py


To run the Typescript script:
1. cd starknetjs_sign
2. npm install
3. npm start

Both scripts output the transaction signature in hexadecimal format.
To verify the transaction hash and the private key used for signing, refer to the following locations:
- For Python: starknet_py/net/signer/stark_curve_signer.py (sign_transaction function)
- For JavaScript: starknet/dist/index.js (signTransaction function)
