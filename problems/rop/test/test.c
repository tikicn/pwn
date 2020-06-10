#include<stdio.h>
#include<stdlib.h>

void pwnme(){
    int *a;
    a=(int *)malloc(100);
    if(a==NULL){
        exit(EXIT_FAILURE);
    }
    return;
}

int main(){
    pwnme();
    return 0;
}

