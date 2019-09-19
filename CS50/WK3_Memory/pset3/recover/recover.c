#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // open input file
    FILE *inptr = fopen(argv[1], "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }
    // declare variables
    uint8_t buffer[512];
    int jpgcnt = 0;
    char jpgname[8];
    FILE *outptr;

    // read 512B buffers until there is no more data to read
    while (fread(buffer, 1, 512, inptr) != 0)
    {
        // check for JPEG header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // close previous JPEG file
            if (jpgcnt > 0)
            {
                fclose(outptr);
            }
            // open a numbered JPEG file
            sprintf(jpgname, "%03i.jpg", jpgcnt);
            outptr = fopen(jpgname, "w");

            jpgcnt++;
        }
        // write buffer to open JPEG file
        if (jpgcnt > 0)
        {
            fwrite(buffer, 512, 1, outptr);
        }
    }
    // close final JPEG file and raw file
    fclose(outptr);
    fclose(inptr);

    return 0;
}
