using System;
using System.Collections.Generic;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Stack of Strings");
		Stack<string> numbers = new Stack<string>();
        numbers.Push("twenty one");
        numbers.Push("thirty two");
        numbers.Push("sixty three");
       
		foreach( string s in numbers )
        {
            Console.WriteLine(s);
        }

        Console.WriteLine("\nPop", numbers.Pop());
        Console.WriteLine("Top: '{0}'",numbers.Peek());
        Console.WriteLine("Pop", numbers.Pop());
	
		Console.WriteLine("\nStack of Integers");
		Stack<int> figures = new Stack<int>();
        figures.Push(21);
        figures.Push(32);
        figures.Push(63);
       
        foreach( int i in figures )
        {
            Console.WriteLine(i);
        }

        Console.WriteLine("\nPop", figures.Pop());
        Console.WriteLine("Top: {0} ",figures.Peek());
        Console.WriteLine("Pop", figures.Pop());
	}
}
