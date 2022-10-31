import os

print(os.listdir('.'))
os.mkdir('test123')
os.rmdir('test123')

cur_dir = os.getcwd()
print(cur_dir)
print(os.path.split(cur_dir))
print(os.path.dirname(cur_dir))
print(os.path.basename(cur_dir))

while os.path.basename(cur_dir):
    cur_dir = os.path.dirname(cur_dir)
    print(cur_dir)
