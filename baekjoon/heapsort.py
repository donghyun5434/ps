import heapq  #heap자료형 사용을 위해 모듈 import

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []    #heap자료형은 트리구조이지만 직관적으로 리스트로 트리로 퉁쳐서 표현
    #즉 h리스트가 곧 힙 자료형 그자체이다
    result= []
# 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)  #h라는 heap에 heapq 모듈안의 함수 heappush를 사용해서 value insert
# 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result. append (heapq. heappop (h))
    return result
 
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)