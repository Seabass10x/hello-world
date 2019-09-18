// Vigenère’s cipher improves upon Caesar’s cipher by encrypting messages using a sequence of keys
// (or, put another way, a keyword).

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Verify that only one fully alpha keyword was given
    if (argc == 2)
    {
        int n = strlen(argv[1]);
        int kw[n];
        for (int i = 0; i < n; i++)
        {
            // Verify keyword is alpha
            if (isalpha(argv[1][i]))
            {
                // Create int array of keyword
                int upascii = (int)(toupper(argv[1][i]));
                kw[i] = (upascii - 65);
                //printf("%i\n", kw[i]);
            }
            else
            {
                printf("Usage: ./vigenere keyword\n");
                return 1;
            }
        }
        string ptext = get_string("plaintext:  ");
        int p = strlen(ptext);
        printf("ciphertext: ");
        int k = 0;
        // Convert plaintext to cyphertext
        for (int i = 0; i < p; i++)
        {
            int ascii = (int) ptext[i];
            int j = k % n;
            if (isupper(ptext[i]))
            {
                printf("%c", (((ascii - 65 + kw[j]) % 26) + 65));
                k++;
            }
            else if (islower(ptext[i]))
            {
                printf("%c", (((ascii - 97 + kw[j]) % 26) + 97));
                k++;
            }
            else
            {
                printf("%c", ptext[i]);
            }
        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
}
