import java.util.*;
class J201options {
  public static void main(String[] args) { 
    Scanner keyboard = new Scanner(System.in);
    //double num1=keyboard.nextDouble();
    int num=Integer.parseInt(keyboard.nextLine());
    // String name=keyboard.nextLine();
    //System.out.println("Harish said \"Hello\" to Sally");
    //System.out.println("Harish said \nHello\n to Sally");
    //System.out.println("Harish said \tHello\t to Sally");
    // System.out.println("Your name is "+name);
    // System.out.println("Twice the number is "+num*2);
    if (num==1) { 
      System.out.println("Option 1");
    } else if (num==2){
      System.out.println("Option 2");
    } else {
      System.out.println("Not a Valid Option");     
    }
  }
}
