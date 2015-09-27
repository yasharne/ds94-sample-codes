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
public class NewClass {
    public static void main(String[] args) {
    
    Test[] a = new Test[10];
    for(int i=0;i< a.length;i++)
    {
       a[i] = new Test("",i);
    }
    
    for(int i = 0; i<a.length;i++)
    {
        System.out.println(a[i].id);
    }
    }
}


class Test{
  
    String name;
    int id;
    
    public Test(String name, int id)
    {
        this.name=name;
        this.id=id;
        
        
    }
}