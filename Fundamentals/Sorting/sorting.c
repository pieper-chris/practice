#include <stdio.h>

// Basic search algorithms and their complexities

// Bubble Sort (ints)

int* bubble_sort(int *lst){
    int length = sizeof(&lst);
    if (length < 2){return lst;}
    for(int i = 0; i < length; i++){
        for(int j = 0; j < length - 1 - i; j++){
            if(lst[j]>lst[j+1]){
                int temp = lst[j];
                lst[j] = lst[j+1];
                lst[j+1] = temp;
            }
        }
    }
    return lst;
}

// Insertion Sort
int* insertion_sort(int * lst){
    int length = sizeof(lst);
    if(length < 2){return lst;}
    for(int right = 0; right < length; right++){
        int left = 0;
        while(lst[right] > lst[left]){ left += 1;}
        int temp = lst[right];
        for (int k = 0; k < (right - left); k++){
            lst[right-k] = lst[right-k-1];
        }
        lst[left] = temp;
    }
    return lst;
}

int main(){

    /* Example scripts for bubble_sort() below */

    int *arr;
    int lst1[] = {3,6,6,4,3,2,4,6};
    arr = lst1;
    arr = bubble_sort(arr);
    int len = sizeof(arr);
    for(int i = 0; i < len; i++){
        printf("Elt #%d is %d\n", i, arr[i]);
    }
    
    /* Example scripts for insertion_sort() below */
    
    int lst2[] = {3,6,6,4,3,2,4,6};
    arr = lst2;
    arr = bubble_sort(arr);
    len = sizeof(arr);
    for(int i = 0; i < len; i++){
        printf("Elt #%d is %d\n", i, arr[i]);
    }
    
    return 0;
}
