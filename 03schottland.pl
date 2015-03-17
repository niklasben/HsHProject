use Net::Twitter::Lite::WithAPIv1_1;
use bigint;
use utf8;
use open qw/:std :utf8/;
use strict;
use warnings;
use Path::Class;
use Time::Piece;
use autodie;
use open ':encoding(utf8)';
binmode(STDOUT, ":utf8");

my $date = localtime->strftime('%Y%m%d');
my $filename = "TweetFile_Schottland_".$date.".txt";
my $dir = dir("E:/Download/Uni/Sem 6/Projekt/TwitterFiles");
my $file = file($filename);
my $file_handle = $file->openw();

  my $searchterm = "schottland OR scotland OR alba OR caledonia OR schottisch OR schotte OR schottin OR schotten
  					OR schottinnen OR edinburgh";

  my $nt = Net::Twitter::Lite::WithAPIv1_1->new(
      traits   => [qw/API::Search/],
      consumer_key        => "4CmmEPwA7ddOi94EoOBYJz4Xk",
      consumer_secret     => "3gKLa57CwoAvEeoQONNhYwnLlDoLOPjucH3xxiyerxPVCZjjWr",
      access_token        => "424193298-Vt2UPLanePcN4eJgnWx5xyMky1CbFoGx5rojD9oV",
      access_token_secret => "y5BSZ3x6EW6BZYjoEMmvPaA3pfeT2hwo44h55LmTMhEaR",
      ssl => 1 
  );
  
my $r;
  eval {
	my $lastid = 0;
	my $more = 0;
	my $wait = 0;
	my $cn = 0;
	do {
		if ($more == 0) {
			$r = $nt->search({q => $searchterm, count => "100" , lang => "de" });
		} else {
			$r = $nt->search({q => $searchterm, count => "100" , lang => "de" , max_id => $lastid });
		}
		$more = 0;
		
		for my $status ( @{$r->{statuses}} ) {
				$more = 1;
				$cn++;
				$lastid = $status->{id}; 
				 
				# print "$lastid\t";
				#binmode(STDOUT, ":utf8");
				$file_handle->print($cn."\t".$status->{id}."\t".$status->{created_at}."\t".$status->{text}."\n")
				#'\t' {text} . "\n");

				
		}
		$wait++;
		if($wait >= 175){
			sleep 900;
			$wait = 0;
		}
    } while ($more == 1);
  };
  warn "Error: $@\n" if $@;
