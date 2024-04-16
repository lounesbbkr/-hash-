# Pi Hashing Algorithm

# MD Hash Algorithm with IV Derived from Pi Digits

This is a special implementation of the MD (Merkle-Damgård) hash algorithm construction where the initial Initialization Vector (IV) is derived from the digits of Pi. It was created by Boubekir Lounes.

## Description

The MD construction is an iterative method used to build hash functions from a compression function. This construction allows for processing messages of arbitrary length by dividing them into fixed-size blocks.

In this particular implementation, the initial IV is not a predefined constant, but rather derived from the digits of Pi. This approach aims to introduce an additional source of randomness into the hash algorithm to enhance its security.

## How It Works

1. The initial digits of Pi are extracted to form the IV value. The length of the IV depends on the word size used in the compression function.

2. The message to be hashed is divided into fixed-size blocks, of  256 bits.

3. The compression function is applied iteratively to each block, using the output value of the previous block as input for the next block. The first block uses the IV derived from the digits of Pi as its input value.

4. After processing all blocks, the final output of the compression function is the hash result.

## Advantages

- Using the digits of Pi as a source to derive the IV introduces an additional factor of unpredictability into the hash algorithm.
- The MD construction allows for efficient processing of messages of arbitrary length.
- The security of the algorithm relies on the strength of the underlying compression function.

## Usage

To use this hash algorithm, you need to have an implementation of the compression function compatible with the MD construction. You will also need access to a reliable source of Pi digits to extract the initial IV value.

Please refer to the documentation and source code for more details on the implementation and usage of this algorithm.

## Contributing

If you wish to contribute to the improvement of this algorithm or report any issues, feel free to open an issue or submit a pull request on the GitHub repository.

## Author

This hash algorithm was created by Boubekir Lounes.

## License

This project is licensed under [specify the appropriate license].