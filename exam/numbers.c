#include <stdio.h>

int int_len(int num);

int main(void){
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    int len = 0;
    int row = 0;
    int num =1;
    while (len < a*b){
        while (row < a){
            printf("%d", num);
            num++;
            len = len + int_len(num);
        }
        row++;
        printf("\n");
    }
}


int int_len(int num){
    int len = 1;
    while (num / 10*len != 0){
        len++;
    }
    return len;
}