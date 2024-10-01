import { Signer, Call, InvocationsSignerDetails, constants, stark } from 'starknet';
import dotenv from 'dotenv';
dotenv.config();
(async () => {
  const mySigner = new Signer(process.env.STARKNET_PRIVATE_KEY);
  const calls: Call[] = [{
    contractAddress: "0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
    entrypoint: "transfer",
    calldata: ["1325201655285835467801926065478906035827722766541350904410603151659132389429", "10000000000000000", "0"]
  }];
  const transactionsDetail: InvocationsSignerDetails = {
    walletAddress: '0x01cD143262C41Bdaa9E8EEaEB6Ac61c351C1A9ac6C6502C1A0296CB4B1bed7F3',
    chainId: constants.StarknetChainId.SN_SEPOLIA,
    cairoVersion: "1",
    maxFee: '0xb1a2bc2ec50000',
    version: "0x1",
    nonce: "0xd"
  };
  const result: any = await mySigner.signTransaction(calls, transactionsDetail);
  const signatureDecimal = stark.signatureToDecimalArray(result)
  const signatureToHex = stark.signatureToHexArray(signatureDecimal)
  console.log(signatureToHex)
})();
