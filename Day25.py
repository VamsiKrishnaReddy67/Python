from pathlib import Path
print(Path.cwd)

folder=Path("Day26")
folder.mkdir(exist_ok=True)
print("Folder Created")

file=Path("studen.txt")
file.touch()
print("File Created")

file=Path("studen.txt")
file.write_text("Name:vamsi\n Age:21\n Branch:CSM")

file=Path("studen.txt")
data=file.read_text()
print(data)

exist=Path("studen.txt")
print(exist.is_file)

prin=Path("project/data/studen.txt")
print(prin.name)
print(prin.suffix)
print(prin.parent)

fold=Path("python")
for item in folder.iterdir():
    print(item)

pathlib=Path("project")/"data"/"studen.json"





