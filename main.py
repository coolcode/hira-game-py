import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
HIRAGANA = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo',
    'ん': 'n',
}

def main():
    correct = 0
    total = 0
    wrong_hiragana_list = set()

    while True:
        hiragana, roma = rand_hiragana()
        ans = input(f"{total+1}. {bcolors.BOLD}{hiragana}{bcolors.ENDC} romaji❓︎")
        if ans == 'q':
            print('QUIT')
            return
        if ans == 'w':
            print('❌ wrong list: ', wrong_hiragana_list) if len(wrong_hiragana_list)>0 else print("🈚️")
        elif ans == roma:
            correct += 1
            total += 1
            correct_rate = int(correct*100/total)
            print(f" {bcolors.BOLD}({hiragana} {roma}){bcolors.ENDC} ✅ 📃 {correct} / {total}, {correct_rate}%")
        else:
            # wrong answer
            wrong_hiragana_list.add(hiragana)
            total += 1
            correct_rate = int(correct*100/total)
            print(f" {bcolors.FAIL}({hiragana} {roma}){bcolors.ENDC} ❌ 📃 {correct} / {total}, {correct_rate}%")

def rand_hiragana():
    hiragana = random.choice(list(HIRAGANA.keys())) 
    return hiragana, HIRAGANA[hiragana]


GAME_TITLE = """
----------------------
Hiragana Learning Game
    平假名学习游戏
       /\_/\  
      ( o.o ) 
       > ^ <
     あいうえお
----------------------
💡 q: quit, w: wrong list
"""

if __name__ == "__main__":
    main()
