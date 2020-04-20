#include <stdio.h>
#include <math.h>

int main(void)
{
    float price;
    do
    {
        printf("Enter change: ");
        scanf("%f", &price);
    }
    while (price < 0.0);

    int money = round(price * 100);
    int coin25 = money / 25;
    int coin10 = (money % 25) / 10;
    int coin5 = (money % 25 % 10) / 5;
    int coin1 = money % 5;

    int amount = coin25 + coin10 + coin5 + coin1;
    printf("%i", amount);
}
