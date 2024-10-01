import os
import asyncio
from starknet_py.net.account.account import Account
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.transaction import Invoke
from starknet_py.contract import Contract
from starknet_py.net.client_models import Call
from starknet_py.hash.selector import get_selector_from_name

async def main():
    # Account details
    private_key_hex = os.environ.get('STARKNET_PRIVATE_KEY')
    account_address_hex = os.environ.get('STARKNET_ACCOUNT_ADDRESS')
    api_key = os.environ.get('NETHERMIND_API_KEY')

    # Check if environment variables are set
    if not all([private_key_hex, account_address_hex, api_key]):
        raise ValueError("Missing required environment variables. Please set STARKNET_PRIVATE_KEY, STARKNET_ACCOUNT_ADDRESS, and NETHERMIND_API_KEY.")

    # Convert to integers
    try:
        private_key = int(private_key_hex, 16)
    except (ValueError, TypeError):
        raise ValueError("Invalid STARKNET_PRIVATE_KEY. Please ensure it's a valid hexadecimal string.")

    try:
        account_address = int(account_address_hex, 16)
    except (ValueError, TypeError):
        raise ValueError("Invalid STARKNET_ACCOUNT_ADDRESS. Please ensure it's a valid hexadecimal string.")

    # Create KeyPair
    key_pair = KeyPair.from_private_key(private_key)

    # Initialize the client
    RPC_CLIENT = FullNodeClient(node_url=f"https://rpc.nethermind.io/sepolia-juno/?apikey={api_key}")

    # Create Account object
    account = Account(
        address=account_address,
        client=RPC_CLIENT,
        key_pair=key_pair,
        chain=StarknetChainId.SEPOLIA,
    )

    # Define the call
    call = Call(
        to_addr=int("0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7", 16),
        selector=get_selector_from_name("transfer"),
        calldata=[
            1325201655285835467801926065478906035827722766541350904410603151659132389429,
            10000000000000000,
            0,
        ],
    )

    max_fee = int("0xb1a2bc2ec50000", 16)
    nonce = int("0xd", 16)

    invoke_tx = await account.sign_invoke_v1(
        calls=call,
        max_fee=max_fee,
        nonce=nonce,
        auto_estimate=False,
    )

    signature = invoke_tx.signature

    # Extract r and s values
    if len(signature) >= 2:
        r = signature[0]
        s = signature[1]
        print("r (hex):", hex(r))
        print("s (hex):", hex(s))

if __name__ == "__main__":
    asyncio.run(main())