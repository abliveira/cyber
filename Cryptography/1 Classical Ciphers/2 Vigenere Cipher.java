/*

The Vigenère cipher is a technique for encrypting alphabetic text using a repeated keyword.
Each letter in the plaintext is shifted by an amount determined by the corresponding letter
in the keyword (modulo the alphabet length). This creates polyalphabetic substitution,
making it more secure than a Caesar cipher.

Example:
Plaintext : "knowledge"
Keyword   : "key"
Encrypted : "ULCGZIAHII"

Explanation:
   k e y k e y k e y  ← keyword (repeated)
 + k n o w l e d g e  ← plaintext
 -------------------
   u l c g z i a h i  ← ciphertext (in uppercase)

Note: Only letters are encrypted. Non-letter characters (e.g., punctuation, spaces) remain unchanged.

*/

class VigenereCipher {

    // Set of characters used for the cipher (uppercase alphabet)
    static final String CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    /**
     * Applies the Vigenère cipher to the input string using a keyword.
     *
     * @param input   The text to be encrypted
     * @param keyword The keyword used for encryption
     * @return The encrypted text with characters shifted based on the keyword
     */
    public static String encrypt(String input, String keyword) {
        if (input == null || input.isEmpty()) {
            return input;
        }
        if (keyword == null || keyword.isEmpty()) {
            throw new IllegalArgumentException("Keyword cannot be null or empty.");
        }

        String upperInput = input.toUpperCase();
        String upperKeyword = keyword.toUpperCase();
        StringBuilder result = new StringBuilder();

        int keywordIndex = 0;

        for (int i = 0; i < upperInput.length(); i++) {
            char currentChar = upperInput.charAt(i);
            int charPos = CHARACTERS.indexOf(currentChar);

            if (charPos >= 0) {
                char keyChar = upperKeyword.charAt(keywordIndex % upperKeyword.length());
                int keyShift = CHARACTERS.indexOf(keyChar);

                int shiftedPosition = (charPos + keyShift) % 26;
                result.append(CHARACTERS.charAt(shiftedPosition));

                keywordIndex++;
            } else {
                // Keep non-alphabet characters unchanged
                result.append(currentChar);
            }
        }
        return result.toString();
    }

    /**
     * Decrypts a Vigenère ciphered string using a keyword.
     *
     * @param input   The text to be decrypted
     * @param keyword The keyword used for decryption
     * @return The decrypted text
     */
    public static String decrypt(String input, String keyword) {
        if (input == null || input.isEmpty()) {
            return input;
        }
        if (keyword == null || keyword.isEmpty()) {
            throw new IllegalArgumentException("Keyword cannot be null or empty.");
        }

        String upperInput = input.toUpperCase();
        String upperKeyword = keyword.toUpperCase();
        StringBuilder result = new StringBuilder();

        int keywordIndex = 0;

        for (int i = 0; i < upperInput.length(); i++) {
            char currentChar = upperInput.charAt(i);
            int charPos = CHARACTERS.indexOf(currentChar);

            if (charPos >= 0) {
                char keyChar = upperKeyword.charAt(keywordIndex % upperKeyword.length());
                int keyShift = CHARACTERS.indexOf(keyChar);

                // For decryption, subtract the shift. Add 26 to handle negative results before modulo.
                int shiftedPosition = (charPos - keyShift + 26) % 26;
                result.append(CHARACTERS.charAt(shiftedPosition));

                keywordIndex++;
            } else {
                // Keep non-alphabet characters unchanged
                result.append(currentChar);
            }
        }
        return result.toString();
    }

    /**
     * Utility method to test Vigenère cipher with input and keyword.
     *
     * @param testNumber Identifier for the test
     * @param text       Text to encrypt/decrypt
     * @param keyword    Key to use for the cipher
     */
    public static void runTest(int testNumber, String text, String keyword) {
        System.out.println("--- Test Case " + testNumber + " ---");
        System.out.println("Input          : " + text);
        System.out.println("Keyword        : " + keyword);
        String encrypted = encrypt(text, keyword);
        System.out.println("Encrypted      : " + encrypted);
        String decrypted = decrypt(encrypted, keyword);
        System.out.println("Decrypted      : " + decrypted);
        System.out.println("Match Original : " + text.equalsIgnoreCase(decrypted));
        System.out.println();
    }

    /**
     * Main method for testing. Runs the Vigenère encryption and decryption with different inputs.
     */
    public static void main(String[] args) {
        runTest(1, "knowledge", "key");               // Comment example
        runTest(2, "hello world!", "cipher");         // Includes space and punctuation
        runTest(3, "Secure Communication", "vigenere"); // Typical use case
    }
}
