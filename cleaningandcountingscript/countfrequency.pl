my $dir ='cleanedoutput';
my $dir_fc = 'freq/'; 

$counter = 0;
#function to read in all the data in a specific folder and run the sub function until all data has been written.
foreach my $fp (glob($dir."/*.txt")) {
	$counter += 1;
	print ($counter."\n");
	open(file, "<", $fp);
	print($fp." completed\n");
	@path_name = split('/', $fp);
	$name = @path_name[scalar @path_name - 1];
	open(new_file, ">", $dir_fc.$name);
	countfrequency(file, new_file);
	close(file);
}

sub countfrequency(file, new_file) {
	$fh = file;
	my %count;
while (my $line = <$fh>) {
    chomp $line;
	foreach my $str (split "\t", $line) { ###foreach loop to make a hash and every word is counted.
       $count{$str}++;
    }
}
 
foreach my $str (sort { $count{$b} <=> $count{$a} } keys %count) { ###foreach loop to sort hash after the biggest number and print it in new file. 
	print (new_file $str, "\t".$count{$str}."\n");
}	
}