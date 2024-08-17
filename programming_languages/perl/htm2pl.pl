#!/usr/bin/perl

# HTM2PL v.0.1
# Convert HTML files to Perl code.
# You can redistribute and/or modify this script under
# the same terms as PERL itself.
# Author: Dimitar D. Mitov ddmitov@yahoo.com

# Beginning and end of every line in the perl code.
$start = "print \"";
$end = "\\n\"\;";

# BOM definition:
$BOM = "\x{ef}\x{bb}\x{bf}";

# Take the command line arguments:
$input = $ARGV[0];
$output = $ARGV[1];

# Open input file for reading:
open(FILE, "$input") or usage();
@file=<FILE>;
close (FILE);

# Convert:
open(FILE, ">$output");
foreach $line (@file){
    #Remove Byte Order Mark in UTF-8 encoded files.
    $line =~ s/$BOM//;
    # Replace double quotes with single quotes.
    $line =~ s/\"/\'/g;
    # Remove the new line character (carriage return).
    chomp $line;
    print FILE "$start$line$end\n"}
close (FILE);

print "\n";
print "Operation successfull!\n";
print "\n";
exit 0;

# Help and credits:
sub usage{
print "\n";
print "HTM2PL --\n";
print "Convert HTML files to Perl code. \n";
print "\n";
print "Usage:\n";
print "perl htm2pl.pl input.htm output.pl\n";
print "\n";
print "Written by Dimitar D. Mitov (ddmitov\@yahoo.com)\n";
print "\n";
}
