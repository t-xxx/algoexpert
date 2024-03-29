class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
        
    # 再帰的に(insertを使用して)ノードを入れる
    def insert(self, value):
	    if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
        return self

    # valueに等しい値がBSTに含まれているかどうかを探索する
    def contains(self, value):
        # Write your code here.
        if value < self.value:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		elif value > self.value:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)
		else:
			return True

    # valueにあたる値を削除する
    def remove(self, value, parent=None):
		if value < self.value:
			if self.left is not None:
				return self.left.remove(value, self)
		elif value > self.value:
			if self.right is not None:
				return self.right.remove(value, self)
		else:
			if self.left is not None and self.right is not None:
				self.value = self.right.getMinValue()
				self.right.remove(self.value, self)
			elif parent is None:
				if self.left is not None:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right is not None:
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
				else:
					pass
			elif parent.left == self:
				parent.left = self.left if self.left is not None else self.right
			elif parent.right == self:
				parent.right = self.left if self.left is not None else self.right
		return self

    # 子ノードの左(値が小さいほう)を再帰的に呼び出す
    def getMinValue(self):
		if self.left is None:
			return self.value
		else:
			return self.left.getMinValue()