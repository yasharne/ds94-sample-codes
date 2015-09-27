/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication4;

/**
 *
 * @author yashar
 */
public class JavaApplication4 {
    
    static int a[][];

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        a = new int[10][];
        for (int i = 0; i < a.length; i++) {
            if(i % 2 == 1)
                a[i] = new int[4];
            else
                a[i] = new int[5];
        }
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                a[i][j] = i * j;
            }
        }
        
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j] + "\t");
            }
            System.out.println("");
        }
        // TODO code application logic here
    }
    
}
