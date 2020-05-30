// Nice object-oriented solution

class Searching
{
    // Basic search algorithms and their complexities

    // Linear search (ints)
    // pass in the element (int) to be found and an int list to search in (can be unsorted)
    // returns index of 1st-found element to match 'elt', returns -1 if DNE
    static int linear_search(int elt, int arr[]){
        int idx = 0;
        int length = arr.length;
        while((idx<length) && (elt != arr[idx])){
            idx += 1;
        }
        if (idx < length){
            return idx;
        }else{
            return -1;
        }
    }

    // binary search (ints)
    // pass in the element (int) to be found and an int list to search in (must be unsorted)
    // returns index of 1st-found element to match 'elt', returns -1 if DNE

    static int binary_search(int elt, int arr[]){
        int length = arr.length;
        int left = 0;
        int right = (length - 1);
        while(left < right){
            int midpoint = (left + right) / 2;
            if (elt > arr[midpoint]){
                left = midpoint + 1;
            } else {right = midpoint;}
        }
        if (elt == arr[left]){
            return left;
        } else{
            return -1;
        }
    }



    public static void main(String[] args){
        
        /* Example scripts for linear_search() below */
        
        // should return -1
        int arr1[] = {3,6,6,4,3,2,4,6};
        System.out.println("Index (linear search) : " + linear_search(5, arr1));
        
        // should return 2 ("third index", as 1st index is 0)
        int arr2[] = {3,6,5,4,3,2,4,6};
        System.out.println("Index (linear search): " + linear_search(5, arr2));
        
        
        
        /* Example scripts for binary_search() below - using sorted lists*/
        
        // should return -1
        int arr3[] = {3,6,6,9,11,12,54,86};
        System.out.println("Index (binary search): " + binary_search(5, arr3));
        
        // should return 4 ("5th index", as 1st index is 0)
        int arr4[] = {1,2,3,4,5,6,7,8};
        System.out.println("Index (binary search): " + binary_search(5, arr4));
        
    }

}


