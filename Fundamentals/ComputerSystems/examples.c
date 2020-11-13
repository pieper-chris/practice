#include <stdio.h>

typedef unsigned char *byte_ptr;

void show_bytes(byte_ptr start, size_t len){
    int i;
    for(i=0;i<len;i++)
        printf(" %.2x",start[i]);
    printf("\n\n");
}

void show_int(int x){
    printf("%d in hex:\n", x);
    show_bytes((byte_ptr) &x, sizeof(int));
}

void show_float(float x){
    printf("%f in hex:\n", x);
    show_bytes((byte_ptr) &x, sizeof(float));
}

int main(){
    
    // Show bit-level representation of numbers (hex format)
    // little-endian on my local machine, may vary on other machines (i.e. big-endian instead)
    int x = 10;
    float y = 3.45;
    show_int(x);
    show_float(y);
    
    int shift_num = 7;
    int shifted = shift_num << 5;
    printf("preshift: %d, postshift %d \n\n", shift_num, shifted);
    
    shift_num = -91;
    shifted = shift_num >> 2;
    printf("preshift: %d, postshift %d \n\n", shift_num, shifted);
    
    
    int a = 7;
    int b = 8;
    printf("preop a: %d, preop b:  %d \n\n", a, b);
    
    // showing bitwise property that a^a=0
    
    a = a^b; // a = a^b, b = b
    b = a^b; // a = a^b, b = (a^b)^b = a
    a = a^b; // a = (a^b)^a = b
    
    // swaped
    printf("postop a: %d, postop b:  %d \n\n", a, b);
    
    
    //Unsigned behavior
    unsigned long unint = (unsigned) -2147483647-1u;
    unsigned long unint2 = (unsigned) -2147483647;
    printf("-2147483647-1U =  %lu \n\n", unint);
    printf("-2147483647 =  %lu \n\n", unint2);
    
    
    return 0;
    
}
