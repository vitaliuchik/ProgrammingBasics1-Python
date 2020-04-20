#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    char str[80];
    int count = 0;
    fgets(str, 81, stdin);

    for(int i=0; str[i]; i++)
    {
        if (str[i] != ' ')
        {
            str[count] = str[i];
            count++;
        }
    }
    str[count] = '\0';

    int row = floor(sqrt(strlen(str) - 1));
    int column = ceil(sqrt(strlen(str) - 1));
    if (row*column < strlen(str) - 1) row++;

    // виведення таблиці
    // for (int i = 0; i < row; i++)
    // {
    //     for (int j = 0; j < column; j++)
    //     {
    //         if (str[i*column + j] != '\0')
    //             putchar(str[i*column + j]);
    //         else
    //             break;
    //     }
    //     putchar('\n');
    // }

    int sup = row;
    for (int i = 0; i < column; i++)
    {
        for (int j = 0; j < sup; j++)
        {
            if (j*column + i == strlen(str) - 2)
                sup--;
            putchar(str[j*column + i]);
        }
        putchar(' ');
    }



}
