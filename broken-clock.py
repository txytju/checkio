from math import floor
def broken_clock(starting_time, wrong_time, error_description):
	durantion = con(wrong_time) - con(starting_time)
	err = error(error_description)
	# 实际时间间隔(s)
	actual_duration = durantion/err
	# 实际时间
	right_time = con(starting_time) + actual_duration

	return ":".join([format(right_time//3600), format(right_time%3600//60), format(floor(right_time%3600%60))])


def format(num):
	num = str(round(num))
	if len(num)==1:
		return "0"+num
	else :
		return num

def con(time):
	# 将时间从 "XX:XX:XX"转换成秒
	time = [int(i) for i in time.split(":")]
	return time[0]*3600 + time[1]*60 + time[2]


def error(error_description):
	s = error_description.split(" ")
	time = times(s[1], s[4])
	# 错误的时间
	x = int(s[3]) + int(s[0])*time
	# 返回错误时间是实际时间的多少倍
	return x/int(s[3])


def times(a,b):
	times = {"second":1, "minute":60, "hour":3600}
	for key_i, value_i in times.items():
		for key_j, value_j in times.items():
			if key_i in a and key_j in b:
				return value_i/value_j


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
