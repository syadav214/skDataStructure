int countingValleys(int n, string s)
{
	int curr_level =0, vally_counter=0;
	bool below_sea_level= false;

	foreach (var ch in s)
	{
		if(ch == 'U')
		{
			curr_level++;
		} else
		{
			curr_level--;
		}

		if(below_sea_level== false)
		{
			if(curr_level < 0)
			{
				below_sea_level = true;
			}
		} 
		else if(curr_level==0)
		{
			vally_counter++;
			below_sea_level= false;
		}
	}
	return vally_counter;
}


Console.Write(countingValleys(10, "UDUUUDUDDD"));