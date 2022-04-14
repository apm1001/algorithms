class Node:

    def __init__(self, data = None):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data['id'] < self.data['id']:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data['id'] > self.data['id']:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, id_to_found):
        if id_to_found < self.data['id']:
            if self.left is None:
                return str(id_to_found)+" Not Found"
            return self.left.findval(id_to_found)
        elif id_to_found > self.data['id']:
            if self.right is None:
                return str(id_to_found)+" Not Found"
            return self.right.findval(id_to_found)
        else:
            print(str(self.data['id']) + ' is found')
            return self.data
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data['id']),
        if self.right:
            self.right.PrintTree()

# first requirement 
def sequentialSearch(alist, item, value):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos][value] == item:
            found = True
        else:
           pos = pos+1
    return found

# third requirement
def binary_search(list, item, value):
  # в low и high хранятся границы части списка, где выполняется поиск
  low = 0
  high = len(list) - 1
  i = 0
  # Пока не останется один элемент
  while low <= high:
    # Проверяем средний элемент
    mid = (low + high) // 2
    guess = list[mid][value]
    # Значение найдено
    if guess == item:
      return mid
    # Значение велико
    if guess > item:
      high = mid - 1
    # Значение мало
    else:
      low = mid + 1
    i=i+1

  # Значение не найдено
  return None

# third requirement 
def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low]['id'] and val <= lys[high]['id']:
        index = low + int(((float(high - low) / ( lys[high]['id'] - lys[low]['id'])) * ( val - lys[low]['id'])))
        if lys[index]['id'] == val:
            return index
        if lys[index]['id'] < val:
            low = index + 1
        else:
            high = index - 1
    return -1

# fifth requirement
def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i]['id'] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i]['id'] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1]['id'] == val):
        return index+1
    return -1

def main():
    file = open('sorted_data.txt', 'r')
    lines = file.readlines()

    data = []

    tree = Node()
    for line in lines:
        info = line.strip().split(",")
        info_struct = {
            "id": int(info[0]),
            "name": info[1],
            "surname": info[2],
            "faculty": info[3],
            "date_of_birth": int(info[4]),
            "year_of_admission": int(info[5])
        }
        data.append(info_struct)

        tree.insert(info_struct)

    # tree.PrintTree()

    # print(tree.findval(50))

    # list must be sorted
    # print(binary_search(data, 11, 'id'))
    # list must be sorted
    # print(InterpolationSearch(data, 496))
    # list must be sorted
    # print(FibonacciSearch(data, 332))


    


if __name__ == "__main__":
    main()