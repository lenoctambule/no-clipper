import sys
import scanner

HELP_MESSAGE = "Usage : python scanner.py <batch_size> <url>"
DEBUG_MSGS = {'init' : "Initalising scan ...", 
                'start' : "Scan initialized\n[Scan running] \nPress Ctrl+C to stop" }

if __name__ == "__main__":
    if len(sys.argv) != 3 :
        print(HELP_MESSAGE)
        exit(0)
    batch_size = None
    api_url = None

    try :
        batch_size = int(sys.argv[1])
        api_url = sys.argv[2]
    except :
        print("Invalid args. \n",HELP_MESSAGE)
        exit(0)

    print(DEBUG_MSGS['init'])
    scan = scanner.Scan(api_url, mode=scanner.scanmode.RAND)

    print(DEBUG_MSGS['start'])
    while (1):
        scan.genbatch_from_rand(batch_size)
        scan.startscan()
