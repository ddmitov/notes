perl -e 'print join "\n", @INC'
perl -e 'foreach $t(@INC) {print "Found perl5db.pl in $t!\n" if (-e "$t/perl5db.pl");}'
perl -e 'use Config; print $Config{perlpath}'

perl -MO=Lint script.pl
perl -MLWP::Simple -e 'mirror("http://www.perl.com/", "perl.html")';
perl -MXML::LibXML -e 'print $INC{"XML/LibXML.pm"}'
perl -MXML::LibXML -MDynaLoader -E 'say for sort @DynaLoader::dl_modules;'
