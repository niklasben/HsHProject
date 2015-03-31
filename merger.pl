

my $dir ='C:/users/Daniel/HsHProject/cleanedoutput';


$counter = 0;
open (file, '>', 'Merged.txt');
foreach my $fp (glob($dir."/*.txt")) {
	$counter += 1;
	open (r_file, '<', $fp);
	@tweets = <r_file>;
	@path_name = split('/', $fp);
	$name = @path_name[scalar @path_name - 1];
	@name = split ('_', $fp); 
		foreach $line (@tweets){
		print(file @name[1]."\t".$line);
		} 
		
			
}

