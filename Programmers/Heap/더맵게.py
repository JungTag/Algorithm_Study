import heapq as hq

def solution(scoville, K):
	answer = 0
	hq.heapify(scoville)
	while scoville:
		try:  # len(scoville) > 1로 검사하는 것은 효율성 측면에서 매우 비효율적이므로 예외 처리를 함
			min_sco = hq.heappop(scoville)
			second_sco = hq.heappop(scoville)
		except:
			return -1
		mix_sco = min_sco + (second_sco * 2)
		answer += 1
		hq.heappush(scoville, mix_sco)
		if scoville[0] >= K:
			break
	return answer