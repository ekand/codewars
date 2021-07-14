# https://www.codewars.com/kata/array-mash/python

def array_mash(a, b):
    mesh = []
    for one, two in zip(a, b):
        mesh.extend([one, two])
    return mesh
