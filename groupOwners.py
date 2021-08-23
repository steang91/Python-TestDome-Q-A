def group_by_owners(files):
    flist = {}
    for m,n in files.items():
        
        flist.setdefault(n,[]).append(m)
    return flist
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))