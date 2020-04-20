#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int height;
    char h[511];
    do
    {
        printf("Enter height of the pyramid: ");
        scanf("%s", h);
        
        height = strtol(h, NULL, 10);
    }
    while (height < 0 || height > 23 || h[0] != '0');

    for (int line = 0; line < height; line++)
    {
        for (int empty = height - line; empty > 1; empty--)
            printf(" ");

        for (int symbol = 0; symbol < line + 2; symbol++)
            printf("#");

        printf("\n");
    }
}
