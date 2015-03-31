my $dir ='C:/users/Daniel/HshProject/cleaningandcountingscript/LemmaInput';
my $dir_fc = 'C:/users/Daniel/HshProject/LemmaMerged'; 

$counter = 0;

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
	foreach my $str (split "\t", $line) {
       $count{$str}++;
    }
}
 
foreach my $str (sort { $count{$b} <=> $count{$a} } keys %count) {
	print (new_file $str, "\t".$count{$str}."\n");
	}	
}