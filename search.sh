#!/bin/bash

# Rang kodlari
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m' # rangni tiklash

clear
echo -e "${BLUE}---------------------------------------------------${NC}"
echo -e "${YELLOW} exploits modulidan qidirish uchun --> 1${NC}"
echo -e "${YELLOW} auxiliary modulidan qidirish uchun --> 2${NC}"
echo -e "${YELLOW} Ikkala moduldan ham qidirish uchun --> 3${NC}"
echo -e "${BLUE}---------------------------------------------------${NC}"

read -p $'\e[1;32mTanlang (1/2/3): \e[0m' option

# Mumkin bo'lgan pathlar
path1="/opt/metasploit-framework/embedded/framework/modules"
path2="/usr/share/metasploit-framework/modules"

# Qaysi path mavjud bo'lsa, shuni ishlatadi
if [ -d "$path1" ]; then
  path="$path1"
elif [ -d "$path2" ]; then
  path="$path2"
else
  echo -e "${RED}❗ Metasploit modul papkasi topilmadi.${NC}"
  echo -e "${YELLOW}Metasploit o‘rnatilganligini va path to‘g‘ri ekanligini tekshiring.${NC}"
  exit 1
fi

while true; do
  read -p $'\e[1;32mQidirish uchun kalit so\'zni kiriting: \e[0m' keyword
  keyword="*$keyword*.rb"
  > ./search_result.txt

  # Loader animatsiyasi funksiyasi
  loader() {
    local pid=$!
    local spin='-\|/'
    echo -ne "${YELLOW}Qidirilmoqda "
    while kill -0 $pid 2>/dev/null; do
      for i in $(seq 0 3); do
        echo -ne "\b${spin:$i:1}"
        sleep 0.1
      done
    done
    echo -e "\b Done!${NC}"
  }

  # Qidirishni parallel boshlash
  {
    case $option in
      1)
        find "$path/exploits" -iname "$keyword" 2> /dev/null >> ./search_result.txt
        ;;
      2)
        find "$path/auxiliary" -iname "$keyword" 2> /dev/null >> ./search_result.txt
        ;;
      3)
        find "$path/exploits" -iname "$keyword" 2> /dev/null >> ./search_result.txt
        find "$path/auxiliary" -iname "$keyword" 2> /dev/null >> ./search_result.txt
        ;;
      *)
        echo -e "${RED}❗ Noto‘g‘ri tanlov! Chiqilmoqda.${NC}"
        exit 1
        ;;
    esac
  } & loader

  if [[ -s ./search_result.txt ]]; then
    count=$(wc -l < ./search_result.txt)
    echo -e "${GREEN}✅ $count ta mos modul topildi.${NC}"
    break
  else
    echo -e "${RED}⚠️ Hech narsa topilmadi. Yana urinib ko‘ring.${NC}"
  fi
done
