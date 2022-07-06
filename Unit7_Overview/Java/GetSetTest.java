class GetSetTest{
         private int _value;
         
         GetSetTest() {
             _value=0;
         }
         public int getVal()
         {
             return _value;
         }
         public void setVal(int x)
         {
             _value = x;
         }
     }
    public class Test{
     
     public static void main(String []args){
        GetSetTest t = new GetSetTest();
        t.setVal(25);
        System.out.println("Value=" + t.getVal());
    }
}
