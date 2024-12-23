import java.util.*;
class Solution {
    ArrayList<String> wordList = new ArrayList<>();
    public int solution(String word) {
        int answer = 0;
        char[] vowels  = {'A','E','I','O','U'};
        for(int length = 1; length <= 5; length++){
            makeWords("", vowels, length);
        }
        Collections.sort(wordList);
        
        return wordList.indexOf(word) + 1;
    }
    
    private void makeWords(String current, char[] vowels, int length){
        if(length == 0){
            wordList.add(current);
            return;
        }
        for(char vowel : vowels){
            makeWords(current + vowel, vowels, length - 1);
        }
    }
}