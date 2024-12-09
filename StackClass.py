# Your Code & Heading go Here!
class ArrayStack:
  def __init__(self):
    self.__stack = []
    self.__size = 0

  def push(self,element):
    """Adding a new element to the stack"""
    self.__stack.append(element)
    self.__size += 1

  def pop(self):
    """Remove the top element from the stack"""
    emptyornot = self.__is_empty()
    if emptyornot == False:
      popvalue = self.__stack[-1]
      self.__stack.remove(self.__stack[-1])
      self.__size -= 1
      return popvalue
    else:
      raise IndexError("List is empty")
  def top(self):
    """Return the top of the stack"""
    emptyornot = self.__is_empty()
    if emptyornot == False:
      topvalue = self.__stack[-1]
      return topvalue
    else:
      raise IndexError("List is empty")
  def __is_empty(self):
    """Returns a booleen telling if the stack is empty, used in pop and top"""
    if len(self.__stack) == 0:

      return True
    else:
      return False  
  def __len__(self):
    """Returns the size of the stack"""
    return self.__size
  def __str__(self):
      """Display contents of stack"""
      out = ""
      for ele in self.__stack:
          out += str(ele) + ' '

      out += "<TOP"
      return out

