import java.util.HashSet;
public class Javaplay {
  public static void main(String args[]) {
  /** ASCII */
  // String s = "asb";
  // // System.out.println(s.charAt(1));
  // int[] index  = new int[128];
  // System.out.println(index[13]);
  // for(int i = 0; i < 128;i++){
  //   index[i] = i;
  // }
  // System.out.println(index[s.charAt(1)]);

  //Using HashSet
  // HashSet<Character> s = new HashSet<Character>();
  // String str = "string";
  // for (int i = 0; i < str.length() - 1 ;i++ ) {
  //     s.add(str.charAt(i));
  // }
  //     System.out.println(s.contains('i'));

  // []++
  int[] s1map = new int[26];
  String s1 = "malicious";
  for(int i = 0; i < s1.length(); i++){
    s1map[s1.charAt(i)-'a']++;
  }

  for(int i = 0; i < s1.length(); i++){
    System.out.println(s1map[i]);
  }
  
  }
}