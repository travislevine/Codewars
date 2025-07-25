package kyu8;

public class InvertValues {
    public static int[] invert(int[] array) {
        int arrayLen = array.length;
        int[] resultArray = new int[array.length];

        for (int i = 0; i < arrayLen; i++) {
            if (array[i] > 0) {
                resultArray[i] = array[i] * -1;
            } else {
                resultArray[i] = array[i] * -1;
            }
        }
        return resultArray;
    }
}
//https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/java
//You have passed all of the tests! :)