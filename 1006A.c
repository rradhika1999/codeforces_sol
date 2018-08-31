#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (){
    int n;
    scanf("%d",&n);
    int i;
    int a[n];
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
        if(a[i]%2==0){
            printf("%d ",a[i]-1);
        }
        else {
            printf("%d ",a[i]);
        }
    }
    
}
