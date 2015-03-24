
while (<>) {
	if(/\w*\t\w*\t(\w*)/)
	{
		print $1." ";
	}
}