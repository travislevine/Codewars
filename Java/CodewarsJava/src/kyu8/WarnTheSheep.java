package kyu8;

public class WarnTheSheep {
    public static String warnTheSheep(String[] array) {
        //Your code)))
        // 1: Find the wolf index
        int wolfIndex = 0;
        for (int i = 0; i < array.length ; i++) {
            if ("wolf".equals(array[i])) {
                wolfIndex = i;
                break;
            }
        }
        if (wolfIndex == (array.length - 1)) {
            return  "Pls go away and stop eating my sheep";
        } else {
            int sheepNumber = array.length - 1 - wolfIndex;
            return "Oi! Sheep number " + sheepNumber + "! You are about to be eaten by a wolf!";
        }
    }
}
//https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/java
//You have passed all of the tests! :)