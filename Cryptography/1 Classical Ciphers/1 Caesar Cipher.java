/*
    The Caesar cipher is one of the oldest and simplest encryption techniques. 
    It is a substitution cipher where each letter in the plaintext is shifted 
    a fixed number of positions down the alphabet. For example, with a shift of 1: 
    A becomes B, B becomes C, and so on. This method is named after Julius Caesar, 
    who is said to have used it for secure communication.

    Example using a shift of 1:
    Plaintext : "defend the east wall of the castle"
    Ciphertext: "efgfoe uif fbtu xbmm pg uif dbtumf"

    Each letter is replaced by the next one in the alphabet. Decryption simply applies 
    the same shift in the opposite direction (e.g., -1 in this case).

    Alphabet shifted by 1:
    Plaintext : "abcdefghijklmnopqrstuvwxyz"
    Ciphertext: "bcdefghijklmnopqrstuvwxyza"

    Different keys produce different shifted alphabets, allowing varying levels of obfuscation.
    Despite its simplicity, the Caesar cipher is useful for illustrating basic principles 
    of encryption.
*/


class CaesarCipher {

    // Set of characters used for the cipher (uppercase alphabet)
    static final String CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    /**
     * Applies a simple substitution cipher to the input string,
     * shifting only alphabetic characters by a fixed amount.
     * This is the core logic used by both encrypt and decrypt.
     *
     * @param input       Original text to be processed
     * @param shiftValue  Integer shift amount (positive for encryption, negative for decryption)
     * @return Resulting text with alphabetic characters shifted
     */
    private static String applyShift(String input, int shiftValue) {
        // Input validation
        if (input == null || input.isEmpty()) {
            return input;
        }

        String upperInput = input.toUpperCase();
        StringBuilder result = new StringBuilder();

        // Normalize shiftValue to be within [0, 25] for correct modulo behavior
        int normalizedShift = shiftValue % 26;
        if (normalizedShift < 0) {
            normalizedShift += 26; // Ensure positive result for negative shifts
        }

        for (int i = 0; i < upperInput.length(); i++) {
            char currentChar = upperInput.charAt(i);
            int position = CHARACTERS.indexOf(currentChar);

            // If the character is in the alphabet, apply the shift
            if (position >= 0) {
                int shiftedPosition = (position + normalizedShift) % 26;
                result.append(CHARACTERS.charAt(shiftedPosition));
            } else {
                // If it's not a letter (e.g., space or punctuation), keep it unchanged
                result.append(currentChar);
            }
        }
        return result.toString();
    }

    /**
     * Encrypts text using the Caesar cipher.
     *
     * @param plaintext The original text to encrypt.
     * @param key       The integer shift amount.
     * @return The encrypted text (ciphertext).
     */
    public static String encrypt(String plaintext, int key) {
        return applyShift(plaintext, key);
    }

    /**
     * Decrypts text encrypted with the Caesar cipher.
     *
     * @param ciphertext The encrypted text to decrypt.
     * @param key        The integer shift amount used for encryption.
     * @return The decrypted text (original plaintext).
     */
    public static String decrypt(String ciphertext, int key) {
        // Decryption is the same as encryption with the inverse shift
        return applyShift(ciphertext, -key);
    }

    /**
     * Runs a test case for the Caesar cipher encryption and decryption.
     *
     * @param caseNumber   The number of the test case
     * @param originalText The text to be encrypted and decrypted
     * @param key          The shift value for the cipher
     */
    private static void runTest(int caseNumber, String originalText, int key) {
        System.out.println("--- Test Case " + caseNumber + " ---");
        System.out.println("Original Text : \"" + originalText + "\"");
        System.out.println("Key           : " + key);

        String encrypted = CaesarCipher.encrypt(originalText, key);
        String decrypted = CaesarCipher.decrypt(encrypted, key);

        System.out.println("Encrypted Text: \"" + encrypted + "\"");
        System.out.println("Decrypted Text: \"" + decrypted + "\"");
        System.out.println("Match Original: " + originalText.equalsIgnoreCase(decrypted));
        System.out.println();
    }

    /**
     * Main method for testing. Runs the encryption and decryption
     * with different inputs and shift values to demonstrate the cipher behavior.
     */
    public static void main(String[] args) {

        // Test Case 1: Standard Encryption and Decryption
        runTest(1, "defend the east wall of the castle", 1);

        // Test Case 2: Zero shift (should return original text)
        runTest(2, "ZeroShift", 0);

        // Test Case 3: Large shift value (should wrap around)
        runTest(3, "WrapAround", 27);
    }
}
