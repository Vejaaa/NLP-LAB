public class Exp2 {
    public static int countBigrams(String[] corpus, String word1, String word2) {
        int count = 0;
        for (String sentence : corpus) {
            String[] words = sentence.split(" ");
            for (int i = 0; i < words.length - 1; i++) {
                if (word1.equalsIgnoreCase(words[i]) && word2.equalsIgnoreCase(words[i + 1])) {
                    count++;
                }
            }
        }
        return count;
    }
    public static int countUnigrams(String[] corpus, String word) {
        int count = 0;
        for (String sentence : corpus) {
            for (String w : sentence.split(" ")) {
                if (word.equalsIgnoreCase(w)) {
                    count++;
                }
            }
        }
        return count;
    }
    public static void main(String[] args) {
        String[] corpus = {
                "There is a big garden",
                "Children play in the garden",
                "They play inside beautiful garden"
        };
        String[] testWords = "They play in a big garden".split(" ");
        double probability = 1.0;
        int vocabularySize = 9;
        for (int i = 0; i < testWords.length - 1; i++) {
            int bigramCount = countBigrams(corpus, testWords[i], testWords[i + 1]);
            int unigramCount = countUnigrams(corpus, testWords[i]);
            double smoothedProbability = (double) (bigramCount + 1) / (unigramCount + vocabularySize);
            System.out.printf("Bigram count of ('%s', '%s'): %d%n", testWords[i], testWords[i + 1], bigramCount);
            System.out.printf("Unigram count of '%s': %d%n", testWords[i], unigramCount);
            System.out.printf("Smoothed probability of ('%s', '%s'): %.4f%n", testWords[i], testWords[i + 1], smoothedProbability);
            probability *= smoothedProbability;
        }
        System.out.printf("Final Probability: %.8f%n", probability);
    }
}
