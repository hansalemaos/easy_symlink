# Creates symlinks and all folders in the symlink path if they don't exist

```python

# You don't have to worry about creating the folder(s).
# If the folder and subfolders don't exist, they will be created.
# If a symlink already exists at the given path, it will be overwritten.
# If something goes wrong, the function returns False
# If everything is fine, it returns True

from easy_symlink import create_symlink

pp = create_symlink(
    r"C:\pictest4\1671814710.650013.png",
    "f:\\aaaaaaaafolder1\\folder2\\folder3\\folder4\\img.png",
)
print(pp)
True



```


