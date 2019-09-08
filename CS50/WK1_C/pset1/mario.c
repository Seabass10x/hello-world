#include <cs50.h>
#include <stdio.h>

int get_height(string prompt);
void space(int s);
void brick(int b);
void pyramid(int h);

int main(void)
{
    int h = get_height("Height: ");
    pyramid(h);
}

// Prompt user for height between 1 and 8
int get_height(string prompt)
{
    int n;
    do
    {
        n = get_int("%s", prompt);
    }
    while (n < 1 || n > 8);
    return n;
}

// Print spaces
void space(int s)
{
    for (int j = 0; j < s; j++)
    {
        printf(" ");
    }
}

// Print bricks #
void brick(int b)
{
    for (int k = 0; k < b; k++)
    {
        printf("#");
    }
}

// Build the pyramid
void pyramid(int h)
{

    for (int i = 1; i <= h; i++)
    {
        space(h - i);
        brick(i);
        printf("  ");
        brick(i);
        printf("\n");
    }
}
