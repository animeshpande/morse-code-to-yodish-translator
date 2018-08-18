import urllib.request

morse_to_english_mapping = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
                            '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                            '-.--': 'Y', '--..': 'Z',
                            '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                            '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

def from_morse(s):
    return ''.join(morse_to_english_mapping.get(i) for i in s.split())

def translate(a):
    words = a.split('/')
    return ''.join(from_morse(word)+' ' for word in words)

english = translate(input("Please enter the morse code: ")).replace(' ','+')

req = urllib.request.Request('https://yoda.p.mashape.com/yoda?sentence='+english)
req.add_header('X-Mashape-Key','eydTwfm4qdmshR5mnMCppdSA5wQCp1vwlu7jsn9xQRVWrRI5BM')
req.add_header('Accept','text/plain')
response = urllib.request.urlopen(req).read()

translation = str(response)[str(response).find("'")+1:-1]

ascii_yoda = """\
    \\
     \\
                   ____
                _.' :  `._
            .-.'`.  ;   .'`.-.
   __      / : ___ ;  /___ ;       __
 ,'_ \"\"--.:__;\".-.\";: :\".-.\":__;.--\"\" _`,
 :' `.t\"\"--.. '<@.`;_  ',@>` ..--\"\"j.' `;
      `:-.._J '-.-'L__ `-- ' L_..-;'
        \"-.__ ;  .-\"  \"-.  : __.-\"
            L ' /.------. ' J
             \"-.   \"--\"   .-\"
            __.l\"-:_JL_;-\";.__
         .-j/'.;  ;\"\"\"\"  / .'\"-.
       .' /:`. \"-.:     .-\" .';  `.
    .-\"  / ;  \"-. \"-..-\" .-\"  :    \"-.
 .+\"-.  : :      \"-.__.-\"      ;-._
 ;   `.; ;                    : : \"+. ;
 :  ;   ; ;                    : ;  : :
 ;  :   ; :                    ;:   ;  :
:   ;  :  ;                  : ;  /  ::
;  ; :   ; :                  ;   :   ;:
:  :  ;  :  ;                : :  ;  : ;
;    :   ; :                ; ;     ; ;
: `.\"-;   :  ;              :  ;    /  ;
 ;    -:   ; :              ;  : .-\"   :
 :       :  ;            : .-\"      :
  ;`.      ; :            ;.'_..--  / ;
  :  \"-.  \"-:  ;          :/.\"      .'  :
             :          ;/  __        :
           .-`.        /t-\"\"  \":-+.   :
     `.  .-\"    `l    __/ /`. :  ; ;   ;
          .-\" .-\"-.-\"  .' .'j   /   ;/
         / .-\"   /.     .'.' ;_:'    ;
         :-\"\"-.`./-.'     /    `.___.'
                `t  ._  /
                \"-.t-._:'
"""

print(' '+'-'*len(translation))
print('<'+translation+'>')
print(' '+'-'*len(translation))
print(ascii_yoda)
