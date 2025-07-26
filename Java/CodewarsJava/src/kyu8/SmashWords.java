package kyu8;

public class SmashWords {

    public static String smash(String[] words) {
        StringBuilder sentence = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            sentence.append(words[i]);
            if (i < words.length - 1) {
                sentence.append(" ");
            }
        }
        return sentence.toString();
    }
}
//https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/java
//You have passed all of the tests! :)