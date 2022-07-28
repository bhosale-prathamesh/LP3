import java.io.*;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class fib{
	public static void main(String[] args){
		System.out.print("Enter n: ");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		System.out.println("Recursive:");
		long startTime = System.nanoTime();
		System.out.println(rec_fib(n));
		long endTime = System.nanoTime();
        	long timeElapsed = endTime - startTime;
        
        	System.out.println("Recursive Time required (ns):"+timeElapsed);
        
		
		System.out.println("Iterative:");
		long itestartTime = System.nanoTime();
		System.out.println(ite_fib(n));
		long iteendTime = System.nanoTime();
        	long itetimeElapsed = iteendTime - itestartTime;
        	
        	System.out.println("Iterative Time required (ns):"+itetimeElapsed);
		
	}
	public static int rec_fib(int n){
		if (n<=1){
			return n;
		}
		return (rec_fib(n-1)+rec_fib(n-2));
	}
	
	public static int ite_fib(int n){
		int a = 0;
		int b = 1;
		int c;
		for(int i=0;i<n;i++){
			c = a+b; 
			a = b;
			b = c;
		}
		return a;
	}
}
