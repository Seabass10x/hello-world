// A Caesar Cipher: Returns an encrypted message converting input text by
// shifting each letter by a certain a number of places input as a
// command argument.

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Verify that only one argument was given and that it was a +int
    if (argc == 2)
    {
        int key = atoi(argv[1]);
        if (key > 0)
        {
            string ptext = get_string("plaintext:  ");
            printf("ciphertext: ");
            //convert each letter to its ascii value shift and print it
            for (int i = 0, n = strlen(ptext); i < n; i++)
            {
                int ascii = (int) ptext[i];
                if (isupper(ptext[i]))
                {
                    printf("%c", (((ascii - 65 + key) % 26) + 65));
                }
                else if (islower(ptext[i]))
                {
                    printf("%c", (((ascii - 97 + key) % 26) + 97));
                }
                else
                {
                    printf("%c", ptext[i]);
                }
            }
            printf("\n");
            return 0;
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
