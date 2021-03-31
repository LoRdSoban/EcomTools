from bs4 import BeautifulSoup as bs
import requests as r 
import re


def Get_Page_Source(page_url):
    response = r.get(page_url)
    return response


def beautify_and_find_all_script_tags(source):
    soup = bs(source.content, "html.parser")
    scripts = soup.find_all("script")
    
    return scripts


def find_stock_value(script_tags):



    ## Previously used for debugging ##
    #              |                  #
    #              |                  #
    #              ▼                  #
    

    #print(script_tags[136])
    #print(type((script_tags[143]).content))

###############################################################################

    # Actual code #
          
    for i in range(130, len(script_tags)):
    
        r = re.findall(r'\w+', str(script_tags[i]))

        if r[1] == "window":
            if r[2] == "LZD_RETCODE_PAGENAME":
                if r[3] == "pdp":
                    break
###############################################################################                

    ## Previously used for debugging ##
    #              |                  #
    #              |                  #
    #              ▼                  #
    
    
    #for i in range(len(script_tags)):
        #print("\n",i,"\n")
        #print(script_tags[i])
    
###############################################################################
    
    for i in range(len(r)):
        if r[i] == "stoock":
            return r[i+1]
            break



def main():
    
    url = input("Enter the URL:")

    page_source = Get_Page_Source(url)

    all_script_tags = beautify_and_find_all_script_tags(page_source)

    stock = find_stock_value(all_script_tags)

    print(f"\n Stock: {stock}")

    input()






if __name__ =="__main__":
    main()
