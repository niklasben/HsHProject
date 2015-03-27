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

my @countries = (
	'Frankreich',
	'Spanien',
	'England',
	'Großbrittanien',
	'Nordirland',
	'Schottland',
	'UK',
	'Griechenland',
	'Russland',
	'Norwegen',
	'Finnland',
	'Ungarn',
	'Ukraine',
	'Türkei',
	'Holland',
	'Niederlande',
	'Bulgarien',
	'Kroatien',
	'Irland',
	'Daenemark',
	'Schweden',
	'Polen',
	'Tschechien',
	'Italien',
	'Portugal'
);
my @terms = (
	"frankreich OR france OR französisch OR franzose OR französin OR franzosen OR französinnen OR paris",
	"spanien OR spain OR espana OR spanisch OR spanier OR spanierin OR spanierinnen OR barcelona OR madrid",
	"england OR englaender OR englaenderin OR englaenderinnen OR englisch OR london",
	"großbritannien OR greatbritain OR britisch OR british OR brite OR britin OR briten OR britinnen",
	"nordirland OR northern_ireland OR nordire OR nordirin OR nordiren OR nordirinnen OR nordirisch OR belfast",
	"schottland OR scotland OR alba OR caledonia OR schottisch OR schotte OR schottin OR schotten OR schottinnen OR edinburgh",
	"uk OR unitedkingdom OR united_kingdom",
	"griechenland OR hellas OR greece OR elliniki dimokratia OR grieche OR griechin OR griechen OR griechinnen OR griechisch OR athen",
	"russland OR russia OR rossija OR russe OR russin OR russen OR russinnen OR russisch OR moskau",
	"norwegen OR norway OR norge OR norwegisch OR norweger OR norwegerin OR norwegerinnen OR oslo",
	"finnland OR finland OR suomi OR finnisch OR finne OR finnen OR finnin OR finninnen OR helsinki",
	"ungarn OR hungary OR magyarorszag OR ungarisch OR ungar OR ungarin OR ungarinnen OR budapest",
	"ukraine OR ukrajina OR ukrainisch OR ukrainer OR ukrainerin OR ukrainerinnen OR kiev",
	"tuerkei OR turkey OR tuerkiye cumhuriyeti OR tuerkisch OR tuerke OR tuerken OR tuerkin OR tuerkinnen OR ankara OR instanbul",
	"holland OR holländisch OR holländer OR holländerin OR holländerinnen OR Amsterdam OR Den_Haag",
	"niederlande OR netherlands OR nederland OR niederländisch OR niederländer OR niederländerin OR niederländerinnen OR nederlan",
	"bulgarien OR bulgarisch OR bulgare OR bulgaren OR bulgarin OR bulgarinnen OR sofia OR Bălgarija OR Bulgaria",
	"kroatien OR croatia OR Hrvatska OR Kroatisch OR Kroate OR Kroaten OR Kroatin OR Kroatinnen OR Zagreb",
	"Irland OR Ireland OR Eire OR irisch OR irish OR Ire OR iren OR irin OR irinnen OR Dublin",
	"Daenemark OR Denmark OR Danmark OR Daenisch OR Daene OR Daenen OR Daenin OR Daeninnen OR Kopenhagen",
	"schwedisch OR Schweden OR sweden OR schwede OR schwedinnen OR schwedin OR sverige OR stockholm",
	"polen OR pole OR polin OR polska OR poland OR warsaw OR warschau OR polnisch",
	"tschechien OR tschechisch OR tscheche OR tschechin OR czech OR czechia OR ceska OR prag",
	"italien OR italy OR italia OR italiener OR italienerin OR italienerinnen OR rom OR italienisch",
	"portugal OR portoguesa OR portugiesisch OR portugiese OR portugiesin OR portugiesen OR portugiesinnen OR lissabon"
);
my $country = ""; 
my $date = localtime->strftime('%Y%m%d');
my $filename = "TweetFile_".$country."_".$date.".txt";
my $dir = dir("../Output");
my $file = $dir->file($filename);
my $file_handle = $file->openw();
my $searchterm;

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
	my $time;
	my $resume = 0;
	my $selected = 0;
	do {
		print "please select a country number!('0' to end script)\n";
		my $cl = 0;
		foreach (@countries){
			$cl++;
			print "$cl. $_ ";
		}
		print "\n";
		$selected = <>;
		if($selected >= 1 && $selected <= 25){
			$selected--;
			$searchterm = $terms[$selected];
			print $searchterm;
			$country = $countries[$selected];
			print $country;
			$resume = 1;
			print "please provide current wait status (calls since last wait):\n";
			$wait = <>;
			do {
				if ($more == 0) {
					$r = $nt->search({q => $searchterm, count => "100" , lang => "de" });
				} else {
					$r = $nt->search({q => $searchterm, count => "100" , lang => "de" , max_id => $lastid });
				}
				$more = 0;
				my $no = 0;
				for my $status ( @{$r->{statuses}} ) {
					$more = 1;
					$cn++;
					$no++;
					$lastid = $status->{id};
					 
					# print "$lastid\t$no";
					#binmode(STDOUT, ":utf8");
					$file_handle->print($cn."\t".$status->{id}."\t".$status->{created_at}."\t".$status->{text}."\n")
					#'\t' {text} . "\n");	
				}
				if($no <= 1){
					$more = 0;
				}
				$wait++;
				if($wait >= 175 && $more == 1){
					$time = localtime;
					print "$time - Reached 175 Calls, sleeping for 15 minutes!\n";
					sleep 5;
					sleep 900;
					$wait = 0;
				}
			} while ($more == 1);
			my $end = localtime;
			print "$end - finished running script for $country. $cn tweets! - Calls since last wait: $wait\n";
		} elsif($selected == 0){
			$resume = 0;
			print "\n Ending Script!";
		} else {
			print "Wrong input, try again";
		}
	} while ($resume == 1)
};
warn "Error: $@\n" if $@;
