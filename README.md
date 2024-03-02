# R.T.L.O.I.F.Y
![RTLOIFY](https://gainsec.com/wp-content/uploads/2024/03/marble-knd.png)

Script to create strings with RTLO characters, change single filenames or even entire directories. Meant to be used for RTLO bypasses/testing in regards to hacking, offensive cyber security and penetration testing. 

## Getting Started

cd /opt/

git clone https://github.com/GainSec/RTLOify

cd RTLOify

chmod +x rtloify.py

### Prerequisites

Python 3.6+ 

## Author

* **Jon Gaines** - *Creator* - [GainSec](https://github.com/GainSec) - Managing Security Consultant @NetSPI

## To Do

* Fill metadata of files with RTLO characters as well
* Add arg for location RTLO character (RN it's before the file extension)
* Built out a better default value within files created

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details


## Example and How To

Strings Example:

* (Interactive Mode) ./RTLO-Maker.py --s

OR 

./RTLO-Maker.py --s test.txt

Single File Example:

* (Interactive Mode) ./RTLO-Maker.py --f

OR 

* ./RTLO-Maker.py --f ~/Payloads/test.txt

Directory Example:

* (Interactive Mode) ./RTLO-Maker.py --d

OR 

* ./RTLO-Maker.py --d --sd ~/Source/Directory --dd ~/Destination/Directory