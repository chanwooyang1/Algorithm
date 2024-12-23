import java.util.*;
class Solution {
    public int solution(String word) {
       
        ArrayList<String> wordsList = new ArrayList<>();
        char[] vowels = {'A', 'E', 'I', 'O', 'U'};
        for(int length = 1; length <= 5; length++){
            generateWords("", length, vowels, wordsList);
        }
        Collections.sort(wordsList);
        return wordsList.indexOf(word) + 1;
        
        
    }
    private void generateWords(String current, int length, char[] vowels, ArrayList<String> wordsList){
        if(length == 0){
            wordsList.add(current);
            return;
        }
        
        for(char vowel : vowels){
            generateWords(current + vowel, length - 1, vowels, wordsList);
        }
    }
}