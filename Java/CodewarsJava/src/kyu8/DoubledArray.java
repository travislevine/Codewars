package kyu8;
public class DoubledArray {
    public static int[] map(int[] arr) {
        int[] resultArray = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            resultArray[i] = arr[i] * 2;
        }
        return resultArray;
    }
}
//https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/java
//You have passed all of the tests! :)