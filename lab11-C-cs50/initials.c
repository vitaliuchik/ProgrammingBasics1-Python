#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>
#define MaxLen 511

int next_letter(char str[MaxLen], int space);
int next_space(char str[MaxLen], int letter);

int main(void)
{
    char outChar;
    bool notEnd = true;
    char inputStr[MaxLen];
    fgets(inputStr, MaxLen, stdin);
    int start = next_letter(inputStr, 0);
    while (notEnd == true)
    {
        outChar = toupper(inputStr[start]);
        printf("%c", outChar);
        start = next_letter(inputStr, next_space(inputStr, start));
        if (start == -1)
            notEnd = false;
    }
    printf("\n");
}

int next_letter(char str[MaxLen], int space)
{
    for (int i=space; i<strlen(str); i++)
    {
        if (str[i] != ' ')
            return i;
    }
    return -1;
}

int next_space(char str[MaxLen], int letter)
{
    for (int i=letter; i<strlen(str); i++)
    {
        if (str[i] == ' ')
            return i;
    }
    return -1;
}
