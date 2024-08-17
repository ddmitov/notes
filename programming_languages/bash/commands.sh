# Bash One-liners:

# Hard disk serial number and LAN card MAC anndress:
sudo udevadm info --query=all --name=/dev/sda | grep ID_SERIAL= | cut -d'=' -f2
sudo cat /sys/class/net/$(ls /sys/class/net | head -n 1)/address

# Flash drive format:
sudo touch forcefsck
sudo fdisk -l
sudo mkdosfs -n 'USBDISK' -F 32 -I /dev/sdb1

# Linux administration:
lsb_release -a
sudo do-release-upgrade

sudo ls -l /var/crash
sudo rm /var/crash/*

# Networking:
sudo mcedit /etc/resolv.conf

nslookup example.com
whois 1.2.3.4

echo "Sending an attachment." | mutt -s "Mutt Test" -a file.txt -- name@mail.com

# Find & Grep:
find . -type f -print | grep '.svg'
find . -name filename.txt

grep -r --before-context=1 --after-context=1 --color=always keyword* /path/to/*.txt
grep -r --before-context=1 --after-context=1 --color=always keyword* .
grep -R 'pattern' .

pdfgrep --ignore-case --with-filename --page-number --recursive 'keyword' /full/path

# Image resizing:
mkdir resized; ls -1 *.JPG | xargs -n 1 bash -c 'convert "$0" "-resize" "20%" "./resized/resized_$0"; echo "Converting $0...";'

# OCR:
tesseract -l grc+bul+lat 0001.tif 0001.txt
convert -colorspace gray -type grayscale -format tiff -deskew 40% 0001.tif 0001-deskewed.tiff
convert -colorspace gray -type grayscale -format tiff -rotate -0.50 0001.tif 0001-deskewed.tiff

tesseract -l grc+bul+eng 0002.tif 0002

tesseract -l bul 0003.png 0003
