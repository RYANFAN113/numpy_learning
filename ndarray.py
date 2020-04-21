#%%
import tensorflow as tf
import numpy as np
print(tf.__version__)
print(np.__version__)

#%%
a=np.arange(5)
print(a)
print(a.dtype)
print(a.shape)

#%%
m= np.array([np.arange(2), np.arange(2)])
print(m)
print(m.shape)

#%%
x=np.array([np.arange(3), np.arange(3), np.arange(3)])
print(x)
print(x.shape)
print([1,1])

#%%
b = np.arange(7, dtype=np.uint16)
print(b)
print(b.dtype)
print(b.dtype.itemsize)

#%%
c=np.arange(3, 4, .01, dtype='f2')
print(c)

#%%
np.dtype('f')
np.sctypeDict.keys()

#%%
t = np.dtype([('name', np.str, 40), ('numitems', np.int32), ('price', np.float32)])
print(t)
print(t['name'])
itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
print(itemz)
print(itemz[1])

#%% [markdown]
## 用一个长度为40个字符的字符串来记录商品名称，
## 用一个32位的整数来记录商品的库存数量，
## 最后用一个32位的单精度浮点数来记录商品价格

#%%


#%%


#%%
