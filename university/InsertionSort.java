import java.util.Arrays;
import java.util.Random;

public class InsertionSort {
    public static void main(String[] args) {
        // create an array of random numbers
        int random_numbers[] = new int[30];
        Random rnd = new Random();
        for (int i = 0; i < random_numbers.length; i++) {
            random_numbers[i] = rnd.nextInt(100);
        }
        print_arr(random_numbers);
        insertion_sort(random_numbers);
        print_arr(random_numbers);

    }


public static void insertion_sort(int arr[]) {
    for (int j = 1; j < arr.length; j++) {
        int key = arr[j];
        int i = j - 1;

        while (i >= 0 && arr[i] > key) {
            arr[i+1] = arr[i];
            i--;
        }
        arr[i+1] = key;
    }
}

public static void print_arr(int arr[])
{
    System.out.println(Arrays.toString(arr));
}

}