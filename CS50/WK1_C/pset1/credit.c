// Validates a credit card number using Luhn's Algorithm
#include <cs50.h>
#include <stdio.h>

long get_card(string prompt);
int LENGTH = 0;
bool CHKSUM;
bool checksum(long c);
void validate(long c);

int main(void)
{
    long cc = get_card("Number: ");
    checksum(cc);
    validate(cc);
}

// Prompt user for credit card number
long get_card(string prompt)
{
    long n;
    do
    {
        n = get_long("%s", prompt);
    }
    while (n < 1);
    return n;
}

// Perform checksum test on credit card number
bool checksum(long c)
{
    int sum1 = 0;
    int sum2 = 0;
    while (c != 0)
    {
        LENGTH++;
        if (LENGTH % 2 == 1)
        {
            sum1 = sum1 + (c % 10);
        }
        else
        {
            sum2 = sum2 + ((2 * (c % 10)) / 10) + ((2 * (c % 10)) % 10);
        }
        c = c / 10;
    }
    CHKSUM = ((sum1 + sum2) % 10 == 0);
    return CHKSUM;
}

// Validate the credit card number
void validate(long c)
{
    if (CHKSUM == false)
    {
        printf("INVALID\n");
    }
    else
    {
        switch (LENGTH)
        {
            case 13:
                if ((c / 1000000000000) == 4)
                {
                    printf("VISA\n");
                    break;
                }
            case 15:
                if (((c / 10000000000000) == 34) || ((c / 10000000000000) == 37))
                {
                    printf("AMEX\n");
                    break;
                }
            case 16:
                if ((c / 1000000000000000) == 4)
                {
                    printf("VISA\n");
                    break;
                }
                else if (((c / 100000000000000) > 50) && ((c / 100000000000000) < 56))
                {
                    printf("MASTERCARD\n");
                    break;
                }
            default:
                printf("INVALID\n");
        }
    }
}
