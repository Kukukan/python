# 수정전 로봇청소기 1회 사용 시작시간과 종료시간을 이용하여 요금을 계산한 코드

def InputData():
	s = input()
	e = input()
	return s, e

def ComputeTime():
	global stime
	global etime
	s = int(stime[0:2]) * 60 + int(stime[3:])
	e = int(etime[0:2]) * 60 + int(etime[3:])
	if s > e:	
		return (1440 - s + e)
	else:
		return (e - s)

def Solve():
	t = ComputeTime()
	if t < 30 : return 500
	tmp = (t-30+9)//10
	p = 500 + tmp * 300
	if p > 30000:
		p = 30000
	return p

def OutputData(sol):
	print(sol)

stime, etime = InputData() #입력 
sol = Solve() # 문제 해결
OutputData(sol) # 출력
