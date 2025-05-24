def accum(st: str) -> str:
    if not st: return ''

    final = []
    
    for n in range(len(st)):
        final.append(st[n].upper())
        
        for m in range(n):
            final.append(st[n].lower())
            
        if n < len(st) - 1:
            final.append('-')
            
    return ''.join(final)

print(accum('aBc'))
