import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = [line.split('  ') for line in self.file.splitlines()]
    self.left = sorted([int(line[0]) for line in self.lines])
    self.right = sorted([int(line[1]) for line in self.lines])
    
  def part1(self):
    return sum(abs(left-right) for left,right in zip(self.left,self.right))
  
  def part2(self):
    unique_right = list(set(self.right))
    freq_right = {num: self.right.count(num) for num in unique_right}
    return sum([i * freq_right.get(i,0) for i in self.left])
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')