# NeuralLedger: Federated Learning on a Byzantine-Fault-Tolerant Blockchain for Decentralized AI Provenance

## Detailed Description

NeuralLedger is a novel framework that combines federated learning (FL) with a Byzantine-fault-tolerant (BFT) blockchain to enable secure and decentralized training of AI models. The primary goal of this project is to address the challenges of data privacy, model poisoning attacks, and lack of transparency in traditional centralized machine learning deployments. By leveraging the inherent security and immutability of blockchain technology, NeuralLedger facilitates a collaborative learning environment where participants can contribute to model training without revealing their sensitive data. The system incorporates verifiable computation and zero-knowledge proofs (ZKPs) to guarantee the integrity of model updates and provide verifiable provenance for AI models.

The architecture comprises a permissioned blockchain based on a BFT consensus algorithm, ensuring resilience against malicious actors. Federated learning is implemented using a decentralized averaging approach, where each participant trains a local model on their private dataset and submits encrypted updates to the blockchain. These updates are aggregated and verified by designated validator nodes, employing cryptographic techniques to detect and mitigate model poisoning attacks. The integration of verifiable computation allows for publicly verifiable execution of computationally intensive tasks, such as model aggregation and validation, without revealing the underlying data. Furthermore, ZKPs are used to generate verifiable proofs of model characteristics and training processes, enabling secure and transparent auditing of AI models.

NeuralLedger offers several key benefits over traditional centralized and federated learning systems. Firstly, it enhances data privacy by allowing participants to train models on their local data without sharing it directly with a central server. Secondly, it improves model robustness by incorporating Byzantine fault tolerance and cryptographic verification mechanisms. Thirdly, it provides verifiable provenance of AI models, enabling stakeholders to trace the origin and evolution of models and assess their trustworthiness. Lastly, the decentralized nature of the system fosters collaboration and democratizes access to AI technologies, empowering individuals and organizations to participate in the development of more reliable and transparent AI solutions.

## Key Features

*   **Byzantine Fault Tolerance (BFT):** Employs a BFT consensus algorithm (e.g., Tendermint) to ensure the blockchain's resilience against malicious nodes attempting to disrupt the training process or manipulate model updates. The implementation specifically uses a modified version of the PBFT algorithm optimized for federated learning scenarios.

*   **Federated Averaging with Differential Privacy:** Implements a secure federated averaging algorithm where participants train models locally and submit differentially private model updates to the blockchain. Differential privacy is achieved through the addition of calibrated noise to the model gradients. This implementation uses the Gaussian mechanism to add noise proportional to the L2 sensitivity of the gradient updates.

*   **Verifiable Computation:** Integrates verifiable computation techniques (e.g., zk-SNARKs) to enable publicly verifiable execution of model aggregation and validation tasks. This allows anyone to verify that the aggregation was performed correctly without needing to execute the computation themselves. Specifically, the system leverages libsnark to generate and verify proofs of correct model aggregation.

*   **Zero-Knowledge Proofs (ZKPs) for Model Provenance:** Utilizes ZKPs to create verifiable proofs of model characteristics and training processes. This allows for secure and transparent auditing of AI models without revealing sensitive information about the training data or model architecture. Implementation includes generating proofs for model accuracy on a small, public dataset, proving that the model meets certain performance criteria without revealing the actual model parameters.

*   **Smart Contract Integration:** Leverages smart contracts on the blockchain to manage the federated learning process, including participant registration, model update submission, aggregation, and reward distribution. The smart contracts are written in Solidity and deployed on a permissioned Ethereum-compatible blockchain.

*   **Model Poisoning Detection:** Incorporates cryptographic techniques such as homomorphic encryption and secure multi-party computation (SMPC) to detect and mitigate model poisoning attacks. This includes detecting outliers in model updates and isolating malicious participants. The implementation uses additive homomorphic encryption to allow validator nodes to compute the average model update without decrypting the individual updates.

*   **Data Encryption:** All data transmitted and stored on the blockchain is encrypted using advanced encryption standards (AES-256) to ensure confidentiality and protect against unauthorized access. The implementation uses a hybrid encryption scheme, where AES keys are encrypted using RSA.

## Technology Stack

*   **Python:** The primary programming language for implementing the federated learning algorithms, cryptographic protocols, and blockchain integration.
*   **TensorFlow/PyTorch:** Deep learning frameworks used for training and evaluating AI models. TensorFlow is preferred for its production readiness, while PyTorch is favored for its research-friendly features. The code is designed to be modular and easily adaptable to either framework.
*   **Solidity:** Smart contract language used for defining and deploying the federated learning logic on the blockchain.
*   **Web3.py:** Python library for interacting with the Ethereum blockchain and deploying smart contracts.
*   **libsnark:** C++ library for generating and verifying zk-SNARKs, used for verifiable computation.
*   **Tendermint:** Byzantine-fault-tolerant consensus engine used for building the blockchain.
*   **gRPC:** High-performance, open-source universal RPC framework used for inter-process communication and communication between blockchain nodes and clients.

## Installation

1.  Clone the repository:
    `git clone https://github.com/ezozu/NeuralLedger.git`
    `cd NeuralLedger`

2.  Install the required Python packages:
    `python3 -m venv venv`
    `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
    `pip install -r requirements.txt`

3.  Install Tendermint (follow instructions specific to your operating system at https://docs.tendermint.com/master/introduction/install.html). Ensure `tendermint` is added to your PATH.

4. Install libsnark:
    Follow the instructions on the libsnark github repository (https://github.com/scipr-lab/libsnark). This involves installing several dependencies and building the library from source. Ensure that the libsnark libraries are linked correctly during compilation of the ZKP components.

5.  Set up the blockchain network.  Navigate to the `blockchain` directory and run the initialization script:
    `cd blockchain`
    `./init_blockchain.sh`

## Configuration

*   **Environment Variables:**
    *   `BLOCKCHAIN_RPC_URL`: The URL of the blockchain RPC endpoint (e.g., `http://localhost:26657`).
    *   `PRIVATE_KEY`: The private key of the participant's Ethereum account.
    *   `CONTRACT_ADDRESS`: The address of the deployed smart contract on the blockchain.
    *   `TENSORFLOW_VISIBLE_DEVICES`: (Optional) Restricts TensorFlow to only use specified GPUs.

*   **Configuration Files:**
    *   `config.ini`: Contains configurable parameters for the federated learning process, such as the number of rounds, the learning rate, and the differential privacy parameters. Example:
        `[FederatedLearning]`
        `rounds = 10`
        `learning_rate = 0.01`
        `dp_epsilon = 1.0`

## Usage

1.  **Start the Blockchain Network:**
    `tendermint init`
    `tendermint node --proxy-app=kvstore`

2.  **Deploy the Smart Contract:**
    Use a tool like Remix or Truffle to deploy the Solidity smart contract located in the `contracts` directory to the blockchain. Update the `CONTRACT_ADDRESS` environment variable with the deployed address.

3.  **Run a Federated Learning Participant:**

    Example:

    Set the environment variables:
    `export BLOCKCHAIN_RPC_URL="http://localhost:26657"`
    `export PRIVATE_KEY="0x..."`
    `export CONTRACT_ADDRESS="0x..."`

    Run the participant script:
    `python participant.py`

    The `participant.py` script will:
    *   Connect to the blockchain.
    *   Register the participant with the smart contract.
    *   Train a local model on a private dataset.
    *   Submit differentially private model updates to the blockchain.

4. **Run the Aggregator Node:**
   Set the necessary environment variables and execute the aggregator script. This node will be responsible for receiving and aggregating model updates, verifying their integrity and updating the global model.

## Contributing

We welcome contributions to NeuralLedger! Please follow these guidelines:

*   Fork the repository and create a branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Follow the project's coding style and conventions.
*   Include unit tests for your code.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ezozu/NeuralLedger/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for providing valuable tools and resources that have contributed to the development of NeuralLedger.