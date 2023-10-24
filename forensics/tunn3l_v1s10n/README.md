xxd the file

notice that the first 2 chars are BMP suspect the file is in BMP format
rename with bmp extension

go and see the bmp file format (headers etc)
use hexedit

offset 02 is the file size, in this case 
8e26 2c00
file length is 002c2680, looks plausible

starting address -> offset 0A, in this case 
bad0 (this is corrupted)
offset 0A -> 14 (offset of the header size) + 40 bytes = 54 bytes = 36 hex

windows bitmapinfoheader, header size = 40 bytes = 28 hex at offset 0E

it says not a flag

offset 16 is for the height of the bitmap
try increasing
it seems that we reveal more of the image
increase again
***here, the most significant byte comes last***

picoCTF{qu1t3_a_v13w_2020}
