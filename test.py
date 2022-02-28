from rectangle_overlaps import solution
import unittest

class allTest(unittest.TestCase):
    def test_case1(self):
        inputvalue={"A":[(1,1),(4,1),(1,3),(4,3)],"B":[(3,2),(5,0),(8,3),(6,5)]}
        self.output = solution(inputvalue)
        self.assertEqual(self.output,True)

    def test_case2(self):
        inputvalue={"A":[(1,1),(4,1),(1,3),(4,3)],"B":[(5,5),(8,5),(5,7),(8,7)]}
        self.output = solution(inputvalue)
        self.assertEqual(self.output,False) 

    def test_case3(self):
        inputvalue={"A":[(1,1),(4,1),(1,3),(4,3)],"B":[(1,1),(1,3),(-2,1),(-2,3)]}
        self.output = solution(inputvalue)
        self.assertEqual(self.output,True)  

    def test_case4(self):
        inputvalue={"A":[(1,1),(4,1),(1,3),(4,3)],"B":[(1,1),(3,-1),(1,-3),(-1,-1)]}
        self.output = solution(inputvalue)
        self.assertEqual(self.output,True)     

    def test_case5(self):
        inputvalue={"A":[(1,1),(4,1),(1,3),(4,3)],"B":[(0.5,0.5),(3,-1),(1,-3),(-1,-1)]}
        self.output = solution(inputvalue)
        self.assertEqual(self.output,False)         

           
if __name__ == '__main__':
    unittest.main()
