int PageCount(int n,int p)
{
	return Math.Floor(Math.Min(p / 2, (n / 2 - p / 2)));
}

Console.Write(PageCount(5,3));