
# To check if the ports are free on a Unix host, run:

$ netstat -an | egrep '4440|4443'

If the ports are in use on the server, you will see output similar to below:

tcp46      0      0  *.4440                 *.*                    LISTEN
