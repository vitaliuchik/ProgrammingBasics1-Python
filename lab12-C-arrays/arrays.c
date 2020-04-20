#include <stdio.h>
#define N 100

int main()
{
    int arr1[N], arr2[N], arr[N];
    int k1=0;
    int k2=0;

    printf("Input arr1 (Enter 0 to stop):\n");
    while (k1 < N){
        scanf("%i", arr1+k1);
        if ( *(arr1+k1) == 0) break;
        k1++;
    }
    printf("Input arr2 (Enter 0 to stop):\n");
    while (k2 < N){
        scanf("%i", arr2+k2);
        if ( *(arr2+k2) == 0) break;
        k2++;
    }

    int max;
    //масив з сумами
    if (k1 <= k2){
        for (int i = 0; i<k1; i++)
            *(arr+i) = *(arr1+i) + *(arr2+i);
        for (int i = k1; i<k2; i++)
            *(arr+i) = *(arr2+i);
        max = k2;
    }
    else{
        for (int i = 0; i<k1; i++)
            *(arr+i) = *(arr1+i) + *(arr2+i);
        for (int i = k1; i<k2; i++)
            *(arr+i) = *(arr2+i);
        max = k1;
    }

    int k = 0;
    for (int i = 0; i < max; i++){
        if (*(arr+i) < 10)
            printf("%i ", *(arr+i));
        else
            printf("%i %i ", *(arr+i)/10, *(arr+i)%10);
    }
    return 0;
}
