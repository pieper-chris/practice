// Basic search algorithms and their complexities


class Sorting
{
    // Bubble Sort (ints)

    static int[] bubble_sort(int []lst){
        int length = lst.length;
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
    static int[] insertion_sort(int [] lst){
        int length = lst.length;
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

    public static void main(String[] args){

        /* Example scripts for bubble_sort() below */

        System.out.println("Bubble Sort... ");
        int []arr;
        int lst1[] = {3,6,6,4,3,2,4,6};
        arr = lst1;
        System.out.println("arr unsorted: [3,6,6,4,3,2,4,6]");
        arr = bubble_sort(arr);
        int len = arr.length;
        String str = "[";
        for(int i = 0; i < len; i++){
            str += arr[i]+",";
            //System.out.println("Elt #"+i+" is " + arr[i]);
        }
        str += "]";
        
        System.out.println("arr sorted: " + str);
        
        /* Example scripts for insertion_sort() below */
        System.out.println("Insertion_Sort... ");
        int lst2[] = {3,6,6,4,3,2,4,6};
        arr = lst2;
        System.out.println("arr unsorted: [3,6,6,4,3,2,4,6]");
        arr = bubble_sort(arr);
        len = arr.length;
        str = "[";
        for(int i = 0; i < len; i++){
            str += arr[i]+",";
            //System.out.println("Elt #"+i+" is " + arr[i]);
        }
        str += "]";
        
        System.out.println("arr sorted: " + str);
    }

}

