import java.util.ArrayList;

public class NumbersVampires {
    private static ArrayList vampires = new ArrayList ();
    private static final int MIN = 11;
    private static final int MAX = 99;
    private static final int LEN = 4;

    public static boolean check (char[] s1, char[] s2) {
        boolean have = false;

        for (int i = 0; i < LEN; i++) {
            for (int j = 0; j < LEN; j++) {

                if (s1[i] == s2[j]) {
                    s2[j] = '_';
                    have = true;
                    break;
                }
                else
                    have = false;
            }

            if (!have)
                return false;
        }

        return true;
    }

    public static void main (String[] args) {
        
        char[] mul = new char[LEN];
        char[] cat = new char[LEN];

        for (int n1 = MIN; n1 <= MAX; n1++) {
            for (int n2 = MAX; n2 >= MIN; n2--) {
                if (n1 * n2 < 1000)
                    continue;

                mul = Integer.toString (n1 * n2).toCharArray ();
                cat = (Integer.toString (n1) + Integer.toString (n2)).toCharArray ();

                if (check (cat, mul) && !vampires.contains (n1 * n2))
                    vampires.add (n1 * n2);
            }
        }

        System.out.println (vampires);
    }
}