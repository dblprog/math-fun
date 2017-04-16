#!/bin/bash


# hash via shasum -a 256
# sort hash
# pass hash to awk
# for each term that's identical to prev term and has occurred before,
# print prev term and current term (guaranteed match because of sort)



find -X ./files -type f -name \*   | 
xargs shasum -a 256                      | 
sort                                     |
awk '{
        ++a[$1]; 
        b[$1] = b[$1] " " $2
    } END {
        for (keys in b) {
            if( a[keys] >1) 
            print b[keys] 
        }
      }'



#' {
#          if (a[$1] == 0) {
#          ++a[$1]; 
#          prev = $2
#        } 
#        else {
#          print prev " " $2;
#        }
#      } 
# '