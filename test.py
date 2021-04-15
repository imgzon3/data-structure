names = ['철수', 'admin', '영희', '성재', '인성']
# names = []

if len(names) == 0: # 이름 리스트가 비어있는 경우, 5-9
    print('사용자가 있어야 합니다!')

else:
    for i in names:
        if i=='admin': # 계정 이름이 admin인 경우
            print('관리자님 안녕하세요, 상태 보고서를 보시겠습니까?')
        else:
            print(i,'님 안녕하세요, 다시 로그인해주셔서 감사합니다.')