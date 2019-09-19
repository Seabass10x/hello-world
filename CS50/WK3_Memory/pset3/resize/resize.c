// Resizes a BMP file

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize f infile outfile\n");
        return 1;
    }

    // convert f to float and check that it is a valid range
    float f = atof(argv[1]);
    if (f <= 0.0 || f > 100.0)
    {
        fprintf(stderr, "f is out of range: 0 < f <= 100\n");
        return 1;
    }

    // remember file names
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // modify headers for outfile
    BITMAPFILEHEADER rbf = bf;
    BITMAPINFOHEADER rbi = bi;

    rbi.biWidth = floor(bi.biWidth * f);
    rbi.biHeight = floor(bi.biHeight * f);
    int rpadding = (4 - (rbi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    rbi.biSizeImage = ((rbi.biWidth * sizeof(RGBTRIPLE)) + rpadding) * abs(rbi.biHeight);
    rbf.bfSize = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + rbi.biSizeImage;

    // write outfile's BITMAPFILEHEADER
    fwrite(&rbf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&rbi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // determine padding for scanlines
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // create an array to store the infile's pixels
    RGBTRIPLE bitmap[bi.biWidth][abs(bi.biHeight)];

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        // iterate over pixels in scanline
        for (int j = 0; j < bi.biWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            // store in bitmap array
            bitmap[j][i] = triple;
        }

        // skip over padding, if any
        fseek(inptr, padding, SEEK_CUR);

    }

    // write pixels to resized outfile using resized height and width
    for (int i = 0, rbiHeight = abs(rbi.biHeight); i < rbiHeight; i++)
    {
        // iterate over pixels in scanline
        for (int j = 0; j < rbi.biWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // divide iterators by f to determine which pixel to write
            triple = bitmap[(int)(j / f)][(int)(i / f)];

            // write RGB triple to outfile
            fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
        }

        // then add it back (to demonstrate how)
        for (int k = 0; k < rpadding; k++)
        {
            fputc(0x00, outptr);
        }
    }


    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
