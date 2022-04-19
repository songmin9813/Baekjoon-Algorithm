def getMoneyText(count):#지금 인자로 받은 count는 숫자 형태가 아니라 스트링 형태임!
  number = list(count)  # num의 각자리수를 list로 저장
  #스트링을 리스트화 시켰기 때문에 number 각각에는 숫자 스트링 값이 저장되어 있다

  number_string = [' ', '일','이','삼','사','오','육','칠','팔','구']#1을 한글로 바꾸는 단순 작업
  unit_string = ['','십','백','천','만','십','백','천','억']#nlen을 인덱스로 쓰는 리스트
  #unit_string은 뒤에서부터 검색하는 특징을 가짐. 잘 만들었네!

  nlen=len(number)-1
  
  for i in number:#아직 i에는 각 스트링이 저장
    if i=='0':#0
        print('%s:' %i)
        nlen=nlen-1 
    else:
       print('%s: %s%s' %(i,
       number_string[int(i)],
       unit_string[nlen]))
       nlen = nlen-1

  print('{:,}'.format(int(count)))

count=input('금액을 숫자로 입력:')
getMoneyText(count) 
print("{:,}".format(int(count)))