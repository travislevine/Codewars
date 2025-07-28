package kyu8;

import java.util.Arrays;

public class SumOfDifferences {
    public static int sumOfDifferences(int[] arr) {
        int sum = 0;
        if (arr.length < 2) {
            return 0;
        }
        Arrays.sort(arr);
        for (int i = arr.length - 1; i > 0; i--) {
            int difference = arr[i] - arr[i-1];
            sum += difference;
        }
        return sum;
    }
    //You have passed all of the tests! :)
    //https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/java
}
