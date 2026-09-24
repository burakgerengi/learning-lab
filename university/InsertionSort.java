import java.util.Arrays;
import java.util.Random;
import java.util.random.*;

// FIXME: fix the code errors.

public class InsertionSort {
    public static void main(String[] args) {
        int dizi[] = new int[15];
        Random rnd = new Random();
        for (int i = 0; i < dizi.length; i++) {
            dizi[i] = rnd.nextInt(51);
        }
        System.out.println(Arrays.toString(dizi));
        System.out.println(sort(dizi));
    }
}

public static void sort(int arr[]) {
    for (int j = 1; j < arr.length; j++) {
        int key = arr[j];
        int i = j - 1;

        while (i >= 0 && arr[i] > key) {
            arr[i + 1] = arr[i];
            i--;
        }
        arr[i] = key;
    }
}
