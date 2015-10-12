package javaapplication3;

public class Test {

    static LinkedList l = new LinkedList();

    public static void main(String[] args) {

        System.out.println(l);
        l.push_front(123, "Ali");
        System.out.println(l);
        try {
            l.pop_back();
        } catch (Exception e) {
        }
        System.out.println(l);
        l.push_front(123, "Ali");
        l.push_front(234, "Ahmad");
        l.push_back(345, "Zahra");
        l.push_front(876, "Mahsa");
        System.out.println(l);
        l.insert(732, "Shaghaiegh", 3);
        System.out.println(l);

    }

}
