#You have a billion urls, where each is a huge page. How do you detect the duplicate documents?

Each url is an average of 100 characters and each character is 4 bytes. 
=> 10 billion URL take up about 4 TB

=> => Disk Storage
assuming each disk block takes up 1 GB. We can using 4000 data blocks and also, there is an unique hash value for each 
data blocks. hash_code = (URL) / 4000.

=> duplicated urls must be in the same data block and so we can fetch one data block at one time and looking for the duplicates



