import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
public class Test{
    public static void test(Collection<?> c){
            for (Object n: c) {
                System.out.print(n+" ");
            }
            System.out.println("");
    }
    public static void main(String []args){
        List<Integer> L1= 
            Arrays.asList(1,2,3,4,5);
        test(L1);
        List<Float> L2= 
            Arrays.asList(1.1f,2.1f,3.1f,4.1f,5.1f);
        test(L2);
        List<String> L3=
            Arrays.asList("a","b","c","d","e");
        test(L3);
    }
}
