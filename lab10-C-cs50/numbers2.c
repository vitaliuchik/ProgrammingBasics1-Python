#include <stdio.h>

int main(void)
{
    char *nums[] = {"one","two","three","four","five","six","seven","eight","nine"};
    int left, right;
    scanf("%i", &left);
    scanf("%i", &right);
    for(int i = left; i <= right; i++)
    {
        if (i > 0)
        {
            if (i < 10)
                printf("%s\n", nums[i-1]);
            else if (i % 2 == 0)
                printf("even\n");
            else
                printf("odd\n");
        }
    }
}
