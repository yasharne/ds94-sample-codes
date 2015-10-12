package recursion;

public class Recursion {

    public static int gcd(int a, int b) {
        if(a == 0) return b;
   if(b == 0) return a;
   if(a > b) return gcd(b, a % b);
   return gcd(a, b % a);
    }
    
    public static int fib(int n) {
        if (n > 2) {
            return fib(n - 1) + fib(n - 2);
        } else {
            return 1;
        }
    }

    public static int fib2(int n1, int n2, int n3) {
        if (n3 > 2) {
            return fib2(n2, n1 + n2, n3 - 1);
        } else {
            return n2;
        }
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("testing fib");
        for (int i = 1; i < 11; i++) {
            System.out.println("fib " + i + " = " + fib(i));
        }
        
        System.out.println("\n\ntesting fib2");
        for (int i = 1; i < 11; i++) {
            System.out.println("fib " + i + " = " + fib2(1, 1, i));
        }
        
        System.out.println("\n\ngcd(2,20) = " + gcd(2,20));
        System.out.println("gcd(8,10) = " + gcd(8,10));
        System.out.println("gcd(5,110) = " + gcd(5,110));
        System.out.println("gcd(16,100) = " + gcd(16,100));
        
    }

}
