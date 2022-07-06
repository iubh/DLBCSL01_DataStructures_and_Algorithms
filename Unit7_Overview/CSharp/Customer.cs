using System;
					
public class Customer
{
	private string _name;
    public string name
    {
        get
        {
            return _name;
        }
        set
        {
            _name = value ;
        }
    }
	int _age;
	public int age {
 		get { return _age; } 
 		set { _age = value; } 
	}
	public int ID 
	{ get; set; }
	
}

public class Program
{
	public static void Main()
	{
		var t = new Customer();
		t.name = "John Doe";
		Console.WriteLine(t.name);
		t.age = 25;
		Console.WriteLine(t.age);
		t.ID = 111222333;
		Console.WriteLine(t.ID);
	}
