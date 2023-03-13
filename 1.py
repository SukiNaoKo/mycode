




import numpy as np



class  play():
    def __init__(self):
        self.sum =np.array([[0, 1, 0, 0, 0]])

    def sum_nub(self):
        self.sum = self.sum+class_n()
        print(self.sum)



def class_n():
    return np.array([[0, 1, 2, 0, 0]])




if __name__ == "__main__":
    #prob_result = np.array([[0.7, 0.8, 0, 0, 0]])
    #prob_result_1 = np.array([[0.7, 0.8, 0, 0, 0]])
    #class_result = np.int64(prob_result > 0.7)
    #class_result_1 = np.int64(prob_result_1 > 0.7)
    #print(type(class_result))
    #sum =sum+class_result+class_result_1
    sum_1 = np.array([[0, 0, 1, 1, 0]])
    sum_2 = np.array([[1, 0, 0, 1, 0]])


    result1 = list(list(sum_1 ^ sum_2) & sum_2)

    #result1 = list(sum_1 ^ sum_2)
    #result1 = list(result1 & sum_2)
    print(result1)

    #sum_1 = ''
    #if  str(sum_1):
    #    print("1")
    #print(str(sum_1))
    #print(sum)
    #play1 = play()
    #play1.sum_nub()
    #class_result = ''
    #if (not  class_result):
     #   print(prob_result)