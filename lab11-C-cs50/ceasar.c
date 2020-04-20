#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MaxLen 511

int main(int argc, char* argv[])
{
    if (argc != 2)
        return 1;

    int key = atoi(argv[1]) % 26;
    printf("Please, enter your text: ");
    char inputStr[MaxLen];
    fgets(inputStr, MaxLen, stdin);
    char outputStr[strlen(inputStr)];
    int position;

    for (int i = 0, n = strlen(inputStr); i < n; i++)
    {
        position = (int) inputStr[i] + key;
        if ( (position > (int) 'z' ) || (position > (int) 'Z' && inputStr[i] <= 'Z' ) )
            position -= 26;

        if (inputStr[i] != ' ')
            outputStr[i] = (char) position;
        else
            outputStr[i] = ' ';
    }

    printf("ciphertext: ");
    for (int i = 0, n = strlen(outputStr); i < n; i++)
        printf("%c", outputStr[i]);
    printf("\n");
}
