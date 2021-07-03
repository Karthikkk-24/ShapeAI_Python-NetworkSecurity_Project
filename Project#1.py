import hashlib

md5_converted = hashlib.md5(b'Cybersecurity')

#This is the pure MD5 conversion of the word
print("Converted text in MD5 (HexCode Form)",end = "")
print(md5_converted.digest())

#This is the HexCode version of MD5 conversion
md5_converted_hex = hashlib.md5(b'Cybersecurity').hexdigest()
print("Converted text in MD5 (HexCode Form)",md5_converted_hex)

