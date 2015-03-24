
while (<>) {

		if(/[\w\s]*2015\s([\w\s\D]*)/)
		{
			print $1."\n";
		}
}



