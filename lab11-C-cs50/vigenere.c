#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MaxLen 511

int main(int argc, char* argv[])
{
    if (argc != 2)
        return 1;

    int key[strlen(argv[1])];
    for (int i = 0, n = strlen(argv[1]); i < n; i++ )
    {
        if ( argv[1][i] >= 'a' && argv[1][i] <= 'z' )
            key[i] = (int) argv[1][i] - (int) 'a';
        else if ( argv[1][i] >= 'A' && argv[1][i] <= 'Z' )
            key[i] = (int) argv[1][i] - (int) 'A';
        else
            return 1;
    }

    printf("Please, enter your text: ");
    char inputStr[MaxLen];
    fgets(inputStr, MaxLen, stdin);

    char outputStr[strlen(inputStr)];
    int position;
    int main_key_count;
    int key_count = 0;

    printf("ciphertext: ");
    for (int i = 0, n = strlen(inputStr); i < n; i++)
    {
        main_key_count = key_count % strlen(argv[1]);
        position = (int) inputStr[i] + key[main_key_count];
        if ( (position > (int) 'z' ) || (position > (int) 'Z' && inputStr[i] <= 'Z' ) )
            position -= 26;
        if ( (inputStr[i] >= (int) 'a' &&  inputStr[i] <= (int) 'z' ) || (inputStr[i] >= (int) 'A' &&  inputStr[i] <= (int) 'Z' ) )
        {
            outputStr[i] = (char) position;
            key_count++;
        }
        else
            outputStr[i] = inputStr[i];
        printf("%c", outputStr[i]);
    }
    printf("\n");

}
