#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
 * Function: get_position
 * ----------------------------
 *  Return position of letter in alphabet.
 *
 *   ch: a letter
 *
 *   returns: position of letter in alphabet.
 *            If argument is not a letter function should return -1.
 */
int get_position(char ch);

/*
 * Function: compare_char
 * ----------------------------
 *  Compare two char by their position in alphabet.
 *
 *   ch1: first char
 *   ch2: second char
 *
 *   returns: Return 1 if letter ch2 appears before ch1 and 0 otherwise.
 *            If neither ch1 nor ch2 are letters function should return -1.
 */
int compare_char(char ch1, char ch2);

/*
 * Function: compare_str
 * ----------------------------
 *  Compare two strings lexicographically.
 *
 *   ch1: first char array
 *   ch2: second char array
 *
 *   returns: Return 1 if string s1 is larger than string s2 and 0 otherwise.
 *            If arguments have different length function should return -1.
 */
int compare_str(char *ch1, char *ch2);

/*
 * Function: type_by_angles
 * ----------------------------
 *  Detect the type of triangle by it's angles in degrees.
 *
 *   a: first angle
 *   b: second angle
 *   c: third angle
 *
 *   returns: return type as int ("right angled triangle" ==> 1, "obtuse triangle" ==> 2, "acute triangle" ==> 3).
 *            If there is no triangle with such angles, then function should return -1.
 */
int type_by_angles(int a, int b, int c);

/*
 * Function: type_by_sides
 * ----------------------------
 *  Detect the type of triangle by it's sides.
 *
 *   a: first side
 *   b: second side
 *   c: third side
 *
 *   returns: return type as int ("right angled triangle" ==> 1, "obtuse triangle" ==> 2, "acute triangle" ==> 3).
 *            If there is no triangle with such sides, then function should return -1.
 */
int type_by_sides(int a, int b, int c);

/*
 * Function: number_of_sentences
 * ----------------------------
 *   Return number of sentences in the char array.
 *
 *   s: char array
 *
 *   returns: Return number of sentences in the char array.
 */
int number_of_sentences(char *s);

/*
 * Function: replace_with_starts
 * ----------------------------
 *   Replace symbols in char array with stars.
 *
 *   s: char array
 *
 *   returns: Return replaced with stars char array.
 */
char *replace_with_starts(char *s);

/*
 * Function: encrypt_message
 * ----------------------------
 *   Replace all letters in char array with next letters in alphabet.
 *
 *   s: char array
 *
 *   returns: Return encrypted replaced char array with next letters in alphabet.
 */
char *encrypt_message(char *s);

/*
 * Function: decrypt_message
 * ----------------------------
 *   Replace all letters in char array with previous letters in alphabet.
 *
 *   s: char array
 *
 *   returns: Return replaced char array with previous letters in alphabet.
 */
char *decrypt_message(char *s);

/*
 * Function: number_of_capital_letters
 * ----------------------------
 *   Find and return number of capital letters in char array.
 *
 *   lst: int array
 *
 *   returns: return number of capital letters in char array.
 */
int number_of_capital_letters(char *s);


int main() {
    char func_name[30];
    scanf("%s\n", func_name);
    fflush(stdin);

    if (strcmp(func_name, "get_position") == 0)
    {
        char c[511];
        scanf("%c", &c);
        if (c[1] != '\0') printf("-1");
        else printf("%i", get_position(c[0]));
    }
    else if (strcmp(func_name, "compare_char") == 0)
    {
        char c1, c2;
        scanf("%c\n", &c1);
        scanf("%c", &c2);
        printf("%i", compare_char(c1, c2));
    }
    else if (strcmp(func_name, "compare_str") == 0)
    {
        char s1[511], s2[511];
        fgets(s1, 511, stdin);
        fgets(s2, 511, stdin);
        printf("%i", compare_str(s1, s2));
    }
    else if (strcmp(func_name, "type_by_angles") == 0)
    {
        int a, b, c;
        scanf("%i\n", &a);
        scanf("%i\n", &b);
        scanf("%i", &c);
        printf("%i", type_by_angles(a, b, c));
    }
    else if (strcmp(func_name, "type_by_sides") == 0)
    {
        int a, b, c;
        scanf("%i\n", &a);
        scanf("%i\n", &b);
        scanf("%i", &c);
        printf("%i", type_by_sides(a, b, c));
    }
    else if (strcmp(func_name, "number_of_sentences") == 0)
    {
        char s[511];
        fgets(s, 511, stdin);
        printf("%i", number_of_sentences(s));
    }
    else if (strcmp(func_name, "number_of_capital_letters") == 0)
    {
        char s[511];
        fgets(s, 511, stdin);
        printf("%i", number_of_capital_letters(s));
    }
    else if (strcmp(func_name, "replace_with_starts") == 0)
    {
        char s[511];
        fgets(s, 511, stdin);
        printf("%s", replace_with_starts(s));
    }
    else if (strcmp(func_name, "encrypt_message") == 0)
    {
        char s[511];
        fgets(s, 511, stdin);
        printf("%s", encrypt_message(s));
    }
    else if (strcmp(func_name, "decrypt_message") == 0)
    {
        char s[511];
        fgets(s, 511, stdin);
        printf("%s", decrypt_message(s));
    }
    else return -1;

    return 0; // Zero indicates success, while any Non-Zero value indicates a failure/error
}


int get_position(char ch)
{
    int position = (int)ch;
    if (position >= 65 && position <= 90) return (position - 64);
    else if (position >= 97 && position <= 122) return (position - 96);
    else return -1;
}


int compare_char(char ch1, char ch2)
{
    if (get_position(ch1) == -1 || get_position(ch2) == -1) return -1;
    else if (get_position(ch1) > get_position(ch2)) return 1;
    else return 0;
}


int compare_str(char *ch1, char *ch2)
{
    if (strlen(ch1) != strlen(ch2)) return -1;
    for (int i = 0; i < strlen(ch1); i++)
        if (get_position(ch1[i]) > get_position(ch2[i])) return 1;
    return 0;
}


int type_by_angles(int a, int b, int c)
{
    if (a > 0 && b > 0 && c > 0 && a + b + c == 180)
    {
        if (a == 90 || b == 90 || c == 90) return 1;
        else if (a > 90 || b > 90 || c > 90) return 2;
        else return 3;
    }
    return -1;
}


int type_by_sides(int a, int b, int c)
{
    if (a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a)
    {
        if (a*a == b*b + c*c || c*c == a*a + b*b || b*b == a*a + c*c) return 1;
        else if (a*a > b*b + c*c || c*c > a*a + b*b || b*b > a*a + c*c) return 2;
        else return 3;
    }
    return -1;
}


int number_of_sentences(char *s)
{
    int amount = 0;
    for (int i = 0; i < strlen(s); i++)
        if (s[i] == '.' || s[i] == '!' || s[i] == '?') amount++;
    return amount;
}


char *replace_with_starts(char *s)
{
    #define LEN strlen(s)
    static char* star;
    star = malloc(LEN * sizeof(char));

    for (int i = 0; i < LEN - 1; i++)
        star[i] = '*';
    star[LEN - 1] = '\0';
    return (char*)&star[0];
}


char *encrypt_message(char *s)
{
    #define LEN strlen(s)
    static char* encrypt;
    encrypt = malloc(LEN * sizeof(char));

    int position;
    for (int i = 0; i < LEN - 1; i++)
    {
        position = (int) s[i] + 1;
        if ( (position > (int) 'z' ) || (position > (int) 'Z' && s[i] <= 'Z' ) )
            position -= 26;

        if ( (s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z') )
            encrypt[i] = (char) position;
        else
            encrypt[i] = s[i];
    }
    encrypt[LEN - 1] = '\0';
    return (char*)&encrypt[0];
}


char *decrypt_message(char *s)
{
    #define LEN strlen(s)
    static char* decrypt;
    decrypt = malloc(LEN * sizeof(char));

    int position;
    for (int i = 0; i < LEN - 1; i++)
    {
        position = (int) s[i] - 1;
        if ( (position < (int) 'A' ) || (position < (int) 'a' && s[i] >= 'a' ) )
            position += 26;

        if ( (s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z') )
            decrypt[i] = (char) position;
        else
            decrypt[i] = s[i];
    }
    decrypt[LEN - 1] = '\0';
    return (char*)&decrypt[0];
}


int number_of_capital_letters(char *s)
{
    int amount = 0;
    for (int i = 0; i < strlen(s); i++)
        if (s[i] >= 'A' && s[i] <= 'Z') amount++;
    return amount;
}
