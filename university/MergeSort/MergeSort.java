// libraries to include

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

// merge sort is a popular sorting algorithm known for its efficiency and stability.
// it follows the Divide and Conquer approach.
// it works by recursively dividing the input array into two halves, recursively sorting the two
// halves and finally merging them back together to obtain the sorted array.

// 1. divide 2. conquer 3. merge

class MergeSort
{

  // the maestro
  public static void
  main (String[] args)
  {

    // init scanner
    Scanner scn = new Scanner (System.in);

    // use scanner to get user input for array length
    System.out.println (
        "Please insert a value regarding the length of the random array that'll be created:");
    int arrLen = scn.nextInt ();
    scn.close ();

    // create the array with random values
    int[] arr = createRandomArr (arrLen);

    // print the array as string
    System.out.println (Arrays.toString (arr));

    // merge sort
    mergeSort (arr, 0, arr.length - 1);

    // print new array
    System.out.println (Arrays.toString (arr));
  }

  // create a random array to use in the merge sort algorithm
  static int[]
  createRandomArr (int arrLen)
  {

    // init
    int[] arr = new int[arrLen];
    Random rndm = new Random ();

    // create random values and pass in regarding the index value
    for (int i = 0; i < arrLen; i++)
      {
        arr[i] = rndm.nextInt (100);
      }

    return arr;
  }

  static void
  mergeSort (int[] arr, int starting_index, int ending_index)
  {

    if (starting_index < ending_index)
      {

        int middle_index = (starting_index + ending_index) / 2;

        mergeSort (arr, starting_index, middle_index);
        mergeSort (arr, middle_index + 1, ending_index);

        merge (arr, starting_index, middle_index, ending_index);
      }
  }

  static void
  merge (int[] arr, int starting_index, int middle_index, int ending_index)
  {

    // rename for a better understanding of the code
    int left_end_index = middle_index;
    int right_end_index = ending_index;

    // init arrays
    int[] leftArray = new int[left_end_index - starting_index + 2];
    int[] rightArray = new int[right_end_index - middle_index + 1];

    // set sentinel_values
    int SENTINEL_VALUE = 999999999;

    leftArray[left_end_index - starting_index + 1] = SENTINEL_VALUE;
    rightArray[right_end_index - middle_index] = SENTINEL_VALUE;

    // place values inside the left array
    for (int i = starting_index, counter = 0; i <= left_end_index; i++, counter++)
      {
        leftArray[counter] = arr[i];
      }

    // place values inside the right array
    for (int i = left_end_index + 1, counter = 0; i <= right_end_index; i++, counter++)
      {
        rightArray[counter] = arr[i];
      }

    // init counters for each array
    int left_counter = 0;
    int right_counter = 0;

    // now actually merge
    for (int counter = starting_index; counter <= ending_index; counter++)
      {
        if (leftArray[left_counter] >= rightArray[right_counter])
          {
            arr[counter] = rightArray[right_counter];
            right_counter += 1;
          }

        else
          {
            arr[counter] = leftArray[left_counter];
            left_counter += 1;
          }
      }
  }
}